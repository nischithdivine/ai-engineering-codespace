from openai import OpenAI

client = OpenAI()

MODEL = "gpt-5.6-luna"

response = client.responses.create(
    model=MODEL,
    input="Reply with exactly: API connection successful",
)

print(response.output_text)