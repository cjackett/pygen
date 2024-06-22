def get_module_prompt(module_content: str) -> str:
    return f"""Write a module-level Python docstring for the following code using PEP 257 standards and Google-style
format. Ensure the docstring does not wrap lines. Only provide the docstring without any additional information or
comments.

Module Content:
{module_content}

The docstring should include:
1. Begin with triple quotes on a line by itself followed by a carriage return.
2. A single-line heading starting on the second line.
3. A longer description of the module's functionality.
4. A list of imports with brief descriptions.
5. A list of classes with brief descriptions, including nested exceptions and methods if applicable.
6. A list of functions with brief descriptions.

Make sure that listed imports, classes and functions are tabbed and start with a dash '-'. Only go one level deep.
I.e. list classes and provide a description, but do not provide deeper information about attributes or methods. Do
not provide a typical usage section and omit the imports, classes and functions lists if they are empty.
"""


def get_class_prompt(class_content: str) -> str:
    return f"""Write a class-level Python docstring for the following code using PEP 257 standards and Google-style
format. Ensure the docstring does not wrap lines. Only provide the docstring without any additional information or
comments.

Class Code:
{class_content}

The docstring should include:
1. A concise single-line summary of the class.
2. A detailed description of the class's functionality and purpose.
3. A list of attributes, each with a brief description.
4. A list of methods, each with a brief description.

Attributes and methods should be listed with a dash '-' and properly indented. Only go one level deep, listing the
attributes and methods with their descriptions without delving into further details about the attributes or methods
themselves. Do not include a typical usage section and omit the attributes and methods lists if they are empty.
"""


def get_function_prompt(function_content: str) -> str:
    return f"""
    Generate a Python function docstring following PEP 257 standards and Google-style format for the code provided
    below.

    Function Code:
    {function_content}

    The docstring should:
    1. Start with triple quotes on a line by itself.
    2. Include a single-line summary on the second line starting with an imperative mood.
    3. Provide a detailed description of the function's purpose and behavior.
    4. Include a section called "Args:" listing each parameter with a brief description.
    5. Include a section called "Returns:" describing the return value, if applicable.

    Formatting rules:
    1. List each parameters within Args and Returns lists with a dash '-' and indent properly.
    2. Avoid including a typical usage section.
    3. Ensure the docstring lines do not wrap.
    4. Only output the docstring without any additional information or comments.
    """
