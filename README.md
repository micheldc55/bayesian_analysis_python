# Bayesian Analysis Python

Repository on Bayesian Analysis / Inference based on the Book: Bayesian Analysis with Python

## Project Setup Guide

This guide will walk you through setting up and running the Python environment required for this project.

### Prerequisites

Python 3.11: Ensure that Python 3.11 or higher is installed on your system.
Git (optional): If you plan to clone the repository, make sure Git is installed.

### Setup Instructions

#### Step 1: Clone the Repository (if applicable)

If you're starting from a Git repository, clone it using the following command:

```bash
git clone https://github.com/micheldc55/bayesian_analysis_python.git
cd bayesian_analysis_python
```

#### Step 2: Navigate to the env Directory

Change your directory to the env folder inside the project:

```bash
cd env
```

#### Step 3: Run the Setup Script

Run the provided Bash script to set up or activate the Python environment:

```bash
bash setup_env.sh
```

**What the Script Does:**

- Environment Check: The script checks if a virtual environment already exists in the env directory.
- Environment Creation: If the environment doesn't exist, it creates one using Python's venv module.
- Package Installation: The script then installs all the necessary Python packages specified in the requirements.txt file.
- Environment Activation: Finally, the script activates the environment, making it ready for use.
  
#### Step 4: Deactivate the Environment (Optional)

When you're done working, you can deactivate the virtual environment by running:

```bash
deactivate
```