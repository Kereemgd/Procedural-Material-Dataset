import bpy
import os

def execute_material_code(material, code, text_file, log_file):
    try:
        # Execute the code in a local context with access to the material's node tree
        exec(code, {'bpy': bpy, 'material': material, 'mat': material})
        log_file.write(f"{text_file} executed successfully.\n")
    except Exception as e:
        # Catch and log any errors
        log_file.write(f"Error in {text_file}: {e}\n")

def test_material_scripts(folder_path, log_file_path):
    # Create a new material to test the scripts
    test_mat = bpy.data.materials.new(name="Test_Material")
    test_mat.use_nodes = True

    # Open the log file for writing
    with open(log_file_path, 'w') as log_file:
        # Ensure we are accessing the correct folder
        if not os.path.exists(folder_path):
            log_file.write(f"Error: The folder path '{folder_path}' does not exist.\n")
            return
        
        # Get all text files in the folder
        try:
            text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        except Exception as e:
            log_file.write(f"Error accessing files in folder '{folder_path}': {e}\n")
            return
        
        if not text_files:
            log_file.write(f"No .txt files found in the folder '{folder_path}'.\n")
            return

        # Process each file individually to prevent memory overload
        for text_file in text_files:
            file_path = os.path.join(folder_path, text_file)
            print(f"Accessing file: {file_path}")  # This will confirm that files are being accessed
            
            try:
                # Read the contents of the text file
                with open(file_path, 'r') as file:
                    code = file.read()
                
                log_file.write(f"Testing {text_file}...\n")
                
                # Execute the code with error handling
                execute_material_code(test_mat.node_tree, code, text_file, log_file)
                
                # Free up memory by clearing nodes in the material after each test
                for node in test_mat.node_tree.nodes:
                    test_mat.node_tree.nodes.remove(node)
                
            except Exception as e:
                log_file.write(f"Error processing {text_file}: {e}\n")
                continue

def delete_files_with_errors(log_file_path, folder_path):
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
    
    for line in lines:
        if "Error in" in line:
            # Extract the file name from the error log
            error_file = line.split("Error in ")[1].split(":")[0]
            file_path = os.path.join(folder_path, error_file)
            try:
                os.remove(file_path)
                print(f"Deleted {error_file} due to errors.")
            except Exception as e:
                print(f"Failed to delete {error_file}: {e}")

# Replace 'your_folder_path' with the path to your folder containing the .txt files
folder_path = 'Finetune data/3.4k_mat_txt_preprocess'

# Path to the log file where results will be written
log_file_path = 'test_results.txt'

# First, test the material scripts and log the results
test_material_scripts(folder_path, log_file_path)

# Then, delete the files that had errors
#delete_files_with_errors(log_file_path, folder_path)