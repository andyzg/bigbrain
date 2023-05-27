import os
import json
import sys
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


TOPIC = "music theory"
NUM_CONCEPTS = 30
prompt = """
Could you create a curriculum for {TOPIC} with {NUM_CONCEPTS} concepts
in JSON format. The key is the concept and the value is a
a list of prerequisite concepts as well as how complex the concept is. Each prerequisite concept
object should contain a name and a short description of how it's related to the original concept.
""".format(TOPIC=TOPIC, NUM_CONCEPTS=NUM_CONCEPTS)

print(prompt)
# sys.exit(0)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.1,
  max_tokens=3900,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response);

print(json.loads(response.choices[0].text))
