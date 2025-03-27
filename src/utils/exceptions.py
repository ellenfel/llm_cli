class GeminiAPIError(Exception):
    """Base exception for Gemini API errors"""
    pass

class APITimeoutError(GeminiAPIError):
    """Raised when API request times out"""
    pass

class InvalidAPIKeyError(GeminiAPIError):
    """Raised when API key is invalid"""
    pass

class MalformedResponseError(GeminiAPIError):
    """Raised when API response is malformed"""
    pass