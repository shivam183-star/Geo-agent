import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_tweet(title, summary):

    prompt = f"""
You are a professional geopolitics news account on Twitter/X.

Your task:
- Write ONE concise tweet
- Sound professional and neutral
- No clickbait
- No propaganda
- No emojis
- Max 280 characters
- Make it informative and engaging

News Title:
{title}

News Summary:
{summary}

Output ONLY the tweet text.
"""

    try:

        response = model.generate_content(prompt)

        tweet = response.text.strip()

        return tweet

    except Exception as e:

        print(f"Gemini Error: {e}")

        return None