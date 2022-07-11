import requests
import json

with open("macro.json", "r") as file:
    r = json.load(file)

print(r)

local_host = "http://localhost:8080/api/v1/macro/update"
r = requests.post(local_host, json=r)
