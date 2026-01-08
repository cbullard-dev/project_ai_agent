import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
  try:
    full_working_directory = os.path.normpath(os.path.abspath(working_directory))
    full_file_path = os.path.normpath(os.path.join(full_working_directory, file_path))
    is_file_path_valid = os.path.commonpath([full_working_directory,full_file_path]) == full_working_directory
    is_file_type_valid = os.path.isfile(full_file_path)
    is_file_type_python = full_file_path.split(".")[-1] == "py"
    if not is_file_path_valid:
      raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not is_file_type_valid:
      raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
    if not is_file_type_python:
      raise Exception(f'Error: "{file_path}" is not a Python file')
    command = ["python", full_file_path]
    if args:
      for arg in args:
        command.extend(arg)
    process_run = subprocess.run(command,text=True, capture_output=True, timeout=30)
    completion_string_list = []
    if process_run.returncode != 0:
      completion_string_list.append(f"Process exited with code {process_run.returncode}")
    if process_run.stdout == '' and process_run.stderr == '':
      completion_string_list.append(f"\nNo output produced")
      return "\n".join(completion_string_list)
    if process_run.stdout != '':
      completion_string_list.append(f"STDOUT: {process_run.stdout}")
    if process_run.stderr != '':
      completion_string_list.append(f"STDERR: {process_run.stderr}")
    return "\n".join(completion_string_list)
      
    
  except Exception as e:
    return f"Error: executing Python file: {e}"