import requests
import time

# Create a new task
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()["token"]
req_time = response.json()["seconds"]

# Send request before job will done
first_response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
assert 'NOT ready' in first_response.json()["status"]

# Send request after work complete
time.sleep(req_time + 0.5)
second_response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
assert ('Job is ready' in second_response.json()["status"]) and ('result' in second_response.json())
print(second_response.text, token, req_time)
