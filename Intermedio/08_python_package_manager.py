## Use pip install
## example: pip install pandas

import requests

reponse = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(reponse)
print(reponse.status_code)
print(reponse.json())