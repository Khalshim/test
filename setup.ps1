# Stop the script if any command returns an error
$ErrorActionPreference = "Stop"

# Step 1: Create a Python virtual environment
python -m venv .venv

# Step 2: Activate the virtual environment
# Depending on your Windows version and PowerShell settings, you might need to use a different command.
# This example assumes you are using PowerShell 7.0 or later.
.\.venv\Scripts\Activate.ps1

# Step 3: Install the Python module in development mode
pip install -e .
pip install .[ci]

# Initialize the repository
git init
git branch -M main
git add .
git commit -m "feat!: :tada: cookiecutter scaffold"

pre-commit install
