print("Hello, World!")

import os

directory = "build_run_test"
os.makedirs(directory, exist_ok=True)  # Creates the folder if it doesn't exist
print(f"Directory '{directory}' created successfully!")