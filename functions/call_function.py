from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file
from functions.run_python_file import run_python_file
from google.genai import types

def call_function(function_call, verbose=False):
  function_name = function_call.name or ""
  function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file_content": write_file,
    "run_python_file": run_python_file
  }
  function_call_string = f"- Calling function: {function_call.name}"
  if verbose:
    function_call_string += f"({function_call.args})"
  print(function_call_string)

  if function_name not in function_map:
    return types.Content(
      role="tool",
      parts=[
        types.Part.from_function_response(
          name=function_name,
          response={"error": f"Unknown function: {function_name}"}
        )
      ]
    )
  
  args = dict(function_call.args) if function_call.arg else {}
  args["working_directory"] = "./calculator"

  function_result = function_map[function_name](**args)

  return types.Content(
    role="tool",
    parts=[
      types.Part.from_function_response(
        name=function_name,
        response={"result": function_result}
      )
    ]
  )