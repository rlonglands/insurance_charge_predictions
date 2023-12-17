import requests
url = "http://localhost:9696/predict"
cus2 = {
        "age":24,
        "sex":"male",
        "bmi":22,
        "children": 1,
        "smoker": "no",
        "region": "northwest"}
print(requests.post(url, json=cus2).json())