from Sources.pdf_loader import load_pdf

from Chunking.chunk_utils import create_chunks

from VectorDB.pinecone_store import (
    create_pinecone_store
)

pdf_path = "Data/pdfs/sample.pdf"

text = load_pdf(
    pdf_path
)

chunks = create_chunks(
    text
)

print(
    f"Chunks Created: {len(chunks)}"
)

create_pinecone_store(
    chunks,
    source="PDF",
    document=pdf_path
)

print(
    "PDF stored in Pinecone successfully"
)