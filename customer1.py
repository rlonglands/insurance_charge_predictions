import requests
url = "http://localhost:9696/predict"
cus1 = {
        "age":56,
        "sex":"male",
        "bmi":27,
        "children": 0,
        "smoker": "yes",
        "region": "southwest"}
print(requests.post(url, json=cus1).json())