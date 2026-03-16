"""
API Helper Utilities
=====================
Common utilities for making safe API calls with error handling,
timeouts, and retry logic. Used across all weeks.
"""

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


def safe_api_call(url: str, method: str = "GET", timeout: int = 10, **kwargs) -> dict:
    """Make a safe API call with timeout and error handling.

    Args:
        url: The API endpoint URL
        method: HTTP method (GET, POST, PUT, DELETE)
        timeout: Request timeout in seconds
        **kwargs: Additional arguments passed to requests

    Returns:
        Parsed JSON response as a dictionary

    Raises:
        ValueError: If the request fails
    """
    try:
        response = requests.request(method, url, timeout=timeout, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise ValueError(f"Request timed out after {timeout}s: {url}")
    except requests.exceptions.HTTPError as e:
        raise ValueError(f"HTTP error {response.status_code}: {e}")
    except requests.exceptions.ConnectionError:
        raise ValueError(f"Connection failed: {url}")
    except requests.exceptions.JSONDecodeError:
        raise ValueError(f"Invalid JSON response from: {url}")


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    retry=retry_if_exception_type((requests.exceptions.Timeout, requests.exceptions.ConnectionError)),
)
def retry_with_backoff(url: str, method: str = "GET", **kwargs) -> dict:
    """Make an API call with automatic retry and exponential backoff.

    Retries up to 3 times with exponential wait (2s, 4s, 8s) on
    timeout or connection errors.

    Args:
        url: The API endpoint URL
        method: HTTP method
        **kwargs: Additional arguments passed to requests

    Returns:
        Parsed JSON response
    """
    return safe_api_call(url, method, **kwargs)
