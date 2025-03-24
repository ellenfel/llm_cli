def main():
    import argparse
    import requests
    from config.settings import API_KEY

    # Define the correct API endpoint
    BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Gemini CLI for interacting with the Gemini API.')
    parser.add_argument('--input', '-i', type=str, required=True, help='The input prompt to send to the Gemini API for content generation.')
    args = parser.parse_args()

    # Prepare the API request payload
    request_data = {
        "contents": [{
            "parts": [{"text": args.input}]
        }]
    }

    # Make the API request
    response = requests.post(
        f"{BASE_URL}?key={API_KEY}",
        json=request_data,
        headers={'Content-Type': 'application/json'}
    )

    # Check for a successful response
    if response.status_code == 200:
        # Parse and print the response
        response_json = response.json()
        print(response_json)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()