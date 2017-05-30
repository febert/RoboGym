import os,sys
folder = '/home/frederik/Documents/RoboGym/mujoco_models/sawyer/meshes'

for fold in os.listdir(folder):
    subfolder = os.path.join(folder,fold)
    for filename in os.listdir(subfolder):
           infilename = os.path.join(subfolder,filename)
           if not os.path.isfile(infilename): continue
           oldbase = os.path.splitext(filename)
           newname = infilename.replace('.STL', '.stl')
           output = os.rename(infilename, newname)