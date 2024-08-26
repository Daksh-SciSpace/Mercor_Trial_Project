"""
OpenAI client module for the Interview Evaluation Application.

This module provides a client for interacting with the OpenAI API,
handling API calls with retry logic and error handling.
"""

import time
import logging
from typing import Dict

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential

# For 2 model types: Finetuned and the Normal one
model = 'ft:gpt-4o-2024-08-06:scispace:two-step-finetuning-final:A0WTYMJt:ckpt-step-430'
# model = 'gpt-4o-2024-08-06'

class OpenAIClient:
    """
    A class to manage interactions with the OpenAI API.
    """

    def __init__(self, api_key: str):
        """
        Initialize the OpenAIClient with an API key.

        Args:
            api_key (str): The OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(3))
    def call_api(self, system_content: str, user_content: str) -> Dict:
        """
        Call the OpenAI API with system and user roles, and return the response.

        This method uses exponential backoff for retries in case of API failures.

        Args:
            system_content (str): The content for the system role.
            user_content (str): The content for the user role.

        Returns:
            Dict: The parsed JSON response from the API.

        Raises:
            Exception: If the API call fails after retries.
        """
        response_format={'type': 'json_object'}
        if model != 'gpt-4o-2024-08-06':
            response_format = {"type": "text"}

        try:
            t1 = time.time()
            response = self.client.chat.completions.create(
                model=model, 
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_content}
                ],
                temperature=0,
                max_tokens=2000,
                response_format=response_format
            )
            t2 = time.time()
            logging.info(f"API call completed in {t2 - t1:.2f} seconds")
            
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            raise