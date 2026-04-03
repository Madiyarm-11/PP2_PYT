import shutil
import os

# Move file
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")

shutil.move("sample.txt", "test_dir/sample.txt")
print("File moved")

# Copy back
shutil.copy("test_dir/sample.txt", "sample.txt")