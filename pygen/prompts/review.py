def get_module_refactor_prompt(module_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Refactor the Python module provided below to
improve its design and implementation, ensuring it adheres to software engineering best practices.

Module Code:

{module_content}

Your review should address the following key areas:
1. Code Quality: Improve the readability, consistency, and maintainability of the code, ensuring adherence to PEP 8
standards.
2. Strong Typing: Implement strong typing using PEP 484.
3. Design Principles: Refactor the module to adhere to SOLID principles (Single Responsibility, Open/Closed, Liskov
Substitution, Interface Segregation, Dependency Inversion), the DRY (Don't Repeat Yourself) principle, and the YAGNI
(You Aren't Gonna Need It) principle.
4. Design Patterns: Identify and implement appropriate design patterns to enhance the module's design and efficiency.
5. Documentation: Ensure the module's docstring and comments are complete, clear, and adhere to PEP 257 standards.
6. Error Handling: Improve how errors and exceptions are managed within the module.
7. Performance and Scalability: Address any potential performance issues or bottlenecks, and ensure the module is
designed to handle increased load and scale effectively.
8. Security: Identify and mitigate any potential security vulnerabilities or practices that could lead to security
issues.

Formatting rules:
1. Ensure the module's docstring adheres to PEP 257 standards.
2. Ensure the code adheres to PEP 8 and PEP 484 standards.
3. Ensure all lines, including the docstring, do not exceed 120 characters.
4. Only output the refactored code without any additional information or comments.
"""


def get_module_review_prompt(module_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python module provided below, ensuring it adheres to software engineering best practices.

Module Code:

{module_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the module's design for modularity, separation of concerns, adherence to SOLID principles
(Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), the DRY (Don't
Repeat Yourself) principle, and YAGNI (You Aren't Gonna Need It) principle.
3. Design Patterns: Identify any design patterns used within the module, evaluate their appropriateness, and suggest
any additional patterns that could improve the design.
4. Documentation: Review the module's docstrings and comments for completeness, clarity, and adherence to PEP 257
standards.
5. Error Handling: Examine how errors and exceptions are managed within the module.
6. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
7. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the module, and assess
whether the module is designed to handle increased load and scale effectively.
8. Security: Evaluate the code for any potential security vulnerabilities or practices that could lead to security
issues.

Provide detailed feedback on each point, referencing specific parts of the module where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""


def get_class_review_prompt(class_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python class provided below, ensuring it adheres to software engineering best practices.

Class Code:

{class_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the class design for proper encapsulation and adherence to SOLID principles (Single
Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), the DRY (Don't Repeat
Yourself) principle, and YAGNI (You Aren't Gonna Need It) principle.
3. Design Patterns: Identify any design patterns used within the class, evaluate their appropriateness, and suggest
any additional patterns that could improve the design.
4. Documentation: Review the class's docstrings and comments for completeness, clarity, and adherence to PEP 257
standards.
5. Error Handling: Examine how errors and exceptions are managed within the class.
6. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
7. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the class, and assess
whether the class is designed to handle increased load and scale effectively.
8. Security: Evaluate the class for any potential security vulnerabilities or practices that could lead to security
issues.

Provide detailed feedback on each point, referencing specific parts of the class where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""


def get_function_review_prompt(function_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python function provided below, ensuring it adheres to software engineering best practices.

Function Code:

{function_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the function's design for proper abstraction and adherence to SOLID principles (Single
Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion), the DRY (Don't Repeat
Yourself) principle, and YAGNI (You Aren't Gonna Need It) principle.
3. Design Patterns: Identify any design patterns used within the function, evaluate their appropriateness, and suggest
any additional patterns that could improve the design.
4. Documentation: Review the function's docstring and comments for completeness, clarity, and adherence to PEP 257
standards.
5. Error Handling: Examine how errors and exceptions are managed within the function.
6. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
7. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the function, and assess
whether the function is designed to handle increased load and scale effectively.
8. Security: Evaluate the function for any potential security vulnerabilities or practices that could lead to
security issues.

Provide detailed feedback on each point, referencing specific parts of the function where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""
