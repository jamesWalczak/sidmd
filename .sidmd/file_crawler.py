import os
import json
import argparse

def get_files(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")

    files = {}
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            files[os.path.abspath(os.path.join(root, filename))] = ""
    
    return files

def prepare_json(files):
  for file in files:
    with open(file, "r") as f:
      files[file] = f.read()
  return json.dumps(files)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--path", type=str, required=True)
  args = parser.parse_args()
  
  path = args.path.strip()
  files = prepare_json(get_files(path))
  print(files)