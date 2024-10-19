import os
import matplotlib.pyplot as plt

def count_files_with_shader_node_tree_and_plot_distribution(directory):
    count = 0
    file_sizes = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # Check only text files
                file_path = os.path.join(root, file)

                # Open the file and check for "ShaderNodeTree"
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'ShaderNodeTree' in content:
                        count += 1
                        file_size = os.path.getsize(file_path)
                        file_sizes.append(file_size)

    # Plotting the file size distribution
    file_sizes_kb = [size / 1024 for size in file_sizes]  # Convert to KB
    bins = range(0, int(max(file_sizes_kb)) + 5, 5)  # 5KB steps
    plt.hist(file_sizes_kb, bins=bins, edgecolor='black')
    plt.title('File Size Distribution of Files Containing "ShaderNodeTree"')
    plt.xlabel('File Size (KB)')
    plt.ylabel('Number of Files')
    plt.show()

    return count

def main():
    directory = r'trial\AllMaterialDescriptionsCommentDimensionErased3rdOptimize'  # Replace with your directory path
    result = count_files_with_shader_node_tree_and_plot_distribution(directory)
    print(f"Number of files containing 'ShaderNodeTree': {result}")

if __name__ == "__main__":
    main()
