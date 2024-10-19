import os
import re

def round_float(match):
    # Extract the matched number, round it to 3 decimal places, and convert to string
    rounded_number = f"{float(match.group()):.3f}"
    return rounded_number

def process_files_in_folder(folder_path):
    # Regular expression to match overly precise floating-point numbers
    float_pattern = re.compile(r'\d+\.\d{4,}')
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Substitute all overly precise floating-point numbers with their rounded version
            new_content = re.sub(float_pattern, round_float, content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

# Specify the folder path
folder_path = 'Finetune data\MatU10'

# Process the files in the folder
process_files_in_folder(folder_path)
