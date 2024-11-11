# Engineering Journal
## Date: 2024-11-11
**Summary**: Today, I worked on starting my Train Delay Notifier project. I completed the initial setup tasks and gained new insights into project management and environment handling.

### Details:

  - Set Up Project Structure:

      - Created the project folder structure using `mkdir` and `touch` commands to organize directories and files efficiently.
      - Established a Python-based project layout, including separate folders for `src`, `tests`, and configuration files.

  - Version Control Configuration:

      - Learned to troubleshoot GitHub account configurations in the terminal to ensure commits were made under the correct account.

  - Environment Management:

      - Implemented a `.env` file to securely store sensitive API keys. This helps in managing credentials without exposing them publicly in version control.

### **Challenges and Solutions:**

  - Challenge: Initial confusion over using the correct GitHub account in the terminal.
     - *Solution:* Updated global Git configuration using `git config --global user.email "myemail@example.com"` and `git config --global user.name "My Name"` to ensure it matched the main GitHub account.
  - Challenge: Understanding how to create and use a .env file for secure credential storage.
     - *Solution:* Researched best practices and applied `python-dotenv` to load environment variables in Python.

### **Key Learnings:**

  - The importance of a structured project layout for maintainability.
  - Managing different GitHub accounts on the terminal effectively.
  - Utilizing .env files to handle API keys and sensitive information securely.

### Next Steps:

  - Begin work on Issue #4: Setting up the API call to fetch train delay data.
  - Plan for writing unit tests for the implemented functions.
