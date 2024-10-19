import os
import re
import json

# Folder paths
input_folder_path = 'trial/AllMaterialDescriptionsCommentDimensionErased3rdOptimize - Kopya'
str_text_files_folder = 'str_text_files'
output_folder_path = 'trial/u25-string-indexed'
# Node types to process
shader_nodes = ["ShaderNodeValToRGB", "ShaderNodeTexNoise", "ShaderNodeCombineXYZ",
                "ShaderNodeSeparateXYZ", "ShaderNodeBump", "ShaderNodeTexCoord", "ShaderNodeOutputMaterial", 
                "ShaderNodeMapping", "ShaderNodeBsdfPrincipled", "ShaderNodeMixShader", 
                "ShaderNodeTexVoronoi", "ShaderNodeVectorMath", "ShaderNodeRGB", "ShaderNodeLayerWeight", 
                "ShaderNodeTexChecker", "ShaderNodeBsdfAnisotropic", "ShaderNodeNewGeometry", "ShaderNodeRGBCurve", 
                "ShaderNodeHueSaturation", "ShaderNodeTexWave", "ShaderNodeFresnel", "ShaderNodeDisplacement", 
                "ShaderNodeVectorRotate", "ShaderNodeInvert", "ShaderNodeValue", "ShaderNodeBrightContrast", 
                "ShaderNodeClamp", "ShaderNodeBsdfGlass", "ShaderNodeBsdfTransparent", "ShaderNodeAddShader", 
                "ShaderNodeLightPath", "ShaderNodeBsdfDiffuse", "ShaderNodeTexGradient", "ShaderNodeRGBToBW", 
                "ShaderNodeEmission", "ShaderNodeSeparateColor", "ShaderNodeTexBrick", "ShaderNodeGamma", 
                "ShaderNodeTexWhiteNoise", "ShaderNodeAmbientOcclusion", "ShaderNodeShaderToRGB", "ShaderNodeNormalMap", 
                "ShaderNodeMixRGB", "ShaderNodeTexMagic", "ShaderNodeCombineColor", "ShaderNodeBevel", 
                "ShaderNodeObjectInfo", "ShaderNodeBsdfTranslucent", "ShaderNodeBsdfRefraction", "ShaderNodeFloatCurve", 
                "ShaderNodeVolumeAbsorption", "ShaderNodeVolumePrincipled", "ShaderNodeTangent", "ShaderNodeUVMap", 
                "ShaderNodeSubsurfaceScattering", "ShaderNodeAttribute", "ShaderNodeVolumeScatter", "ShaderNodeWireframe", 
                "ShaderNodeTexImage", "ShaderNodeBsdfHair", "ShaderNodeBsdfSheen", "ShaderNodeNormal"]

# Regex patterns
node_pattern = re.compile(r'(\w+)\s*=\s*\w+\.nodes.new\("(\w+)"\)')
attribute_pattern = re.compile(r'(\w+)\.(inputs|outputs)\[(\d+)\]')

def load_input_output_map(node_type):
    filename = f"{node_type}.txt"
    file_path = os.path.join(str_text_files_folder, filename)
    
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        start_index = content.find('{')
        if start_index == -1:
            print(f"Input/Output map not found in file: {file_path}")
            return {}
        map_str = content[start_index:]
        try:
            input_output_map = json.loads(map_str.replace("'", '"'))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file: {file_path}, Error: {e}")
            return {}
    
    print(f"Loaded map for {node_type}: {input_output_map}")
    return input_output_map

def replace_inputs_outputs(content, node_type, input_output_map, nodes):
    def replace_match(match):
        variable, attr_type, index = match.groups()
        index = int(index)
        
        # Print debug information
        print(f"Checking: {variable}.{attr_type}[{index}]")
        print(f"Node type: {node_type}")
        print(f"Available nodes: {nodes}")
        
        if variable in [node[0] for node in nodes if node[1] == node_type]:
            if attr_type in input_output_map and str(index) in input_output_map[attr_type]:
                replacement = f"{variable}.{attr_type}[\"{input_output_map[attr_type][str(index)]}\"]"
                print(f"Replacing: {match.group(0)} with {replacement}")
                return replacement
            else:
                print(f"No replacement found for {attr_type}[{index}]")
        else:
            print(f"Variable {variable} not found in nodes of type {node_type}")
        return match.group(0)
    
    new_content = attribute_pattern.sub(replace_match, content)
    if new_content != content:
        print(f"Updated content for node type {node_type}.")
        # Print a few lines of the updated content for verification
        print("Sample of updated content:")
        print("\n".join(new_content.split("\n")[:5]))
    else:
        print(f"No changes made for node type {node_type}.")
    return new_content
# Iterate through all the text files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find all nodes and check if their types match the shader_nodes list
        nodes = node_pattern.findall(content)
        node_types = {node_type for _, node_type in nodes if node_type in shader_nodes}
        
        print(f"Processing file: {filename}")
        print(f"Found node types: {node_types}")

        # Process only for specified node types
        if node_types:
            for node_type in node_types:
                input_output_map = load_input_output_map(node_type)
                if input_output_map:
                    content = replace_inputs_outputs(content, node_type, input_output_map, nodes)

            # Write the updated content to a new file
            output_filename = f"{os.path.splitext(filename)[0]}.txt"
            output_file_path = os.path.join(output_folder_path, output_filename)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(content)
            print(f"Processed {filename} and updated inputs/outputs with mapped names.")
        else:
            print(f"No relevant shader nodes found in {filename}. Skipping.")

folder_path = input_folder_path

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Filter out lines containing .inputs["Weight"].default_value = 0.0
        new_lines = [line for line in lines if '.inputs["Weight"].default_value = 0.0' not in line]
        
        # Write the filtered content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

print("Lines removed successfully.")
