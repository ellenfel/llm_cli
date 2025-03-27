import requests
from requests.exceptions import Timeout, RequestException
from typing import Dict, List, Optional
from src.config.settings import API_KEY, BASE_URL, TIMEOUT
from utils.helpers import format_request, parse_response, handle_api_error  # Fixed import names
from utils.exceptions import APITimeoutError, InvalidAPIKeyError, MalformedResponseError
import datetime as import_datetime
from exceptions import GeminiAPIError
import json

class GeminiAgent:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.conversation_history: List[Dict] = []
        self.max_retries = 3

    def generate_response(self, prompt: str, context: Optional[str] = None) -> Optional[str]:
        """Generate a response from the Gemini API based on the given prompt."""
        full_prompt = self._build_prompt(prompt, context)
        
        try:
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                json={"contents": [{"parts": [{"text": full_prompt}]}]},
                headers={'Content-Type': 'application/json'},
                timeout=TIMEOUT
            )

            # Check for specific error status codes
            if response.status_code == 401:
                raise InvalidAPIKeyError("Invalid API key. Please check your configuration.")
            elif response.status_code == 400:
                raise MalformedResponseError(f"Bad request: {response.json().get('error', {}).get('message', 'Unknown error')}")
            elif response.status_code != 200:
                raise GeminiAPIError(f"API request failed with status code: {response.status_code}")

            try:
                self.last_response = response.json()
                answer = self.last_response['candidates'][0]['content']['parts'][0]['text']
                self._update_history(prompt, answer)
                return answer
            except (KeyError, IndexError, json.JSONDecodeError) as e:
                raise MalformedResponseError(f"Failed to parse API response: {str(e)}")

        except Timeout:
            raise APITimeoutError(f"API request timed out after {TIMEOUT} seconds")
        except RequestException as e:
            raise GeminiAPIError(f"Request failed: {str(e)}")

    def _build_prompt(self, prompt: str, context: Optional[str] = None) -> str:
        """Build a context-aware prompt."""
        if context:
            return f"Context: {context}\nQuestion: {prompt}"
        return prompt

    def summarize(self, text: str) -> Optional[str]:
        """Summarize the given text."""
        return self.generate_response(f"Please summarize this text: {text}")

    def _update_history(self, prompt: str, response: str) -> None:
        """Update conversation history."""
        self.conversation_history.append({
            "prompt": prompt,
            "response": response,
            "timestamp": import_datetime.datetime.now().isoformat()
        })

    def get_conversation_history(self) -> List[Dict]:
        """Get the conversation history."""
        return self.conversation_history