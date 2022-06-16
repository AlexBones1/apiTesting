import requests

http_methods = [requests.get, requests.post, requests.put, requests.delete]
api_params = ["GET", "POST", "PUT", "DELETE"]

# HTTP request without any method in parameters
response_first = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"First answer - {response_first.text}, \n Status code is {response_first.status_code}")
print('-'*22)

# HTTP request with method, which is not in the list
response_second = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Second answer - {response_second.text}, \n Status code is {response_second.status_code}")
print('-'*22)

# HTTP request with valid method
payload = {"method": "POST"}
response_third = http_methods[1]("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(f"Third answer - {response_third.text}, \n Status code is {response_third.status_code}")
print('-'*22)

# Find a bug (success with DELETE and 'GET' from api-method)
s = ''
for i in range(0, len(http_methods)):
    for j in range(0, len(api_params)):
        if i == 0:
            response = http_methods[i]("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": f"{api_params[j]}"})
            if ('success' in response.text):
                s += f"\n Response body - {response.text}, http - {http_methods[i]}, payload - {api_params[j]}"
        else:
            response = http_methods[i]("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{api_params[j]}"})
            if ('success' in response.text):
                s += f"\n Response body - {response.text}, http - {http_methods[i]}, payload - {api_params[j]}"
print(s)









