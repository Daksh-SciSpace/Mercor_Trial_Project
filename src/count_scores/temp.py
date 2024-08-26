# Count the unique score in the json file in wich the element looks like this 
# [
#   {
#     "question": "Great! I see from your resume that you've had a significant role in the AI society and IEEE at USICT. Can you tell me about a specific project or event where you applied your AI skills to make a notable contribution?",
#     "answer": "Yes. So, basically, we worked in a project where we have to, uh, make an object detection model, and you run that on a Jetson Nano. And that was for the event that was happening in Delhi. And, uh, we made an object detection model using, uh, Yolo v 3. It's a darknet based backbone, and we use it. We optimized it. We fine tuned it on the dataset for our treasure hunt. So, basically, we have a we have data for QR codes, and we have to label them. And then we have to train the model on uh, YOLO v 5 uh, v 3 model, sorry, on those dataset. And we got an accuracy of above 90%, and we evaluated that, uh, and the evaluation accuracy was also near 91%. And we used the model in run time, and we deploy optimized it. And then we quantized it on a 4 bit, And we put that on Zetson Nano, and we, uh, showed that in an event where people were using or doing the Treasure Hut. Uh, so that was the main, uh, project that I did in I triple e.",
#     "evaluation": "{\"expertise\": { \"score\": 4, \"justification\": \"The candidate demonstrates a strong understanding of AI and object detection technologies, specifically mentioning the use of YOLO v3 for object detection and deployment on a Jetson Nano. They accurately describe the process of fine-tuning the model on a dataset, achieving high accuracy, and optimizing the model for deployment. The response showcases a good level of technical detail, including model quantization and deployment on hardware, which indicates a solid grasp of both software and hardware aspects of AI projects. However, the explanation could benefit from more detail on the specific challenges faced and how they were overcome, as well as a deeper discussion of the methodologies used.\", \"thought_process\": \"1. Identified key technologies: YOLO v3, Jetson Nano, object detection, model quantization. 2. Assessed accuracy: Technical terms are used correctly, and the process described is coherent and accurate. 3. Evaluated depth: The candidate provides a detailed overview of the project, including model training, optimization, and deployment, but lacks discussion of specific challenges or advanced techniques. 4. Considered examples: The example of deploying an object detection model for a treasure hunt event is relevant and well-explained. 5. Technicality level: Appropriate for the context, with a good balance of technical detail and practical application.\" }}"
#   },...
# ]  

import json
from collections import Counter

def count_score_occurrences(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    scores = []
    for item in data:
        evaluation = json.loads(item['evaluation'])
        scores.append(evaluation['expertise']['score'])

    score_counts = Counter(scores)
    return dict(score_counts), len(score_counts)

# Usage
json_file = 'evaluation_results.json'
score_occurrences, unique_count = count_score_occurrences(json_file)
print("Score Occurrences:", score_occurrences)
print("Number of Unique Scores:", unique_count)