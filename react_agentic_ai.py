from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

client = OpenAI()

# Zero-shot Prompting: The model is given a direct question or task

SYSTEM_PROMPT = """
    

     Rules:
    1. Follow the strict JSON output as per schema.
    2. Always perform one step at a time and wait for the next input.
    3. Carefully analyse the user query,

    Output Format:
    {{ "content": "string" }}

  Example:



"""

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        response_format={"type": "json_object"},
        messages=messages
    )

    messages.append(
        {"role": "assistant", "content": response.choices[0].message.content})
    parsed_response = json.loads(response.choices[0].message.content)

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    print("AI: ", parsed_response.get("content"))
    continue
