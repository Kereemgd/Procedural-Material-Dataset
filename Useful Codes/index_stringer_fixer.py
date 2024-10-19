import os
import bpy
import traceback

folder = "trial/u25-string-indexed"
log_file = "test_results-after-iterate.txt"

def execute_material_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    try:
        exec(code)
        return True
    except Exception as e:
        return traceback.format_exc()

def process_traceback(traceback_str):
    lines = traceback_str.split('\n')
    for line in lines:
        if "File" in line and "line" in line:
            parts = line.split(',')
            line_number = int(parts[1].strip().split(' ')[1])
            return line_number
    return None

def delete_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i != line_number - 1:
                file.write(line)

def log_process(file_path, message):
    with open(log_file, 'a') as log:
        log.write(f"{file_path}: {message}\n")

def main():
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            while True:
                result = execute_material_code(file_path)
                if result is True:
                    log_process(file_path, "Execution successful")
                    break
                else:
                    line_number = process_traceback(result)
                    if line_number is not None:
                        delete_line(file_path, line_number)
                        log_process(file_path, f"Deleted line {line_number} due to error: {result}")
                    else:
                        log_process(file_path, f"Unhandled error: {result}")
                        break

if __name__ == "__main__":
    main()

