import unittest
from unittest.mock import patch, mock_open
from src.main import send_request, log_token_usage

class TestMainFunctions(unittest.TestCase):

    @patch("src.main.requests.post")
    def test_send_request(self, mock_post):
        # Mock the API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "candidates": [{"content": {"parts": [{"text": "Test response"}]}}],
            "usageMetadata": {"totalTokenCount": 123}
        }

        response = send_request("Test prompt")
        self.assertEqual(response.status_code, 200)
        self.assertIn("candidates", response.json())

    @patch("builtins.open", new_callable=mock_open)
    def test_log_token_usage(self, mock_file):
        log_token_usage(123, "test_token_usage.txt")
        mock_file.assert_called_once_with("test_token_usage.txt", "a")
        mock_file().write.assert_called_once_with("Total Token Count: 123\n")

if __name__ == "__main__":
    unittest.main()