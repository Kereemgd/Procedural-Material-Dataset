import os
import json

# Define the input and output paths
input_folder = 'trial/u25-string-indexed-procedurals'
output_file = 'u25-string-indexed-procedurals.jsonl'

# Create a list to store the data
data = []

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read()
            # Generate instruction content by removing underscores and file extension
            instruction_content = os.path.splitext(filename)[0].replace('_', ' ')
            # Append the instruction as the user message and output as the assistant message
            data.append({
                "messages": [
                    {"role": "user", "content": instruction_content},
                    {"role": "assistant", "content": content}
                ]
            })

# Write the data to a JSONL file
with open(output_file, 'w', encoding='utf-8') as f:
    for entry in data:
        json_line = json.dumps(entry)
        f.write(json_line + '\n')

print(f"Data has been formatted and saved to {output_file}")