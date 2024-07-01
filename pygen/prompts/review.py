def get_module_prompt(module_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python module provided below, ensuring it adheres to software engineering best practices.

Module Code:

{module_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the module's design for modularity, single responsibility, and separation of
concerns.
3. Documentation: Review the module's docstrings and comments for completeness, clarity, and adherence to PEP 257
standards.
4. Error Handling: Examine how errors and exceptions are managed within the module.
5. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
6. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the module, and assess
whether the module is designed to handle increased load and scale effectively.
7. Security: Evaluate the code for any potential security vulnerabilities or practices that could lead to security
issues.

Provide detailed feedback on each point, referencing specific parts of the module where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""


def get_class_prompt(class_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python class provided below, ensuring it adheres to software engineering best practices.

Class Code:

{class_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the class design for principles such as single responsibility and proper
encapsulation.
3. Documentation: Review the class's docstrings and comments for completeness, clarity, and adherence to PEP 257
standards.
4. Error Handling: Examine how errors and exceptions are managed within the class.
5. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
6. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the class, and assess
whether the class is designed to handle increased load and scale effectively.
7. Security: Evaluate the class for any potential security vulnerabilities or practices that could lead to security
issues.

Provide detailed feedback on each point, referencing specific parts of the class where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""


def get_function_prompt(function_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the design and implementation of the
Python function provided below, ensuring it adheres to software engineering best practices.

Function Code:

{function_content}

Your review should cover the following key areas:
1. Code Quality: Assess the overall quality of the code, including readability, consistency, maintainability,
and adherence to PEP 8 standards.
2. Design Principles: Evaluate the function's design for principles such as single responsibility and proper
abstraction.
3. Documentation: Review the function's docstring and comments for completeness, clarity, and adherence to PEP 257
standards.
4. Error Handling: Examine how errors and exceptions are managed within the function.
5. Dependencies: Identify any external libraries or modules used, and assess their necessity and impact.
6. Performance and Scalability: Analyze any potential performance issues or bottlenecks in the function, and assess
whether the function is designed to handle increased load and scale effectively.
7. Security: Evaluate the function for any potential security vulnerabilities or practices that could lead to
security issues.

Provide detailed feedback on each point, referencing specific parts of the function where necessary, and discuss the
overall strengths and weaknesses of the implementation.
"""
