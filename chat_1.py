from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero-shot Prompting: The model is given a direct question or task

SYSTEM_PROMPT = """
    You are an AI expert in Coding. You know any programming language.
    You help users in solving there programming doubts only and nothing else.
    If user tried to ask something else apart from programming you can just roast them.
"""

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, My name is Debaprasad"},
        {"role": "assistant",
            "content": "Hey Debaprasad! How can I help you with your Python code today?"},
        {"role": "user", "content": "can you write a python code for to sum two numbers?"},
        {"role": "assistant",
            "content": "Sure! Here's a simple Python code to sum two numbers:\n\n```python\n# Function to sum two numbers\ndef sum_two_numbers(a, b):\n    return a + b\n\n# Example usage\nnum1 = 5\nnum2 = 10\nresult = sum_two_numbers(num1, num2)\nprint(f'The sum of {num1} and {num2} is {result}')\n```"},
        {"role": "user", "content": "how to do the same in java script?"},
    ]
)

print(response.choices[0].message.content)
