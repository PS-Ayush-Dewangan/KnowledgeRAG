from Sources.pdf_loader import load_pdf
from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store


pdf_path = "data/pdfs/sample.pdf"

text = load_pdf(pdf_path)

chunks = create_chunks(text)

print(f"Chunks Created: {len(chunks)}")

create_vector_store(chunks)

print("PDF stored in FAISS successfully")