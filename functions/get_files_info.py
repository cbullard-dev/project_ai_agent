import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself '.')",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
  try:
    working_directory_path = os.path.normpath(os.path.abspath(working_directory))
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    valid_target_dir = os.path.commonpath([working_directory_path,target_dir]) == working_directory_path

    if not valid_target_dir:
      raise Exception(f'Error: Cannot list "{target_dir}" as it is outside the permitted working directory')
    
    is_directory = os.path.isdir(target_dir)

    if not is_directory:
      raise Exception(f'Error: "{target_dir}" is not a directory')
    
    file_in_dir = os.listdir(target_dir)
    file_details = list()
    for file in file_in_dir:
      file_path = os.path.join(target_dir, file)
      file_name = file
      file_size = os.path.getsize(file_path)
      is_dir = os.path.isdir(file_path)
      file_details.append(f"- {file_name}: file_size={file_size}, is_dir={is_dir}")
    
      

    return "\n".join(file_details)
  except Exception as e:
    return e

