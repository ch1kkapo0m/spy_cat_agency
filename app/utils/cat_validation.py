import requests

def is_valid_breed(breed: str) -> bool:
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    if response.status_code == 200:
        breeds = [b['name'].lower() for b in response.json()]
        return breed.lower() in breeds
    return False
