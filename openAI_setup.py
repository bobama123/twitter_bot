from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
   api_key = os.getenv("openai_api_key")
)


def generate_tweet():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a twitter bot."},
            {
                "role": "user",
                "content": "Write a random tweet about tech."
            }
        ]
    )

    return completion.choices[0].message.content

