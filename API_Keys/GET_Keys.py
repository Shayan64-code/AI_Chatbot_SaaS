import requests

# Get current API key (GET /key)
response = requests.get(
  "https://openrouter.ai/api/v1/key",
  headers={
    "Authorization": "Bearer "
  },
)
print(response.json())