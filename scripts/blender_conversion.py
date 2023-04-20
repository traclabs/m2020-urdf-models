# https://blender.stackexchange.com/questions/34537/how-to-batch-convert-between-file-formats
# https://docs.blender.org/api/current/bpy.ops.wm.html
import bpy
import os

path="/home/ana/ros/plum/src/m2020-urdf-models/rover/meshes"

for root, dirs, files in os.walk(path):
  for f in files:
    if f.endswith('.gltf'):
      gltf_file = os.path.join(path, f)
      dae_file = os.path.splitext(gltf_file)[0] + ".dae"
      
      bpy.ops.object.select_all(action='SELECT')
      bpy.ops.object.delete()
      
      bpy.ops.import_scene.gltf(filepath=gltf_file)
      bpy.ops.object.select_all(action='SELECT')
      bpy.ops.wm.collada_export(filepath=dae_file, export_global_forward_selection='-Z', export_global_up_selection='Y', apply_global_orientation=True, selected=True)
      