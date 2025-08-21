# stay wrong, I don't understand

import requests

req = requests.post("localhost:8000/tryrequest/", data={"name": "klonggrok"})

print(req.text)