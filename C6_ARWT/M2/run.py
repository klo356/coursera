#! /usr/bin/env python3

import os
import requests

# This script reads feedback from text files in the /data/feedback directory,
# parses the content, and posts it to a specified URL.

# Function to parse feedback from a text file
def parse_feedback(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')

    if len(lines) < 4:
        raise ValueError("File must contain at least 4 lines: title, name, date, and feedback.")

    return {
        'title': lines[0].strip(),
        'name': lines[1].strip(),
        'date': lines[2].strip(),
        'feedback': ' '.join(line.strip() for line in lines[3:]).strip()
    }


# Get a list of all .txt files under /data/feedback directory (including subdirectories)
txt_files = []
feedback_directory = '/data/feedback'

for root, dirs, files in os.walk(feedback_directory):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(os.path.join(root, file))
#print(txt_files)


# Example usage
# ['/data/feedback/020.txt', '/data/feedback/001.txt', '/data/feedback/007.txt', '/data/feedback/019.txt', '/data/feedback/005.txt']
#file_path = 'feedback.txt'  # Path to your text file
#feedback_dict = parse_feedback(file_path)
#print(feedback_dict)

url = "http://35.230.21.130/feedback/"

for file_path in txt_files:
    feedback_dict = parse_feedback(file_path)
    response = requests.post(url, json=feedback_dict)
    
    # Check if the response is successful
    if response.status_code != 201:
        print(f"Error posting {file_path}: {response.status_code} - {response.text}")
    else:
        print(f"Success posting {file_path}: {response.status_code}")