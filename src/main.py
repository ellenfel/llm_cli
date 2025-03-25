import argparse
import requests
import json
from config.settings import API_KEY

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

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
    parser.add_argument('--input', '-i', type=str, required=True, help='The input prompt to send to the Gemini API for content generation.')
    args = parser.parse_args()

    # Make the API request
    response = send_request(args.input)

    # Check for a successful response
    if response.status_code == 200:
        # Parse the response
        response_json = response.json()
        answer = response_json['candidates'][0]['content']['parts'][0]['text']
        total_token_count = response_json['usageMetadata']['totalTokenCount']

        # Print the answer
        print(f"Answer: {answer.strip()}")

        # Log the token usage
        log_token_usage(total_token_count)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()