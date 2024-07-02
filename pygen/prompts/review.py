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
