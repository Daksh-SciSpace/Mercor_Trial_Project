USER_ROLE = """
You will now be presented with an interview question and answer. Please evaluate it using the rubric and process described above. Remember to use the full range of scores from 1 to 5, and avoid clustering around middle values.

Interviewer: {interviewer_question}
Interviewee: {interviewee_answer}

Provide your evaluation in the specified JSON format, including the score, justification, and thought process. Ensure your scoring is consistent with the rubric and examples provided.
Do not give anything out of the JSON. No explantion or any text is required out of the JSON.
"""

FINETUNED_USER_ROLE = """Evaluate the following interview response for technical expertise:

Interviewer: {interviewer_question}
Interviewee: {interviewee_answer}
"""