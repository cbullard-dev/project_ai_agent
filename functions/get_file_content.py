import os
from config.config import MAX_FILE_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
  try:  
    working_directory_path = os.path.abspath(working_directory)
    absolute_file_path = os.path.normpath(os.path.join(working_directory_path,file_path))
    file_path_valid = os.path.commonpath([working_directory_path,absolute_file_path]) == working_directory_path
    is_file = os.path.isfile(absolute_file_path)

    if not file_path_valid:
      raise Exception(f'Error: Cannot read "{absolute_file_path}" as it is outside permitted working directory {working_directory_path}')
    
    if not is_file:
      raise Exception(f'Error: File not found or is not a regular file: "{absolute_file_path}"')
    
    with open(absolute_file_path, "r") as f:
      content_string = f.read(MAX_FILE_CHARS)
      if f.read(MAX_FILE_CHARS):
        content_string += f'[...File "{absolute_file_path}" truncated at {MAX_FILE_CHARS} characters]'
    return content_string

  except Exception as e:
    return e