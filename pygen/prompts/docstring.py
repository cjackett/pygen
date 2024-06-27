def get_module_prompt(module_content: str) -> str:
    return f"""
    You are a professional and experienced software engineer. Write a Python module docstring following PEP 257
    standards and Google-style format for the code provided below.

    Module Code:
    {module_content}

    The docstring should:
    1. Start with a single-line summary in the imperative mood.
    2. Provide a detailed description of the module's purpose and behavior.
    3. Include a section called "Imports:" listing each imported library with a brief description.
    4. Include a section called "Classes:" listing each class method with a brief description.
    5. Include a section called "Functions:" listing each function with brief descriptions.

    Formatting rules:
    1. List each item within "Imports", "Classes", and "Functions" with a dash '-' and indent properly. Only go one
    level deep. I.e. list classes and provide a description, but do not provide deeper information about attributes
    or methods.
    2. Avoid including a typical usage section.
    2. Ensure the docstring lines do not exceed 120 characters.
    4. Only output the docstring without any additional information or comments.
    """


def get_class_prompt(class_content: str) -> str:
    return f"""
    You are a professional and experienced software engineer. Write a Python class docstring following PEP 257
    standards and Google-style format for the code provided below.

    Class Code:
    {class_content}

    The docstring should:
    1. Start with a single-line summary in the imperative mood.
    2. Provide a detailed description of the class's purpose and behavior.
    3. Include a section called "Attributes:" listing each attribute with a brief description.
    4. Include a section called "Methods:" listing each class method with a brief description.
    5. Include a section called "Example:" showing how to instantiate and use the class.

    Formatting rules:
    1. List each item within "Attributes" and "Methods" with a dash '-' and indent properly.
    2. Ensure the docstring lines do not exceed 120 characters.
    3. Only output the docstring without any additional information or comments.
    """


def get_function_prompt(function_content: str) -> str:
    return f"""
    You are a professional and experienced software engineer. Write a Python function docstring following PEP 257
    standards and Google-style format for the code provided below.

    Function Code:
    {function_content}

    The docstring should:
    1. Start with a single-line summary in the imperative mood.
    2. Provide a detailed description of the function's purpose and behavior.
    3. Include a section called "Args:" listing each argument with a brief description.
    4. Include a section called "Returns:" describing the return value.
    5. Include a section called "Raises:" describing any errors that might occur.

    Formatting rules:
    1. List each parameters within "Args" and "Raises" with a dash '-' and indent properly.
    2. Avoid including a typical usage section.
    2. Ensure the docstring lines do not exceed 120 characters.
    4. Only output the docstring without any additional information or comments.
    """
