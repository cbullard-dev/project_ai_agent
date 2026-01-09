# AI Agent Project

This project implements an AI Agent chatbot using the `gemini-2.5-flash` model. It is designed to interact with a file system and execute Python code based on user prompts. The `main.py` script serves as the core entry point, parsing user input, managing the conversation flow with the AI model, and orchestrating function calls.

## Disclaimer:

This AI Agent is developed for educational and learning purposes only. It is not recommended for use in production environments due to the absence of comprehensive security, safety, and robustness features that a production-grade AI system would require. Users should exercise caution and discretion when interacting with this agent.

## Key Features:

*   **AI-Powered Interaction:** Leverages the `gemini-2.5-flash` model to process user prompts and generate responses.
*   **Function Calling:** Capable of invoking a set of predefined functions to interact with the local environment.
*   **File System Operations:** Through its functions, the agent can:
    *   List files and directories (`get_files_info`)
    *   Read the content of files (`get_file_content`)
    *   Write content to files (`write_file_content`)
    *   Execute Python scripts (`run_python_file`)
*   **Iterative Conversation:** The `main.py` script allows for a multi-turn conversation up to a defined maximum number of iterations (`MAX_ITERATIONS`).
*   **Verbose Output:** Supports a `--verbose` flag for more detailed output during execution.

## How it Works:

1.  The `main.py` script takes a `user_prompt` as a command-line argument.
2.  It initializes a conversation with the AI model, passing the user's prompt and a system instruction.
3.  The AI model can respond with text or suggest function calls.
4.  If function calls are suggested, the `call_function.py` module dispatches these calls to the appropriate Python functions (e.g., `get_files_info`, `write_file_content`).
5.  The results of the function calls are then fed back into the AI model, allowing it to continue the conversation or generate a final response.
6.  The process repeats until the AI provides a final text response or the maximum number of iterations is reached.

*This update was made by this application itself as a demonstration of what the application can do.*