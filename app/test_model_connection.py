import openai

client = openai.OpenAI(
    api_key="local",
    base_url="http://localhost:11434/v1"
)

response = client.chat.completions.create(
    model="qwen2.5:14b",
    messages=[{"role": "user", "content": "Hello World!"}]
)

print(response.choices[0].message.content)
