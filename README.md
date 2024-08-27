# MERCOR_TRIAL: Interview Evaluation Application

## Project Structure
```
MERCOR_TRIAL/
├── requirements/
│   └── requirements.txt
├── src/
│   ├── pycache/
│   ├── client_based_services/
│   │   ├── pycache/
│   │   ├── init.py
│   │   ├── claude_client.py
│   │   └── openai_client.py
│   ├── count_scores/
│   │   ├── pycache/
│   │   ├── init.py
│   │   └── count_score_occurrences.py
│   ├── csv_operation/
│   │   ├── pycache/
│   │   ├── init.py
│   │   └── csv_handler.py
│   ├── master_service/
│   │   ├── pycache/
│   │   ├── init.py
│   │   └── runner.py
│   ├── process_data/
│   │   ├── pycache/
│   │   ├── init.py
│   │   └── interview_eval.py
│   ├── prompts/
│   │   └── init.py
│   │   ├── system_role_prompt.py
│   │   └── user_role_prompt.py
│   └── init.py
├── .gitignore
└── Mercor trial final.ipynb
```
## Overview
This application automates the evaluation of technical interview responses using AI. It processes interview data, utilizes AI models (OpenAI and Claude) including finetuned ones for evaluation, and provides analysis of the results.

## Directory and File Descriptions

### requirements
- `requirements.txt`: Lists all Python dependencies required for the project.

### src
The main source code directory.

#### client_based_services
- `__init__.py`: Initializes the client_based_services package.
- `claude_client.py`: Manages interactions with the Claude AI service.
- `openai_client.py`: Manages interactions with the OpenAI API.

#### count_scores
- `__init__.py`: Initializes the count_scores package.
- `count_score_occurrences.py`: Handles counting and analyzing score occurrences from evaluations.

#### csv_operation
- `__init__.py`: Initializes the csv_operation package.
- `csv_handler.py`: Manages CSV file operations for input and output data.

#### master_service
- `__init__.py`: Initializes the master_service package.
- `runner.py`: Main script to orchestrate the entire evaluation process.

#### process_data
- `__init__.py`: Initializes the process_data package.
- `interview_eval.py`: Contains core logic for evaluating interview responses.

#### prompts
- `__init__.py`: Initializes the prompts package.
- `system_role_prompt.py`: Defines the system role prompt for AI models.
- `user_role_prompt.py`: Defines the user role prompt template for each evaluation.

### Mercor trial final.ipynb
A Jupyter notebook containing the data analysis, data formatting, and evaluation process. This notebook includes:
- Data loading and preprocessing
- Data formatting for fine-tuning process
- Evaluation of the fine-tuned model on test data
- Performance scores
- You can find the detailed explanation here: https://keen-savory-a61.notion.site/Data-Pre-Processing-for-Mercor-Trial-07eca47a9e9140dfac462a875967108c

## Setup and Installation
1. Clone the repository:
```
git clone https://github.com/Daksh-SciSpace/Mercor_Trial_Project.git
cd MERCOR_TRIAL
```
2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements/requirements.txt
```
## Usage
To run the application:
1. Ensure your interview data is properly formatted and accessible.
2. Configure API keys for OpenAI and Claude in os env.
3. Run the main script:
```
python -m src.master_service.runner
```
4. Check the output for evaluation results and score analysis (new .JSONL file will be created).
   
## Configuration
- Update API model type for OpenAI (finetuned or normal) in `src/client_based_services/openai_client.py`.
- Update the prompts type (finetuned or normal) in `src/master_service/runner.py`.
- You can change evaluating model (openai or claude) for testing in `src/process_data/interview_eval.py`.

##### Created by Daksk Raghuvanshi 

