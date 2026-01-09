import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts.prompts import SYSTEM_PROMPT
from config.call_function_config import AVAILABLE_FUNCTIONS
from config.config import MAX_ITERATIONS
from functions.call_function import call_function

def main():
    parser = argparse.ArgumentParser(description="AI Chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    parser.add_argument("--verbose",action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    AI_MODEL = "gemini-2.5-flash"
    prompt_data = args.user_prompt
    messages = [types.Content(role="user",parts=[types.Part(text=prompt_data)])]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    for _ in range(MAX_ITERATIONS):  
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=AI_MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[AVAILABLE_FUNCTIONS]
                ,system_instruction=SYSTEM_PROMPT
                )
            )
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content != None:
                    messages.append(candidate.content)
        usage_metadata = response.usage_metadata
        function_calls = response.function_calls
        if not function_calls:
            if usage_metadata == None:
                raise Exception("response metadata not present")
            response_text = response.text or ""
            prompt_tokens = usage_metadata.prompt_token_count
            response_tokens = usage_metadata.candidates_token_count
            verbose_print_format = f"""
                User prompt: {prompt_data}
                Prompt tokens: {prompt_tokens}
                Response tokens: {response_tokens}
            """

            standard_format = f"""
            Final response:
            {response_text}
            """

            print_list = list()
            print_list.append("\n\n")

            if args.verbose:
                print_list.append(verbose_print_format)
            if response_text:
                print_list.append(standard_format)
            print_format = '\n'.join(print_list)

            print(print_format)
            return

        function_calls_results = list()
        function_strings = list()
        if function_calls:
            for function_call in function_calls:
                function_calls_results.append(call_function(function_call=function_call,verbose=args.verbose))
        if function_calls_results:
            for function_call in function_calls_results:
                if not function_call.parts:
                    raise Exception(f"No 'parts' found in function call responses")
                if function_call.parts[0].function_response == None:
                    raise Exception(f"Function response is None")
                if function_call.parts[0].function_response.response == None:
                    raise Exception(f"Function response is None")
                function_strings.append(f"-> {function_call.parts[0].function_response.response}")
        
        messages.append(
            types.Content(role="user", parts=[function_call.parts[0] for function_call in function_calls_results])
        )
    print(f"Maximum iterations ({MAX_ITERATIONS}) reached")
    sys.exit(1)


if __name__ == "__main__":
    main()
