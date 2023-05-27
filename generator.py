import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="What are 5 key points I should know when studying Ancient Rome?",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
