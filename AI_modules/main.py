import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Usage: python3 main.py \"your question here\" [--verbose]")
    sys.exit(1)

user_prompt = sys.argv[1]

# Check for verbose flag (should be after the prompt)
verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

messages = [
    types.Content(
        role="user",
        parts=[
            types.Part(
                text=user_prompt
            )
        ]
    )
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
    # f"""
    # You are a helpful assistant that can answer questions and help with tasks.
    # You are given a question and you need to answer it.
    # You are also given a list of tools that you can use to answer the question.
    # You need to use the tools to answer the question.   

    # Question: {user_prompt}
    # """
)


if verbose:
    print(f"User prompt: {user_prompt}")

print(response.text)

if verbose:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")









