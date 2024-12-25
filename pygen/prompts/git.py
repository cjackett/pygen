def get_pr_prompt(branch1: str, branch2: str, diff_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Write a comprehensive Git pull request
message for the following diff between branches '{branch1}' and '{branch2}'. Follow a rigorous and structured format
including:

Title: [Feature/Fix/Chore/Refactor/Performance/Style/Test/Docs/Security/Hotfix] Provide a concise and descriptive
title for the pull request.
    Example: [Feature] Adding feature X to improve Y
    Example: [Fix] Resolve bug in user authentication
    Example: [Refactor] Simplify data processing logic in module Z

Summary: Provide a detailed description of the purpose of the pull request in one paragraph containing no more than 8
sentences.
    Example: This pull request adds feature X to improve the performance of Y by implementing Z. Feature X optimizes
    the handling of large datasets, reducing the computational complexity of the process. By implementing Z,
    we can achieve faster data processing and enhance the overall system efficiency.
    Example: This pull request fixes a critical bug in the user authentication process that was causing login
    failures. The fix involves correcting the token validation logic and updating the related error handling mechanisms.
    Example: This pull request refactors the data processing logic in module Z to improve code readability and
    maintainability. The refactoring includes restructuring the functions and adding comprehensive inline documentation.

Problem: Explain the problem that the pull request addresses in one paragraph containing no more than 4 sentences.
    Example: Currently, the system suffers from slow performance when handling large datasets. Feature X aims to
    mitigate this issue by optimizing Z.
    Example: There is a bug in the user authentication process that causes login failures for some users.
    Example: The data processing logic in module Z is overly complex and difficult to maintain, leading to frequent
    errors and increased development time.

Solution: Describe the solution and the key changes introduced in one paragraph containing no more than 4 sentences.
    Example: The solution involves adding a new algorithm for Z which reduces the computational complexity. This
    includes implementing the new algorithm in module A, refactoring module B to improve code maintainability,
    and updating existing tests and documentation.
    Example: The solution involves correcting the token validation logic and updating the error handling mechanisms.
    This includes fixing the token validation function in module C, adding new unit tests to cover edge cases,
    and updating the user authentication documentation.
    Example: The solution involves restructuring the functions in module Z and adding inline documentation. This
    includes breaking down complex functions into smaller, more manageable ones, adding detailed comments and
    docstrings, and refactoring the error handling logic for better clarity.

Design: Describe the design and architecture considerations in one paragraph containing no more than 8 sentences.
    Example: The design includes a modular approach, where the new algorithm is encapsulated in a dedicated module,
    ensuring separation of concerns. The architecture leverages existing data processing pipelines, integrating the
    new functionality with minimal disruption to the existing workflow. Detailed diagrams and flowcharts are provided in
    the design documentation to illustrate the data flow and component interactions.
    Example: The design involves a layered architecture, where the token validation logic is separated into a service
    layer for better maintainability and testability. The architecture ensures that changes to the validation logic do
    not impact other parts of the system, promoting a clear separation of concerns. Documentation includes sequence
    diagrams to illustrate the authentication flow.
    Example: The design focuses on improving code readability and maintainability by breaking down complex functions
    into smaller, well-documented components. The architecture includes a central error handling mechanism to streamline
    error management across the module. Diagrams and pseudocode are included to provide a clear overview of the
    refactored design.

Impact: Describe the potential impact of the changes on the system and its users in one paragraph containing no more
than 4 sentences.
    Example: These changes are expected to improve data processing speed by 50%, benefiting users who handle large
    datasets.
    Example: This fix will ensure that all users can log in successfully, improving the overall user experience.
    Example: The refactored code will be easier to maintain and extend, reducing the likelihood of future bugs and
    speeding up development time.

Testing: Describe the testing strategy and results. If no tests have been added or modified, just print the title and do
 not include the contents of this section.
    Example: Added unit tests for the new feature. Conducted performance testing on large datasets. All tests pass with
    significant performance improvements observed.
    Example: Added unit tests to cover the corrected token validation logic. Conducted integration testing to ensure the
     fix works across different scenarios. All tests pass successfully.
    Example: Added comprehensive unit tests for the refactored functions. Conducted regression testing to ensure no
    existing functionality is broken. All tests pass with no issues.

Documentation: Note any updates to documentation. If no documentation has been added or modified, just print the title
and do not include the contents of this section.
    Example: Updated the README and added a new section to the user guide detailing feature X.
    Example: Updated the user authentication documentation to reflect the changes in token validation logic.
    Example: Added detailed inline comments and docstrings in module Z to improve code readability.

Breaking Changes: Identify any potential breaking changes that the pull request may introduce. If there are no clear
breaking changes, just print the title and do not include the contents of this section.
    Example: The new algorithm in module A may change the output format, which could affect downstream processes relying
    on the previous format.
    Example: Correcting the token validation logic might invalidate existing tokens, requiring users to log in again.
    Example: Restructuring functions in module Z may break compatibility with existing scripts and tools that depend on
    the old function signatures.

Known Issues or Limitations: Mention any known issues or limitations with the current implementation. If there are no
clear issues or limitations, just print the title and do not include the contents of this section.
    Example: There may be minor performance issues when handling extremely large datasets beyond the current test scope.
    Example: Some edge cases in the user authentication process are not fully covered and may require further testing.
    Example: The refactored code may have compatibility issues with older versions of the dependent libraries.

Added Files: List all of the newly added files and provide a short summary of the contributions of each file. Only
include newly added files in this list.
    Example:
        - File A: Added a new X module in the Y package to encapsulate the Z functionality.
        - File B: Introduced a new X module in the Y package to manage Z.
        - File C: Created a new X module in the Y package to handle Z.

Modified Files: List all of the files that were modified and provide a short summary of the modifications in each file.
Do not include newly added files or files that have been removed from the repository in this list.
    Example:
        - File A: Implemented the new algorithm for Z.
        - File B: Refactored code for better maintainability.
        - File C: Updated unit tests to cover new features.
        - File D: Improved error handling and added logging.

Removed Files: List all of the files that were removed from the repository. Do not include newly added files or files
that have been modified in this list.

Additional Notes: Include any additional context or information relevant to the pull request.
    Example: There was some refactoring involved that extended to changes in files X and Y.
    Example: Requires installation of the X package.
    Example: Ensure database is migrated before testing.

Notes to Reviewer: Include important points for the reviewers to consider.
    Example: Please pay close attention to the changes in module B, as they might affect existing functionalities.
    Example: Verify the performance improvements by running code on a suitable test dataset.
    Example: Check the compatibility of the refactored code with older versions of the dependent libraries.

Here is the Git diff between branches '{branch1}' and '{branch2}':

{diff_content}
"""

def get_git_review(branch1: str, branch2: str, diff_content: str) -> str:
    return f"""You are a professional and experienced software engineer. Review the changes introduced in the Git diff
between branches '{branch1}' and '{branch2}', ensuring they adhere to software engineering best practices.

Git Diff:

{diff_content}

Your message should cover the following key areas:
1. Summary: Provide a clear and concise summary of the changes introduced in this diff.
2. Code Quality: Assess the overall quality of the changes, including readability, consistency, maintainability,
and adherence to coding standards.
3. Design Impact: Evaluate how the changes affect the design of the existing codebase, including modularity, separation
of concerns, and adherence to SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface
Segregation, Dependency Inversion), as well as the DRY (Don't Repeat Yourself) and YAGNI (You Aren't Gonna Need It)
principles.
4. Design Patterns: Identify any design patterns introduced or modified by the changes, evaluate their appropriateness,
and suggest any additional patterns that could improve the design.
5. Documentation: Review the documentation added or modified in the changes, including docstrings and comments, for
completeness, clarity, and adherence to documentation standards.
6. Error Handling: Examine how errors and exceptions are managed in the new or modified code.
7. Dependencies: Identify any new external libraries or modules introduced by the changes, and assess their necessity
and impact on the codebase.
8. Performance and Scalability: Analyze any potential performance issues or bottlenecks introduced by the changes, and
assess whether the changes are designed to handle increased load and scale effectively.
9. Security: Evaluate the changes for any potential security vulnerabilities or practices that could lead to security
issues.
10. Testing: Confirm that the changes are adequately tested, including unit tests, integration tests, and any other
relevant test coverage.

Provide detailed feedback on each point, referencing specific parts of the Git diff where necessary, and discuss the
overall strengths and weaknesses of the changes.
"""
