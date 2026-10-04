import httpx
import os 



api_key = os.getenv("OPENAI_API_KEY")


url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content-type": "application/json"
}

body = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Explain transformers in one sentence."}
    ],
}

with httpx.Client(http2=True) as client:
    response =  client.post(url, headers=headers, json=body)


print(response.status_code)
print(response.json())

print(response.http_version)

print(response.extensions)




