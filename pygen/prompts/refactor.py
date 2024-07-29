def get_function_refactor_prompt(function_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Refactor the Python function provided below to
improve its design and implementation, ensuring it adheres to software engineering best practices.

Function Code:

{function_content}

Your refactoring should address the following key areas:
1. Code Quality: Improve the readability, consistency, and maintainability of the code, ensuring adherence to PEP 8
standards.
2. Strong Typing: Implement strong typing using PEP 484.
3. Design Principles: Refactor the function to adhere to SOLID principles (Single Responsibility, Open/Closed,
Liskov Substitution, Interface Segregation, Dependency Inversion), the DRY (Don't Repeat Yourself) principle, and the
YAGNI (You Aren't Gonna Need It) principle.
4. Design Patterns: Identify and implement appropriate design patterns to enhance the function's design and efficiency.
5. Documentation: Ensure the function's docstring and comments are complete, clear, and adhere to PEP 257 standards.
6. Error Handling: Improve how errors and exceptions are managed within the function.
7. Performance and Scalability: Address any potential performance issues or bottlenecks, and ensure the function is
designed to handle increased load and scale effectively.
8. Security: Identify and mitigate any potential security vulnerabilities or practices that could lead to security
issues.

Formatting rules:
1. Ensure the function's docstring adheres to PEP 257 standards.
2. Ensure the code adheres to PEP 8 and PEP 484 standards.
3. Ensure all lines, including the docstring, do not exceed 120 characters.
4. Only output the refactored code without any additional information or comments.
"""
