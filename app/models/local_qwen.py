import os

from dotenv import load_dotenv
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY", None)
BASE_URL = os.getenv("OPENAI_API_BASE", None)

if not API_KEY:
    raise ValueError('Missing required environment key "API_KEY"')

if not BASE_URL:
    raise ValueError('Missing required environment key "BASE_URL"')

local_qwen = OpenAIModel(
    model_name="qwen2.5:14b",
    provider=OpenAIProvider(base_url=BASE_URL, api_key=API_KEY),
)
