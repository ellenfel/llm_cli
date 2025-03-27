import argparse
import requests
import json
from config.settings import API_KEY
from utils.agent import GeminiAgent
from config.settings import BASE_URL

def send_request(prompt):
    """
    Send a request to the Gemini API with the given prompt.
    """
    request_data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    response = requests.post(
        f"{BASE_URL}?key={API_KEY}",
        json=request_data,
        headers={'Content-Type': 'application/json'}
    )
    return response

def log_token_usage(token_count, file_path="token_usage.txt"):
    """
    Log the total token count to a file.
    """
    with open(file_path, "a") as file:
        file.write(f"Total Token Count: {token_count}\n")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Gemini CLI for interacting with the Gemini API.')
    parser.add_argument('--input', '-i', type=str, required=True, 
                       help='The input prompt to send to the Gemini API for content generation.')
    parser.add_argument('--context', '-c', type=str,
                       help='Optional context for the prompt')
    parser.add_argument('--summarize', '-s', action='store_true',
                       help='Summarize the input text')
    args = parser.parse_args()

    # Initialize the GeminiAgent
    agent = GeminiAgent()

    try:
        if args.summarize:
            response = agent.summarize(args.input)
        else:
            response = agent.generate_response(args.input, args.context)

        if response:
            print(f"Response: {response}")
            history = agent.get_conversation_history()
            print(f"\nConversation history: {len(history)} interactions")
            
            # Get token count from the last API response
            if hasattr(agent, 'last_response') and agent.last_response:
                token_count = agent.last_response['usageMetadata']['totalTokenCount']
                log_token_usage(token_count)
                print(f"Tokens used in this interaction: {token_count}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()