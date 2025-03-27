import unittest
from unittest.mock import patch
from requests.exceptions import Timeout
from src.utils.agent import GeminiAgent
from src.utils.exceptions import (
    APITimeoutError,
    InvalidAPIKeyError,
    MalformedResponseError
)

class TestGeminiAgent(unittest.TestCase):
    def setUp(self):
        self.agent = GeminiAgent()

    @patch('requests.post')
    def test_timeout_handling(self, mock_post):
        mock_post.side_effect = Timeout()
        with self.assertRaises(APITimeoutError):
            self.agent.generate_response("test prompt")

    @patch('requests.post')
    def test_invalid_api_key(self, mock_post):
        mock_post.return_value.status_code = 401
        with self.assertRaises(InvalidAPIKeyError):
            self.agent.generate_response("test prompt")

    @patch('requests.post')
    def test_malformed_response(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"invalid": "response"}
        with self.assertRaises(MalformedResponseError):
            self.agent.generate_response("test prompt")