from Sources.wikipedia_loader import load_wikipedia

text = load_wikipedia(
    "Artificial intelligence"
)

if text:
    print(text[:2000])