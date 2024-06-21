#program to find automatically bitcoin rate

import requests

from pprint import pprint

url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(url.json())