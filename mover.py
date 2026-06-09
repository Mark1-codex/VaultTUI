import sys, os
initloc = sys.argv[1]
print("Enter new path of the file (path with name):")
newpath = input(" > ")
os.system(f"mv {initloc} {newpath}")