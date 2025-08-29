import requests
import json

url = "https://fullstack-api-bf0e.onrender.com/bfhl"
payload = {"data": ["a", "1", "334", "4", "R", "$"]}
headers = {"Content-Type": "application/json"}

try:
    print("Sending POST request to:", url)
    response = requests.post(url, json=payload, headers=headers)
    
    print("Status Code:", response.status_code)
    print("Response Headers:", dict(response.headers))
    
    # Check if response contains JSON
    if response.headers.get('Content-Type', '').startswith('application/json'):
        print("Response JSON:", response.json())
    else:
        print("Response Text:", response.text)
        
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except json.JSONDecodeError as e:
    print("JSON decode error:", e)
    print("Raw response:", response.text)
except Exception as e:
    print("Unexpected error:", e)