import sys, os
from pathlib import Path
path_to_dir = sys.argv[1]
print("Enter creation type (fl - file; fd - folder):")
creation_type = input(" > ")
if creation_type == "fl":
    print("Enter file name:")
    file_name = input(" > ")
    os.system(f"touch {os.path.join(path_to_dir, file_name)}")
elif creation_type == "fd":
    print("Enter folder name:")
    folder_name = input(" > ")
    os.system(f"mkdir {os.path.join(path_to_dir, folder_name)}")
else:
    print()
sys.exit(0)