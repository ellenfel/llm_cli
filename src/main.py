def main():
    import argparse
    import requests
    from config.settings import API_KEY, BASE_URL
    from utils.helpers import format_request, parse_response

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Gemini CLI for interacting with the Gemini API.')
    parser.add_argument('prompt', type=str, help='The prompt to send to the Gemini API for content generation.')
    args = parser.parse_args()

    # Prepare the API request
    request_data = format_request(args.prompt)

    # Make the API request
    response = requests.post(BASE_URL, json=request_data, headers={'Authorization': f'Bearer {API_KEY}'})

    # Check for a successful response
    if response.status_code == 200:
        # Parse and print the response
        output = parse_response(response.json())
        print(output)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()