import json
import tiktoken
import matplotlib.pyplot as plt

# Initialize the tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

def count_tokens_in_jsonl(file_path):
    total_tokens = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            messages = data.get("messages", [])
            
            # Process each message in the list
            for message in messages:
                content = message.get("content", "")
                
                # Tokenize the content
                content_tokens = tokenizer.encode(content)
                
                # Count the tokens
                total_tokens += len(content_tokens)
    
    return total_tokens

# File paths
file_paths = [
    'mat-u10-procedurals.jsonl',
    'mat-u15-procedurals.jsonl',
]

# Count tokens for each file
token_counts = []
for file_path in file_paths:
    total_tokens = count_tokens_in_jsonl(file_path)
    token_counts.append(total_tokens)
    print(f"Total number of tokens before comment erasing in {file_path}: {total_tokens}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.bar(file_paths, token_counts, color=['blue', 'green', 'red'])
plt.xlabel('File')
plt.ylabel('Total Tokens')
plt.title('Token Counts before comment erasing in JSONL Files')
plt.show()

