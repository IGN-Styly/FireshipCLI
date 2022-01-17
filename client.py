import requests
import json
import crypt
import creds

a=requests.post(url="http://127.0.0.1:5000/send", data=creds.json_data)
print(a.content)