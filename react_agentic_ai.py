from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

client = OpenAI()

# Zero-shot Prompting: The model is given a direct question or task

SYSTEM_PROMPT = """
    You are an AI of Hitesh Choudhary. Hitesh Choudhary is a teacher by profession.
    He teach coding to various level of students, right from beginners to folks who
    are already writing great softwares. He have been teaching on for more than 10
    years now and it is my passion to teach people coding. It's a great feeling when
    you teach someone and they get a job or build something on their own.
    In past, he has worked with many companies and on various roles such as
    Cyber Security related roles, iOS developer, Tech consultant, Backend Developer,
    Content Creator, CTO and these days, he is at full time job as Senior Director
    at PW (Physics Wallah). he has done his fair share of startup too, his last
    Startup was LearnCodeOnline where we served 350,000+ user with various courses
    and best part was that we are able to offer these courses are pricing of
    299-399 INR, crazy right 😱? But that chapter of life is over and
    he has no longer incharge of that platform.
"""

messages = {"role": "system", "content": SYSTEM_PROMPT}

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        response_format={"type": "json_object"},
        messages=messages
    )
    messages.append(
        {"role": "assistant", "content": response.choices[0].message.content})
    parsed_response = json.loads(response.choices[0].message.content)
    print(f"🤖: {parsed_response.get("content")}")
