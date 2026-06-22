import requests
from bs4 import BeautifulSoup


def load_website(url):

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Remove unwanted tags
    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header"
    ]):
        tag.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return text