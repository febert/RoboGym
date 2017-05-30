# to be executed form inside blender

import bpy

def export_all_fbx(exportFolder):
    objects = bpy.data.objects
    for object in objects:
        bpy.ops.object.select_all(action='DESELECT')
        object.select = True
        exportName = exportFolder + object.name + '.fbx'
        bpy.ops.export_scene.stl(filepath=exportName, use_selection=True)

        if object.type != 'MESH':
            continue
        # Clear selection
        bpy.ops.object.select_all(action="DESELECT")
        # Select single object
        object.select = True
        # Export single object to STL
        bpy.ops.export_mesh.stl(
            filepath="/home/frederik/Documents/RoboGym/mujoco_models/environment" + object.name + ".stl")


export_all_fbx('/home/frederik/Documents/RoboGym/mujoco_models/environment')