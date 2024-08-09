import requests

params = {
    "shouji": "15618919442",
    "appkey": "0c818521d38759e1"
}

r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query?shouji=15618919442&appkey=0c818521d38759e1", params=params)

print(r.status_code)
print(r.json())
