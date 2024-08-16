#!/bin/bash

# Define the directory for the virtual environment
ENV_DIR="../env"

# Check if the environment already exists
if [ -d "$ENV_DIR" ]; then
    echo "Activating the existing virtual environment..."
    source "$ENV_DIR/bin/activate"
else
    echo "Creating a new virtual environment..."
    python3 -m venv "$ENV_DIR"
    source "$ENV_DIR/bin/activate"
    echo "Installing required packages..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

echo "Environment is ready and activated!"
