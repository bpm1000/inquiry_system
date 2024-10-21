import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from config.config import MYGPTS_API_URL, MYGPTS_API_KEY

def get_gpt_response(question):
    try:
        headers = {
            'Authorization': f'Bearer {MYGPTS_API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'gpt-4o-mini',
            'messages': [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            'max_tokens': 150
        }
        print("Sending request to OpenAI API...")
        print("Headers:", headers)
        print("Data:", json.dumps(data, indent=2))

        response = requests.post(MYGPTS_API_URL, headers=headers, json=data)
        response.raise_for_status()  # HTTPエラーをチェック

        print("Response:", response.json())

        return response.json().get('choices')[0].get('message').get('content').strip()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return f"Error: {e}"
