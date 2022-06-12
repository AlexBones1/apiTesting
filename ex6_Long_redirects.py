import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
requests_count = len(response.history)
final_url = response.url
print(requests_count, '\n', final_url)
