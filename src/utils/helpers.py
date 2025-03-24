import requests

def format_request(prompt):
    """
    Format the API request payload for the Gemini API.
    """
    return {"prompt": prompt}

def parse_response(response_json):
    """
    Parse the response from the Gemini API and extract the output.
    """
    try:
        if "error" in response_json:
            raise ValueError(f"API Error: {response_json['error']}")
        return response_json.get("output", "No output found.")
    except ValueError as e:
        print(f"Error parsing response: {e}")
        return None

def handle_api_error(response):
    """
    Handle API errors gracefully by printing the error details.
    """
    print(f"API Error: {response.status_code} - {response.text}")

def validate_api_key(api_key):
    """
    Validate the API key format.
    """
    if not api_key or len(api_key) != 32:  # Example length check
        raise ValueError("Invalid API key. Please check your key.")