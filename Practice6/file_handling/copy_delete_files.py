import shutil
import os

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")
print("File copied")

# Backup file
shutil.copy("sample.txt", "backup_sample.txt")
print("Backup created")

# Append to file
with open("sample.txt", "a") as f:
    f.write("Appended line\n")

# Delete file safely
if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("File deleted")
else:
    print("File not found")