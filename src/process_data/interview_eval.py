"""
Interview Evaluator module for the Interview Evaluation Application.

This module contains the InterviewEvaluator class, which processes
interview data and manages the evaluation process using the OpenAI API.
"""

import logging
from typing import List, Dict

from src.csv_operation.csv_handler import CSVHandler
from src.client_based_services.openai_client import OpenAIClient
from src.client_based_services.claude_client import ClaudeClient

class InterviewEvaluator:
    """
    A class to evaluate interview responses using the OpenAI API.
    """

    def __init__(self, system_role: str, user_role: str, openai_client: OpenAIClient, claude_client: ClaudeClient):
        """
        Initialize the InterviewEvaluator.

        Args:
            client: Choose the  client to use
            system_role (str): The system role prompt for the OpenAI API.
            user_role (str): The user role prompt template for the OpenAI API.
            openai_client (OpenAIClient): An instance of the OpenAIClient.
            claude_client (ClaudeClient): An instance of the ClaudeClient.
        """
        self.client = 'openai' # can choose between 'claude' and 'openai'
        self.system_role = system_role
        self.user_role = user_role
        self.main_client = openai_client
        if self.client == 'claude':
            self.main_client = claude_client
        self.csv_handler = CSVHandler()

    def format_user_content(self, question: str, answer: str) -> str:
        """
        Format the user content for the OpenAI API.

        Args:
            question (str): The interviewer's question.
            answer (str): The interviewee's answer.

        Returns:
            str: The formatted user content.
        """
        return self.user_role.format(
            interviewer_question=question,
            interviewee_answer=answer
        )

    def process_csv(self, file_path: str) -> List[Dict]:
        """
        Process the CSV file and return a list of evaluation results.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            List[Dict]: A list of dictionaries containing questions, answers, and evaluations.
        """
        data = self.csv_handler.read_csv(file_path)
        results = []
        
        for row in data:

            try:
                question, answer = self.csv_handler.extract_qa(row['question_cand_answer'])
                user_content = self.format_user_content(question, answer)
                evaluation = self.main_client.call_api(self.system_role, user_content)
                
                results.append({
                    'question': question,
                    'answer': answer,
                    'evaluation': evaluation
                })
                logging.info(f"Processed question: {question[:50]}...")
            except Exception as e:
                logging.error(f"Error processing row: {e}")

        return results