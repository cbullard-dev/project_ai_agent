import os

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