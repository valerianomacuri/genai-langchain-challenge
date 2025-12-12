import io

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pypdf import PdfReader  # Necesario para leer el PDF en memoria

from app.services.document_service import process_document
from app.shared.logging import logger

router = APIRouter()


@router.post("/documents")
async def upload_document(
    file: UploadFile = File(...),
    title: str = Form("Untitled"),  # Usar Form para que vaya en el body
    tags: str = Form(""),  # Usar Form para que vaya en el body
):
    # 1. Validar que sea PDF (opcional pero recomendado)
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    try:
        # 2. Leer el contenido binario
        content = await file.read()

        # 3. Extraer texto del PDF (No se puede hacer decode utf-8 directo)
        # Usamos io.BytesIO para tratar los bytes como un archivo en memoria
        pdf_reader = PdfReader(io.BytesIO(content))
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text() + "\n"

        # 4. Preparar metadatos
        metadata = {"title": title, "tags": tags, "filename": file.filename}

        # 5. Enviar al servicio (asumiendo que process_document acepta string)
        # Nota: Si process_document espera una ruta de archivo, la lógica cambia.
        # Aquí asumo que espera el TEXTO extraído.
        process_document(file.filename, text_content, metadata)

        logger.info(f"Documento {file.filename} procesado correctamente")
        return {"status": "success", "document": file.filename}

    except Exception as e:
        logger.error(f"Error procesando archivo: {e}")
        raise HTTPException(status_code=500, detail=str(e))
