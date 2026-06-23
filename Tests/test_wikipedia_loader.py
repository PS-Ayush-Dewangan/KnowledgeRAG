from Sources.wikipedia_loader import load_wikipedia

text = load_wikipedia(
    "Ray Ban"
)

print(text[:2000])