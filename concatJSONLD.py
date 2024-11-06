import json
import glob

obj_out = []

json_files = glob.glob("*.jsonld")
print(len(json_files))

# Load each JSON file into a Python object.
for json_file in json_files:
    with open(json_file, "r") as f:
        obj_out.append(json.load(f))

# Dump all the Python objects into a single JSON file.
with open("openml.jsonld", "w") as f:
    json.dump(obj_out, f, indent=4)
