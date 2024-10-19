import os
import shutil

def copy_files_with_shader_node_tree(source_directory, destination_directory):
    copied_count = 0
    skipped_count = 0
    
    # Create destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.txt'):  # Check only text files
                source_path = os.path.join(root, file)
                
                try:
                    # Open the file and check for "ShaderNodeTree"
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'ShaderNodeTree' in content:
                            # Copy the file if it contains "ShaderNodeTree"
                            relative_path = os.path.relpath(source_path, source_directory)
                            destination_path = os.path.join(destination_directory, relative_path)
                            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                            shutil.copy2(source_path, destination_path)
                            copied_count += 1
                            print(f"Copied: {source_path} -> {destination_path}")
                        else:
                            skipped_count += 1
                except Exception as e:
                    print(f"Could not process: {source_path}. Error: {str(e)}")
                    skipped_count += 1
    
    return copied_count, skipped_count

def main():
    source_directory = r'trial\u25-string-indexed'  # Replace with your source directory path
    destination_directory = r'trial\u25-string-indexed-procedurals'  # Replace with your destination directory path
    copied_files, skipped_files = copy_files_with_shader_node_tree(source_directory, destination_directory)
    print(f"Number of files copied: {copied_files}")
    print(f"Number of files skipped: {skipped_files}")

if __name__ == "__main__":
    main()
