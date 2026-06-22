from Sources.pdf_loader import load_pdf

text = load_pdf(
    "data/pdfs/sample.pdf"
)

print(text[:2000])