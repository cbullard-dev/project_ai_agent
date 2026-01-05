import os
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    parser = argparse.ArgumentParser(description="AI Chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    args = parser.parse_args()

    AI_MODEL = "gemini-2.5-flash"
    prompt_data = args.user_prompt
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model= AI_MODEL,contents=prompt_data)
    usage_metadata = response.usage_metadata
    if usage_metadata == None:
        raise Exception("response metadata not present")
    response_text = response.text
    prompt_tokens = usage_metadata.prompt_token_count
    response_tokens = usage_metadata.candidates_token_count
    print_format = f"""
        User prompt: {prompt_data}
        Prompt tokens: {prompt_tokens}
        Response tokens: {response_tokens}
        Response:
        {response_text}
    """
    print(print_format)


if __name__ == "__main__":
    main()
