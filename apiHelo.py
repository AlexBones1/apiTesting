import requests

payload = {"name": "Alison"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_json_text = response.json()
print(response.text, "\n", response.status_code, "\n", parsed_json_text["answer"])
