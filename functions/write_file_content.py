import os
from google.genai import types

schema_write_file_content = types.FunctionDeclaration(
  name="write_file_content",
  description="Write content to a file, if the file or the directory path for the file doesn't yet exist create it in the process",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path":types.Schema(
        type=types.Type.STRING,
        description="The file path for the file you need the contents from, relative to the working directory"
      ),
      "content":types.Schema(
        type=types.Type.STRING,
        description="The content of the file to be written in a string format"
      )
    }
  )
)

def write_file(working_directory, file_path, content):
  try:
    full_working_directory = os.path.normpath(os.path.abspath(working_directory))
    full_file_path = os.path.normpath(os.path.join(full_working_directory,file_path))
    is_file_path_valid = os.path.commonpath([full_working_directory,full_file_path]) == full_working_directory
    is_file_dir = os.path.isdir(full_file_path)
    if not is_file_path_valid:
      raise Exception(f'Error: Cannot write to "{full_file_path}" as it is outside the permitted working directory')
    
    if is_file_dir:
      raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
    
    os.makedirs(os.path.dirname(full_file_path),exist_ok=True)

    with open(full_file_path, "w") as f:
      if f.write(content):
        return f'Successfully wrote to "{full_file_path}" ({len(content)} characters written)'

    
    
  except Exception as e:
    return e