import requests
url = "http://localhost:9696/predict"
cus3 = {
        "age":84,
        "sex":"female",
        "bmi":32,
        "children": 4,
        "smoker": "yes",
        "region": "southeast"}
print(requests.post(url, json=cus3).json())