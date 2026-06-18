from Chunking.chunk_utils import create_chunks

with open("data/sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = create_chunks(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print(chunk)