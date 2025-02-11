import json, re, sys

def find_branch_name(comments):
    comments_json = json.loads(comments)
    pattern = r'https://github\.com/[^/]+/[^/]+/tree/([^/]+)'

    for comment in comments_json:
        if ("The code has been successfully generated. Please review the changes in the latest commit of branch" in comment["body"]):
            match = re.search(pattern, comment["body"])
            return(match.group(1))

if __name__ == "__main__":
  branch_name=find_branch_name(sys.argv[1])
  print(branch_name)
