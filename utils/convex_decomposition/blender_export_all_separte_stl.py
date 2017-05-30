
# to be executed form inside blender

import bpy

def export_all_fbx():
    objects = bpy.data.objects
    for object in objects:

        if object.type != 'MESH':
            continue
        # Clear selection
        bpy.ops.object.select_all(action="DESELECT")
        # Select single object
        object.select = True
        # Export single object to STL
        bpy.ops.export_mesh.stl(
            filepath="/home/frederik/Documents/RoboGym/mujoco_models/environment" + object.name + ".stl")


export_all_fbx()
