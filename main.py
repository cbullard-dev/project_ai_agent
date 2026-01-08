import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts.prompts import SYSTEM_PROMPT

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

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model= AI_MODEL,contents=messages,config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT))
    usage_metadata = response.usage_metadata
    if usage_metadata == None:
        raise Exception("response metadata not present")
    response_text = response.text
    prompt_tokens = usage_metadata.prompt_token_count
    response_tokens = usage_metadata.candidates_token_count
    verbose_print_format = f"""
        User prompt: {prompt_data}
        Prompt tokens: {prompt_tokens}
        Response tokens: {response_tokens}
        Response:
        {response_text}
    """

    print_format = f"""
    Response:
    {response_text}
    """

    if args.verbose:
        print_format = verbose_print_format

    print(print_format)


if __name__ == "__main__":
    main()
