import sys
from pathlib import Path
path = Path(str(sys.argv[1]))
print("Enter search query:")
query = input(" > ")
foundfiles = []
for i in path.rglob("*"):
    name = i.name
    if name.startswith(query) or name.endswith(query):
        foundfiles.append(i)
for i in foundfiles:
    print(i)
print("Searching complete. Press CTRL+C to exit")
while True:
    pass
