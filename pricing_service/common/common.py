import requests


def get_content(url: str) -> str:
    response = requests.get(url)
    return response.content
