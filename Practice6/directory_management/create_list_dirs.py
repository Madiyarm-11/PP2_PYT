import os

# Create directory
os.mkdir("test_dir")

# Create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)

# Current directory
print("Current dir:", os.getcwd())

# List files
print("Files:", os.listdir())