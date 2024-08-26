import csv
import logging
from typing import List, Dict, Tuple

class CSVHandler:
    """
    A class to handle CSV file operations.
    """

    @staticmethod
    def read_csv(file_path: str) -> List[Dict]:
        """
        Read the CSV file and return a list of dictionaries.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            List[Dict]: A list of dictionaries, each representing a row in the CSV.
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            logging.error(f"CSV file not found: {file_path}")
            raise
        except csv.Error as e:
            logging.error(f"Error reading CSV file: {e}")
            raise

    @staticmethod
    def extract_qa(text: str) -> Tuple[str, str]:
        """
        Extract interviewer's question and interviewee's answer from the text.

        Args:
            text (str): The combined question and answer text.

        Returns:
            Tuple[str, str]: A tuple containing the question and answer.

        Raises:
            ValueError: If the text format is unexpected.
        """
        parts = text.split("\n\n")
        if len(parts) != 2:
            raise ValueError("Unexpected format in question_cand_answer")
        
        question = parts[0].replace("Interviewer: ", "").strip()
        answer = parts[1].replace("Interviewee: ", "").strip()
        return question, answer