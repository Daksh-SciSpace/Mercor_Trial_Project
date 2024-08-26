"""
Main script for the Interview Evaluation Application.

This script initializes and runs the application, handling the overall process
of evaluating interview responses using OpenAI's API.
"""

import json
import logging
import os
from typing import Dict

from src.process_data.interview_eval import InterviewEvaluator
from src.client_based_services.openai_client import OpenAIClient
from src.client_based_services.claude_client import ClaudeClient
from src.prompts.system_role_prompt import SYSTEM_ROLE, FINETUNED_SYSTEM_ROLE
from src.prompts.user_role_prompt import USER_ROLE, FINETUNED_USER_ROLE

class InterviewEvaluationApp:
    """
    A class to manage the interview evaluation application.
    """

    def __init__(self):
        """
        Initialize the InterviewEvaluationApp. Comment out the variable depending on the application for the testing 
        """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
        # Choose between available model or finetuned specific model 

        # self.system_role = SYSTEM_ROLE
        # self.user_role = USER_ROLE

        self.system_role = FINETUNED_SYSTEM_ROLE
        self.user_role = FINETUNED_USER_ROLE

        self.openai_client = self.initialize_openai_client()
        self.claude_client = self.initialize_claude_client()
        self.evaluator = InterviewEvaluator(self.system_role, self.user_role, self.openai_client, self.claude_client)

    @staticmethod
    def initialize_openai_client() -> OpenAIClient:
        """
        Initialize the OpenAI client.

        Returns:
            OpenAIClient: An instance of the OpenAIClient.

        Raises:
            ValueError: If the OPENAI_API_KEY is not set.
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set")
        return OpenAIClient(api_key)

    @staticmethod
    def initialize_claude_client() -> ClaudeClient:
        """
        Initialize the Claude client.

        Returns:
            ClaudeClient: An instance of the ClaudeClient.

        Raises:
            ValueError: If the CLAUDE_API_KEY is not set.
        """
        api_key = os.getenv('CLAUDE_API_KEY')
        if not api_key:
            raise ValueError("CLAUDE_API_KEY not set")
        return ClaudeClient(api_key)
    
    def process_csv(self, file_path: str) -> None:
        """
        Process the CSV file and save the evaluation results.

        Args:
            file_path (str): Path to the CSV file.
        """
        try:
            results = self.evaluator.process_csv(file_path)
            self.save_results(results)
        except Exception as e:
            logging.error(f"Error processing CSV: {e}")
            raise

    @staticmethod
    def save_results(results: Dict) -> None:
        """
        Save the evaluation results to a JSON file.

        Args:
            results (Dict): The evaluation results to save.
        """
        try:
            with open('evaluation_results.json', 'w') as f:
                json.dump(results, f, indent=2)
            logging.info("Results saved to evaluation_results.json")
        except IOError as e:
            logging.error(f"Error saving results: {e}")
            raise

    def run(self, csv_file_path: str) -> None:
        """
        Run the interview evaluation process.

        Args:
            csv_file_path (str): Path to the CSV file to process.
        """
        try:
            self.process_csv(csv_file_path)
        except Exception as e:
            logging.error(f"Error in main process: {e}")

def main():
    """
    Main function to run the interview evaluation application.
    """
    try:
        app = InterviewEvaluationApp()
        csv_file_path = 'csv_data_for_testing/balanced_testing.csv'  # Replace with your CSV file path
        app.run(csv_file_path)
    except Exception as e:
        logging.error(f"Application error: {e}")

if __name__ == "__main__":
    main()