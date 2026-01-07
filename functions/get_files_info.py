import os

def get_files_info(working_directory, directory="."):
  working_directory_path = os.path.abspath(working_directory)
  target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
  valid_target_dir = os.path.commonpath([working_directory_path,target_dir]) == working_directory_path
  print(f"Working dir: {working_directory}\nTarget dir: {target_dir}\nValid directory: {valid_target_dir}")
  if not valid_target_dir:
    return f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory'
  is_directory = os.path.isdir(target_dir)
  print(f"Is directory: {is_directory}")
  if not is_directory:
    return f'Error: "{target_dir}" is not a directory'