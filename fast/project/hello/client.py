import requests

response1 =requests.get("http://localhost:8000")
response2 =requests.get("http://localhost:8000/items/10?q=hello")
res_json1 = response1.text
res_json2 = response2.json()
print(res_json1)
print()
print(res_json2)