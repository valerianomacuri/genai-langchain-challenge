from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.shared.logging import logger
from app.shared.vector_store import add_document

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)


def process_document(doc_id: str, content: str, metadata: dict):
    # Dividir en chunks
    chunks = text_splitter.split_text(content)
    logger.info(f"{len(chunks)} chunks generados para el documento {doc_id}")

    # Agregar al vector DB
    add_document(doc_id, chunks, metadata)
    logger.info(f"Documento {doc_id} agregado a Vector DB")
