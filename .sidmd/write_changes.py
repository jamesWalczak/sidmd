import os
import json
import argparse

def write_changes(json_files):
  for key, value in json_files.items():
    os.makedirs(os.path.dirname(key), exist_ok=True)

    with open(key, "w") as file:
      file.write(value)
  return 

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--structure", type=str, required=True)
  args = parser.parse_args()

  if os.path.isfile(args.structure):
    with open(args.structure, 'r') as file:
      file_structure = json.load(file)
  else:
    file_structure = json.loads(args.structure)
  
  write_changes(file_structure)
