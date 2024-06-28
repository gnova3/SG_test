
# Instructions to Run the test

This document provides the necessary steps to set up and run the project in your local environment.

## Folder Contents

- `requirements.txt`: File listing the test dependencies.
- `stress_test`: Script to generate a user interacting with SG.
- `multi_test`: Script to run several stress_test.
- `chromedriver`: Selenium WebDriver driver for Chrome.

## Steps to Setup and Run the Project

### 1. Create a Virtual Environment with Python 3.10

Ensure you have Python 3.10 installed on your system. Then, create a virtual environment for this project.

### 2. Install Dependencies

Activate the virtual environment you just created and install the project dependencies from `requirements.txt`

```bash
source myenv/bin/activate  # Activate virtual environment on Linux/Mac
pip install -r requirements.txt
```

### 3. Requirement: Chrome Installed on Your PC

This project requires Google Chrome to be installed on your local laptop. The `chromedriver` file is essential for automation with Selenium. 

### 4. Run `multi_test`

Once all dependencies are installed and Chrome is available on your PC, you can run the `multi_test` script:

```bash
python multi_test.py
```

This script will perform multiple tests according to the number of cores.

---




