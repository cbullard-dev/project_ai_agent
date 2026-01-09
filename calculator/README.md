# Command-Line Calculator

## Overview

This project provides a simple yet effective command-line calculator application built with Python. It allows users to evaluate basic arithmetic expressions directly from their terminal, making it a quick tool for computations.

## How It Works

1.  **Expression Input**: The application takes a mathematical expression as a command-line argument (e.g., `python main.py "3 + 5 * 2"`).
2.  **Expression Parsing and Evaluation**: At its core, the `Calculator` class (located in `pkg/calculator.py`) is responsible for parsing and evaluating the input expression. It handles standard arithmetic operations such as addition, subtraction, multiplication, and division, while correctly applying operator precedence rules.
3.  **Result Output**: Once the expression is evaluated, the application formats the original expression and its calculated result into a clear JSON output, which is then printed to the console.

## Why It Exists

This project was created to demonstrate a basic command-line utility for performing arithmetic calculations. It serves as a practical example of:

*   **Command-line argument parsing** in Python.
*   **Implementing a custom arithmetic evaluator** with support for operator precedence.
*   **Modular project structure** using packages (e.g., `pkg`).
*   **Basic error handling** for invalid expressions or inputs.

It's a foundational tool that can be extended with more advanced features, such as support for parentheses, functions, or more complex mathematical operations.