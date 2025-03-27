import requests
import json
from typing import Dict, List, Optional
from config.settings import API_KEY, BASE_URL
from utils.helpers import format_request, parse_response, handle_api_error  # Fixed import names
import datetime as import_datetime

class GeminiAgent:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.conversation_history: List[Dict] = []
        self.max_retries = 3

    def generate_response(self, prompt: str, context: Optional[str] = None) -> Optional[str]:
        """Generate a response from the Gemini API based on the given prompt."""
        # Build context-aware prompt
        full_prompt = self._build_prompt(prompt, context)
        
        # Use existing send_request function
        response = requests.post(
            f"{self.base_url}?key={self.api_key}",
            json={"contents": [{"parts": [{"text": full_prompt}]}]},
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            self.last_response = response.json()  # Store the full response
            answer = self.last_response['candidates'][0]['content']['parts'][0]['text']
            self._update_history(prompt, answer)
            return answer
        else:
            handle_api_error(response)
            return None

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