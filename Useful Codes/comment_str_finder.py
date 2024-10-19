import bpy

# List of node names you're interested in
shader_nodes = ["ShaderNodeMath", "ShaderNodeMix", "ShaderNodeValToRGB", "ShaderNodeTexNoise", "ShaderNodeCombineXYZ",
                "ShaderNodeSeparateXYZ", "ShaderNodeBump", "ShaderNodeTexCoord", "ShaderNodeOutputMaterial", 
                "ShaderNodeMapRange", "ShaderNodeMapping", "ShaderNodeBsdfPrincipled", "ShaderNodeMixShader", 
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

# Function to add a node and get its socket information
def add_and_get_node_sockets(node_type):
    # Get the active material
    material = bpy.context.object.active_material

    if material and material.use_nodes:
        # Get the node tree of the material
        node_tree = material.node_tree

        # Add a new node of the specified type
        new_node = node_tree.nodes.new(type=node_type)
        
        # Store the socket information
        socket_info = {
            'inputs': {},
            'outputs': {}
        }
        
        # Collect the input sockets with their index
        for i, input in enumerate(new_node.inputs):
            socket_info['inputs'][i] = input.identifier

        # Collect the output sockets with their index
        for i, output in enumerate(new_node.outputs):
            socket_info['outputs'][i] = output.identifier
        
        return socket_info
    else:
        print("No active material with nodes found.")
        return None

# Function to process all nodes and gather their socket information
def process_all_nodes(shader_nodes):
    all_node_info = {}

    for node_type in shader_nodes:
        print(f"Processing node type: {node_type}")
        socket_info = add_and_get_node_sockets(node_type)
        if socket_info is not None:
            all_node_info[node_type] = socket_info
    
    return all_node_info

# Function to save the node information to text files
def save_node_info_to_files(node_info, output_dir):
    import os
    
    os.makedirs(output_dir, exist_ok=True)

    for node_type, info in node_info.items():
        output_file_path = os.path.join(output_dir, f"{node_type}.txt")
        print(f"Saving attributes for node {node_type} to {output_file_path}")
        with open(output_file_path, 'w') as file:
            file.write("input_output_map = {\n")
            file.write("    'inputs': {\n")
            for index, name in info['inputs'].items():
                file.write(f"        {index}: \"{name}\",\n")
            file.write("    },\n")
            file.write("    'outputs': {\n")
            for index, name in info['outputs'].items():
                file.write(f"        {index}: \"{name}\",\n")
            file.write("    }\n")
            file.write("}\n")

def main():
    node_info = process_all_nodes(shader_nodes)
    save_node_info_to_files(node_info, "str_text_files")

if __name__ == "__main__":
    main()
