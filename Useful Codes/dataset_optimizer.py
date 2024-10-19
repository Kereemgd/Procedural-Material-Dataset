import os

# Define the folder containing the text files
folder_path = "Finetune data/3.4k_mat_txt_preprocess"

# Define the rules for removal
removal_rules = [
    ".default_value = 0.5",
    ".use_clamp = False",
    ".name",
    ".operation = 'ADD'"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_math = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeMath" in stripped_line:
            inside_shader_node_math = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_math:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeMath section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_math = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os
# Define the rules for removal
removal_rules = [
    ".name",
    ".blend_type = 'MIX'",
    ".clamp_result = False",
    ".clamp_factor = True",
    ".factor_mode = 'UNIFORM'",
    ".inputs[0].default_value = 0.5",
    ".inputs[1].default_value = (0.5, 0.5, 0.5)",
    ".inputs[2].default_value = 0.0",
    ".inputs[3].default_value = 0.0",
    ".inputs[4].default_value = (0.0, 0.0, 0.0)",
    ".inputs[5].default_value = (0.0, 0.0, 0.0)",
    ".inputs[6].default_value = (0.5, 0.5, 0.5, 1.0)",
    ".inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)"
]

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_lines = False
    node_started = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeMix" in stripped_line:
            node_started = True
        
        if node_started:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If line does not match any removal rule and section has ended
            if stripped_line.startswith("shader_node_mix") or not stripped_line:
                node_started = False
        
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")
import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".distribution = 'MULTI_GGX'",
    ".subsurface_method = 'RANDOM_WALK'",
    ".inputs[0].default_value = (0.8, 0.8, 0.8, 1.0)",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 0.5",
    ".inputs[3].default_value = 1.5",
    ".inputs[4].default_value = 1.0",
    ".inputs[5].default_value = (0.0, 0.0, 0.0)",
    ".inputs[6].default_value = 0.0",
    ".inputs[7].default_value = 0.0",
    ".inputs[8].default_value = (1.0, 0.2, 0.1)",
    ".inputs[9].default_value = 0.05",
    ".inputs[10].default_value = 1.4",
    ".inputs[11].default_value = 0.0",
    ".inputs[12].default_value = 0.5",
    ".inputs[13].default_value = (1.0, 1.0, 1.0, 1.0)",
    ".inputs[14].default_value = 0.0",
    ".inputs[15].default_value = 0.0",
    ".inputs[16].default_value = (0.0, 0.0, 0.0)",
    ".inputs[17].default_value = 0.0",
    ".inputs[18].default_value = 0.0",
    ".inputs[19].default_value = 0.029",
    ".inputs[20].default_value = 1.5",
    ".inputs[21].default_value = (1.0, 1.0, 1.0, 1.0)",
    ".inputs[22].default_value = (0.0, 0.0, 0.0)",
    ".inputs[23].default_value = 0.0",
    ".inputs[24].default_value = 0.5",
    ".inputs[25].default_value = (1.0, 1.0, 1.0, 1.0)",
    ".inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)",
    ".inputs[27].default_value = 0.0",
    ".inputs[28].default_value = 0.0",
    ".inputs[29].default_value = 1.3"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_bsdf_principled = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeBsdfPrincipled" in stripped_line:
            inside_shader_node_bsdf_principled = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_bsdf_principled:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeBsdfPrincipled section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_bsdf_principled = False
            
        new_lines.append(line)
    
    with open(file_path, 'w',encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".color_ramp.color_mode = 'RGB'",
    ".color_ramp.hue_interpolation = 'NEAR'",
    ".color_ramp.interpolation = 'LINEAR'",
    ".name"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_val_to_rgb = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeValToRGB" in stripped_line:
            inside_shader_node_val_to_rgb = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_val_to_rgb:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeValToRGB section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_val_to_rgb = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".noise_dimensions = '3D'",
    ".noise_type = 'FBM'",
    ".normalize = True",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 5.0",
    ".inputs[3].default_value = 2.0",
    ".inputs[4].default_value = 0.5",
    ".inputs[5].default_value = 2.0",
    ".inputs[8].default_value = 0.0",
    ".inputs[7].default_value = 1.0",
    ".inputs[6].default_value = 0.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_tex_noise = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeTexNoise" in stripped_line:
            inside_shader_node_tex_noise = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_tex_noise:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeTexNoise section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_tex_noise = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".inputs[0].default_value = 0.0",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 0.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_combine_xyz = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeCombineXYZ" in stripped_line:
            inside_shader_node_combine_xyz = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_combine_xyz:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeCombineXYZ section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_combine_xyz = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_separate_xyz = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeSeparateXYZ" in stripped_line:
            inside_shader_node_separate_xyz = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_separate_xyz:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeSeparateXYZ section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_separate_xyz = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".invert = False",
    ".inputs[0].default_value = 1.0",
    ".inputs[1].default_value = 1.0",
    ".inputs[2].default_value = 1.0",
    ".inputs[3].default_value = (0.0, 0.0, 0.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_bump = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeBump" in stripped_line:
            inside_shader_node_bump = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_bump:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeBump section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_bump = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")


import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".from_instancer = False"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_tex_coord = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeTexCoord" in stripped_line:
            inside_shader_node_tex_coord = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_tex_coord:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeTexCoord section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_tex_coord = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os


# Define the rules for removal
removal_rules = [
    ".name",
    ".is_active_output = True",
    ".target = 'ALL'"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_output_material = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeOutputMaterial" in stripped_line:
            inside_shader_node_output_material = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_output_material:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeOutputMaterial section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_output_material = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal
removal_rules = [
    ".name",
    ".inputs[0].default_value = 0.5"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_mix_shader = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeMixShader" in stripped_line:
            inside_shader_node_mix_shader = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_mix_shader:
            if any(rule in stripped_line for rule in removal_rules):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeMixShader section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_mix_shader = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeMapRange
removal_rules_map_range = [
    ".clamp = True",
    ".data_type = 'FLOAT'",
    ".interpolation_type = 'LINEAR'",
    ".inputs[0].default_value = 1.0",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 1.0",
    ".inputs[3].default_value = 0.0",
    ".inputs[4].default_value = 1.0",
    ".inputs[5].default_value = 4.0",
    ".inputs[6].default_value = (0.0, 0.0, 0.0)",
    ".inputs[7].default_value = (0.0, 0.0, 0.0)",
    ".inputs[8].default_value = (1.0, 1.0, 1.0)",
    ".inputs[9].default_value = (0.0, 0.0, 0.0)",
    ".inputs[10].default_value = (1.0, 1.0, 1.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_map_range = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeMapRange" in stripped_line:
            inside_shader_node_map_range = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_map_range:
            if any(rule in stripped_line for rule in removal_rules_map_range):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeMapRange section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_map_range = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeMapping
removal_rules_mapping = [
    ".vector_type = 'POINT'",
    ".default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = (0.0, 0.0, 0.0)",
    ".inputs[2].default_value = (0.0, 0.0, 0.0)",
    ".inputs[3].default_value = (1.0, 1.0, 1.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_mapping = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeMapping" in stripped_line:
            inside_shader_node_mapping = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_mapping:
            if any(rule in stripped_line for rule in removal_rules_mapping):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeMapping section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_mapping = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeTexVoronoi
removal_rules_voronoi = [
    ".name",
    ".distance = 'EUCLIDEAN'",
    ".feature = 'F1'",
    ".normalize = False",
    ".voronoi_dimensions = '3D'",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 5.0",
    ".inputs[3].default_value = 0.0",
    ".inputs[4].default_value = 0.5",
    ".inputs[5].default_value = 2.0",
    ".inputs[8].default_value = 1.0",
    ".inputs[7].default_value = 0.5",
    ".inputs[6].default_value = 1.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_voronoi = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeTexVoronoi" in stripped_line:
            inside_shader_node_voronoi = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_voronoi:
            if any(rule in stripped_line for rule in removal_rules_voronoi):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeTexVoronoi section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_voronoi = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeVectorMath
removal_rules_vector_math = [
    ".name",
    ".operation = 'ADD'",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = (0.0, 0.0, 0.0)",
    ".inputs[2].default_value = (0.0, 0.0, 0.0)",
    ".inputs[3].default_value = 1.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_vector_math = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeVectorMath" in stripped_line:
            inside_shader_node_vector_math = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_vector_math:
            if any(rule in stripped_line for rule in removal_rules_vector_math):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeVectorMath section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_vector_math = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeLayerWeight
removal_rules_layer_weight = [
    ".inputs[0].default_value = 0.5"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_layer_weight = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeLayerWeight" in stripped_line:
            inside_shader_node_layer_weight = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_layer_weight:
            if any(rule in stripped_line for rule in removal_rules_layer_weight):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeLayerWeight section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_layer_weight = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the rules for removal for ShaderNodeTexChecker
removal_rules_tex_checker = [
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = (0.8, 0.8, 0.8, 1.0)",
    ".inputs[2].default_value = (0.2, 0.2, 0.2, 1.0)",
    ".inputs[3].default_value = 5.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_tex_checker = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeTexChecker" in stripped_line:
            inside_shader_node_tex_checker = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_tex_checker:
            if any(rule in stripped_line for rule in removal_rules_tex_checker):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeTexChecker section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_tex_checker = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the folder containing the text files

# Define the rules for removal for ShaderNodeBsdfAnisotropic
removal_rules_bsdf_anisotropic = [
    ".distribution = 'MULTI_GGX'",
    ".inputs[0].default_value = (0.8, 0.8, 0.8, 1.0)",
    ".inputs[1].default_value = 0.5",
    ".inputs[2].default_value = 0.0",
    ".inputs[3].default_value = 0.0",
    ".inputs[4].default_value = (0.0, 0.0, 0.0)",
    ".inputs[5].default_value = (0.0, 0.0, 0.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_bsdf_anisotropic = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeBsdfAnisotropic" in stripped_line:
            inside_shader_node_bsdf_anisotropic = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_bsdf_anisotropic:
            if any(rule in stripped_line for rule in removal_rules_bsdf_anisotropic):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeBsdfAnisotropic section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_bsdf_anisotropic = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os
# Define the rules for removal for ShaderNodeBsdfGlass
removal_rules_bsdf_glass = [
    ".distribution = 'MULTI_GGX'",
    ".inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)",
    ".inputs[1].default_value = 0.0",
    ".inputs[2].default_value = 1.5",
    ".inputs[3].default_value = (0.0, 0.0, 0.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    inside_shader_node_bsdf_glass = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if "ShaderNodeBsdfGlass" in stripped_line:
            inside_shader_node_bsdf_glass = True
            new_lines.append(line)
            continue
        
        if inside_shader_node_bsdf_glass:
            if any(rule in stripped_line for rule in removal_rules_bsdf_glass):
                continue  # Skip the line if it matches the removal rule
            
            # If the end of the ShaderNodeBsdfGlass section is detected, stop skipping lines
            if stripped_line == "":
                inside_shader_node_bsdf_glass = False
            
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os
# Define the patterns to look for and remove
removal_patterns = [
    ".attribute_domain = 'POINT'",
    ".label",
    ".name",
    ".parent",
    ".hide"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Filter out lines that match any of the removal patterns
    new_lines = [line for line in lines if not any(pattern in line for pattern in removal_patterns)]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os
# Define the node and attributes to remove
node_name = "ShaderNodeTexWave"
attributes_to_remove = [
    ".bands_direction = 'X'",
    ".rings_direction = 'X'",
    ".wave_profile = 'SIN'",
    ".wave_type = 'BANDS'",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = 5.0",
    ".inputs[2].default_value = 0.0",
    ".inputs[3].default_value = 2.0",
    ".inputs[4].default_value = 1.0",
    ".inputs[5].default_value = 0.5",
    ".inputs[6].default_value = 0.0"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_lines = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if node_name in stripped_line:
            skip_lines = True
        
        if skip_lines:
            if any(attr in stripped_line for attr in attributes_to_remove):
                continue  # Skip the line if it matches any attribute to remove
            
            # Stop skipping lines when encountering a line that indicates the end of the node block
            if not stripped_line or node_name not in stripped_line:
                skip_lines = False
        
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the node and attributes to remove
node_name = "ShaderNodeDisplacement"
attributes_to_remove = [
    ".space = 'OBJECT'",
    ".inputs[0].default_value = 0.0",
    ".inputs[1].default_value = 0.5",
    ".inputs[2].default_value = 1.0",
    ".inputs[3].default_value = (0.0, 0.0, 0.0)"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_lines = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if node_name in stripped_line:
            skip_lines = True
        
        if skip_lines:
            if any(attr in stripped_line for attr in attributes_to_remove):
                continue  # Skip the line if it matches any attribute to remove
            
            # Stop skipping lines when encountering a line that indicates the end of the node block
            if not stripped_line or node_name not in stripped_line:
                skip_lines = False
        
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os

# Define the node and attributes to remove
node_name = "ShaderNodeTexBrick"
attributes_to_remove = [
    ".offset = 0.5",
    ".offset_frequency = 2",
    ".squash = 1.0",
    ".squash_frequency = 2",
    ".inputs[0].default_value = (0.0, 0.0, 0.0)",
    ".inputs[1].default_value = (0.8, 0.8, 0.8, 1.0)",
    ".inputs[2].default_value = (0.2, 0.2, 0.2, 1.0)",
    ".inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)",
    ".inputs[4].default_value = 5.0",
    ".inputs[5].default_value = 0.02",
    ".inputs[6].default_value = 0.1",
    ".inputs[7].default_value = 0.0",
    ".inputs[8].default_value = 0.5",
    ".inputs[9].default_value = 0.25"
]

# Function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_lines = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if node_name in stripped_line:
            skip_lines = True
        
        if skip_lines:
            if any(attr in stripped_line for attr in attributes_to_remove):
                continue  # Skip the line if it matches any attribute to remove
            
            # Stop skipping lines when encountering a line that indicates the end of the node block
            if not stripped_line or node_name not in stripped_line:
                skip_lines = False
        
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")

import os
# Define the attributes to remove
attributes_to_remove = [
    ".default_value = (0.0, 0.0, 0.0)",
    ".subtype = 'NONE'",
    ".attribute_domain = 'POINT'"
]

# Define a function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_lines = False
    node_detected = False
    
    for line in lines:
        stripped_line = line.strip()

        # Check if the line contains a node definition
        if "ShaderNode" in stripped_line:
            node_detected = True
        
        if node_detected:
            if any(attr in stripped_line for attr in attributes_to_remove):
                continue  # Skip the line if it matches any attribute to remove
            
            # Stop skipping lines when encountering a line that indicates the end of the node block
            if not stripped_line or "ShaderNode" not in stripped_line:
                node_detected = False
        
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("Processing complete.")


import os

# Define a function to process each file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_section = False
    
    for line in lines:
        stripped_line = line.strip()

        # Detect the start of the NodeFrame section
        if "NodeFrame" in stripped_line:
            skip_section = True

        # If in NodeFrame section, skip lines
        if skip_section:
            # Detect the end of the NodeFrame section (usually the closing bracket or similar)
            if stripped_line.endswith("}") or stripped_line == "":
                skip_section = False
            continue
        
        # Add lines that are not within NodeFrame sections
        new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Process all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        process_file(os.path.join(folder_path, filename))

print("NodeFrame sections removed.")
