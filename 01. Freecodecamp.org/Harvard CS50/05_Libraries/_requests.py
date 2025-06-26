# pip.org/project/requests
# pip install requests
# docs.python.org/3/library/json.html

import json
import requests
import sys

# print(len(sys.argv))

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(f"https://itunes.apple.com/lookup?id={sys.argv[1]}&entity=song&limit=4")
# print(json.dumps(response.json(), indent=2))

o = response.json()
for i, result in enumerate(o["results"]):
    if "trackName" in result:
        print(f"{i + 1}. {result["trackName"]}")

