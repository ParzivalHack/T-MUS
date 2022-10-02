import requests
import urllib
import json
import time
import os
os.system("toilet T-MUS")
url = input("Insert URL to scan: ")
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/6iP3Ci09b83suqDijoQ4pHSD9uayadBp/"
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))
