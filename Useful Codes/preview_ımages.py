import bpy
import os

# Specify the folder containing the .txt files
folder_path = "C:/Users/mesey/Downloads/MaterialScraper/synthetic_mat_codes/"  # Replace with your folder path

# Iterate through all .txt files in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            try:
                # Read and execute the contents of the file
                exec(file.read())
                print(f"Executed {filename} successfully.")
            except Exception as e:
                print(f"Error executing {filename}: {e}")

# Optional: If you want to create a material for each defined material in the .txt files, ensure
def render_scene_with_material(material):
    # Create a new scene for the preview
    scene = bpy.context.scene

    # Delete all existing objects in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Create a new UV Sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
    sphere = bpy.context.object

    # Add a subdivision surface modifier to subdivide the sphere
    bpy.ops.object.modifier_add(type='SUBSURF')
    sphere_mod = sphere.modifiers["Subdivision"]
    sphere_mod.levels = 3  # Viewport subdivision level
    sphere_mod.render_levels = 3  # Render subdivision level

    # Apply the subdivision modifier (optional)
    bpy.ops.object.modifier_apply(modifier="Subdivision")

    # Enable smooth shading
    bpy.ops.object.shade_smooth()

    # Apply the material to the sphere
    if len(sphere.data.materials) == 0:
        sphere.data.materials.append(material)
    else:
        sphere.data.materials[0] = material

    # Set up the camera
    bpy.ops.object.camera_add(enter_editmode=False, location=(0, 0, 3))
    camera = bpy.context.object
    camera.rotation_euler = (0, 0, 0)
    scene.camera = camera

    # Set up the light source
    bpy.ops.object.light_add(type='POINT', location=(0.8, -0.02, 4))
    light = bpy.context.object
    light.data.energy = 2500

    # Ensure the camera object is selected and active
    bpy.context.view_layer.objects.active = camera
    camera.select_set(True)

    # Set the 3D Viewport to camera perspective
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.region_3d.view_perspective = 'CAMERA'
                    space.shading.type = 'MATERIAL'  # Switch to Material Preview mode
                    break
            break

    # Set render engine to Eevee
    scene.render.engine = 'BLENDER_EEVEE'

    # Enable bloom, ambient occlusion, and screen space reflections
    scene.eevee.use_bloom = True
    scene.eevee.use_gtao = True  # Ambient Occlusion
    scene.eevee.use_ssr = True  # Screen Space Reflections

    # Set render settings
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    mat_name = material.name
    scene.render.filepath = f"C:/Users/mesey/Downloads/MaterialScraper/synthetic_mat_codes/{mat_name}"

    # Render the scene using Eevee
    bpy.ops.render.render(write_still=True)


# Iterate over all materials in bpy.context.data.materials
for material in bpy.context.blend_data.materials:
    render_scene_with_material(material)

print("Rendering complete.")
