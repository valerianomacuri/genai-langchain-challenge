from typing import List

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough
from langchain_openai import ChatOpenAI

from app.shared.settings import settings
from app.shared.vector_store import vector_store

# 1. Configuración del LLM
llm: ChatOpenAI = ChatOpenAI(
    api_key=settings.openai_api_key, temperature=0, model=settings.openai_llm_model
)

# 2. Configuración del Retriever
# (Nota: vector_store.as_retriever devuelve un VectorStoreRetriever)
retriever = vector_store.as_retriever(search_kwargs={"k": 5})


# 3. Función auxiliar para formatear docs (Con tipado)
def format_docs(docs: List[Document]) -> str:
    """Combina el contenido de múltiples documentos en un solo string."""
    return "\n\n".join(doc.page_content for doc in docs)


# 4. Prompt Template
template: str = """Usa el siguiente contexto para responder a la pregunta.
Si no sabes la respuesta, di que no lo sabes.

Contexto:
{context}

Pregunta: {question}
"""
prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(
    template,
)

# 5. Construcción de la Cadena (LCEL Puro)
# El tipo Runnable generalmente toma un input (dict/str) y devuelve un output (str/dict)
rag_chain: Runnable = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


def answer_query(query: str) -> str:
    """Ejecuta la cadena RAG y devuelve la respuesta como string."""
    return rag_chain.invoke(query)
