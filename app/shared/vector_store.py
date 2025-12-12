from typing import Any, Dict, List

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.shared.settings import settings

# 1. Inicialización
embeddings = OpenAIEmbeddings(
    api_key=settings.openai_api_key, model=settings.openai_embedding_model
)

# Al conectar por host/port, la persistencia la maneja el servidor remoto/docker
vector_store = Chroma(
    client_settings=None,  # Opcional, dependiendo de tu versión exacta, pero host/port suele bastar
    host=settings.chroma_host,
    port=settings.chroma_port,
    embedding_function=embeddings,
    collection_name="documents",  # Recomendado: definir un nombre explícito
)


def add_document(doc_id: str, texts: List[str], metadata: Dict[str, Any]) -> None:
    """Añade documentos al vector store. La persistencia es automática."""
    vector_store.add_texts(
        texts=texts,
        metadatas=[metadata] * len(texts),  # Replica la metadata para cada chunk
        ids=[f"{doc_id}_{i}" for i in range(len(texts))],
    )


def query_vector_db(query: str, k: int = 5) -> List[Any]:
    """Busca los k documentos más similares."""
    return vector_store.similarity_search(query, k=k)
