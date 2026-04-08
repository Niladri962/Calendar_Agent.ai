# config.py
import requests

API_KEY = "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"

url = "https://openrouter.ai/api/v1/models"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    print("Available Models:\n")
    for model in data['data']:
        print(model['id'])
else:
    print("Error:", response.text)

