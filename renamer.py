import sys, os
from pathlib import Path
initloc = sys.argv[1]
print("Enter new name:")
newname = input(" > ")
os.system(f"mv {initloc} {Path(initloc).parent / newname}")