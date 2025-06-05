import os

import openai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY", None)
BASE_URL = os.getenv("OPENAI_API_BASE", None)

if not API_KEY:
    raise ValueError('Missing required environment key "API_KEY"')

if not BASE_URL:
    raise ValueError('Missing required environment key "BASE_URL"')

client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

response = client.chat.completions.create(
    model="qwen2.5:14b", messages=[{"role": "user", "content": "Hello World!"}]
)

model_reponse = response.choices[0].message.content

if not model_reponse:
    raise Exception("\nCONNECTION FAILED!")
else:
    print("\nCONNECTION SUCCEEDED!")

# print(response.choices[0].message.content)
