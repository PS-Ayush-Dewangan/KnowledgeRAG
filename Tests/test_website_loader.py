from Sources.website_loader import load_website

text = load_website(
    "https://fastapi.tiangolo.com/"
)

print(text[:2000])