from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_json_text = response.json()
    print(parsed_json_text)

except JSONDecodeError:
    print("Response is not JSON format")
