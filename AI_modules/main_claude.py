import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.environ.get("CLAUDE_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

# Initialize conversation history
messages = []

print("Claude AI Assistant - Type 'quit' to exit")
print("-" * 40)

while True:
    # Get user input
    user_input = input("\nYou: ").strip()
    
    # Check if user wants to quit
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye!")
        break
    
    if not user_input:
        continue
    
    # Add user message to conversation history
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Send to Claude
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system="You are a professional, well knowledged assistant with a friendly and calm tone. Please respond to questions in a concise but very accurate manner.",
        messages=messages
    )
    
    # Get Claude's response
    claude_response = response.content[0].text
    
    # Add Claude's response to conversation history
    messages.append({
        "role": "assistant", 
        "content": claude_response
    })
    
    # Display response
    print(f"\nClaude: {claude_response}")
    print(f"\nTokens - Input: {response.usage.input_tokens}, Output: {response.usage.output_tokens}")