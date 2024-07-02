def get_module_tests_prompt(module_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Write a comprehensive set of pytest unit tests 
for the Python module provided below, ensuring full coverage.

Module Code:

{module_content}

The tests should:
1. Include comprehensive tests for all functions and classes.
2. Use descriptive test case names.
3. Cover typical cases, edge cases, and error handling for all functions and methods.
4. Include boundary tests, negative tests, and performance tests where applicable.
5. Use pytest fixtures where appropriate for setup and teardown.
6. Utilize tempfile wherever possible for creating temporary files and directories.
7. Use mocks for external dependencies to isolate the unit under test.
8. Ensure all assertions are clear and informative.
9. Separate different test cases into distinct functions to maintain clarity.

Formatting rules:
1. Follow PEP 8 guidelines for Python code style.
2. Keep lines to a maximum of 120 characters.
3. Ensure test functions are named in a descriptive and clear manner, prefixed with 'test_'.
4. Only output the pytest test code without any additional information or comments.
"""


def get_class_tests_prompt(class_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Write a comprehensive set of pytest unit tests 
for the Python class provided below, ensuring full coverage.

Class Code:

{class_content}

The tests should:
1. Include comprehensive tests for all methods in the class.
2. Use descriptive test case names.
3. Cover typical cases, edge cases, and error handling for all methods.
4. Include boundary tests, negative tests, and performance tests where applicable.
5. Use pytest fixtures where appropriate for setup and teardown.
6. Utilize tempfile wherever possible for creating temporary files and directories.
7. Use mocks for external dependencies to isolate the unit under test.
8. Ensure all assertions are clear and informative.
9. Separate different test cases into distinct functions to maintain clarity.

Formatting rules:
1. Follow PEP 8 guidelines for Python code style.
2. Keep lines to a maximum of 120 characters.
3. Ensure test functions are named in a descriptive and clear manner, prefixed with 'test_'.
4. Only output the pytest test code without any additional information or comments.
"""


def get_function_tests_prompt(function_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Write a comprehensive set of pytest unit tests 
for the Python function provided below, ensuring full coverage.

Function Code:

{function_content}

The tests should:
1. Include comprehensive tests for all possible scenarios.
2. Use descriptive test case names.
3. Cover typical cases, edge cases, and error handling for the function.
4. Include boundary tests, negative tests, and performance tests where applicable.
5. Use pytest fixtures where appropriate for setup and teardown.
6. Utilize tempfile wherever possible for creating temporary files and directories.
7. Use mocks for external dependencies to isolate the unit under test.
8. Ensure all assertions are clear and informative.
9. Separate different test cases into distinct functions to maintain clarity.

Formatting rules:
1. Follow PEP 8 guidelines for Python code style.
2. Keep lines to a maximum of 120 characters.
3. Ensure test functions are named in a descriptive and clear manner, prefixed with 'test_'.
4. Only output the pytest test code without any additional information or comments.
"""
