"""
Claude client module for the Interview Evaluation Application.

This module provides a client for interacting with the Cluade API,
handling API calls with retry logic and error handling.
"""

import time
import logging
from typing import Dict

import anthropic
from tenacity import retry, stop_after_attempt, wait_random_exponential

class ClaudeClient:
    """
    A class to manage interactions with the Claude API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the OpenAIClient with an API key.

        Args:
            api_key (str): The OpenAI API key.
        """
        self.client = anthropic.Anthropic(api_key=api_key)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(3))
    def call_api(self, system_content: str, user_content: str) -> Dict:
        """
        Call the Claude API with system and user roles, and return the response.

        This method uses exponential backoff for retries in case of API failures.

        Args:
            system_content (str): The content for the system role.
            user_content (str): The content for the user role.

        Returns:
            Dict: The parsed JSON response from the API.

        Raises:
            Exception: If the API call fails after retries.
        """
        try:
            t1 = time.time()
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=2000,
                temperature=0,
                system=system_content,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user_content
                            }
                        ]
                    }
                ]
            )
            t2 = time.time()
            logging.info(f"API call completed in {t2 - t1:.2f} seconds")
            return response.content[0].text
        except Exception as e:
            logging.error(f"Claude API error: {e}")
            raise