from huggingface_hub import InferenceClient
import os
import sys
import json

ai_api_key = os.getenv("AI_API_KEY")

def ask_ai(usage, load, structure=''):

  #Define the AI connection
  client = InferenceClient(token=ai_api_key, model='google/gemma-2-27b-it')

  #The LLM response has to implement all four usage cases. Prompts can be slightly modified to accommodate needs a particular model, but be aware that significant changes might (and probably will) break the response system.
  if usage == "feature":
    load = 'From now on, you are a code generator. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Implement a feature according to the following description:' + load + 'Make comments in the code to improve understanding of the changes. You are allowed to create new files and add to the existing ones. it is of great importance that the response is in the same format as the list of files ("path" and "content" are placeholders for actual values) {"path": "content", "path": "content", ...}, as it will afterwards be turned into a JSON format. JSON has only one root, stick strictly to one root and then paths and content in it, just like a regular json. PLEASE USE ONE ROOT ELEMENT. Use the line break character instead of multiline. Here is the file structure: ' + structure
  elif usage == "initiation":
    load = "From now on, you are a code generator. You are generating .sh files. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Respond in a way that will make console execute your output." + " " + load
  elif usage =="bug":
    load = 'From now on you are a code repair tool. Analyse the file or files given. Propose fixes according to the description. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Response in a way that will make console execute your output. Description: ' + load + 'Make comments in the code to improve understanding of the changes. You are allowed to create new files and add to the existing ones. it is of great importance that the response is in the same format as the list of files ("path" and "content" are placeholders for actual values) {"path": "content", "path": "content", ...}, as it will afterwards be turned into a JSON format. JSON has only one root. Use the line break character instead of multiline. Here is the file structure: ' + structure
  elif usage == "validation":
    load = 'From now on, you are a code generator. You prepare json files in a text format. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Please correct the text below, so that it contains a valid JSON in a format of {"path": "content", "path": "content", ...} ("path" and "content" are placeholders for actual values).' + load

  #Make a request, ensure it returns only a text string.
  return client.text_generation(load, max_new_tokens=6400, temperature=0.4, top_p=0.7)

def verify_code(response):
    try:
        parsed_response = json.loads(response)
        return json.dumps(parsed_response)
    except json.JSONDecodeError:
        fixed_response = ask_ai("validation", response)

        if fixed_response is not None:
            try:
                parsed_fix = json.loads(fixed_response)
                return json.dumps(parsed_fix)
            except json.JSONDecodeError:
                pass

    raise ValueError("JSON could not be fixed and remains invalid.")

if __name__ == "__main__":
  if(sys.argv[1]=="initiation"):
    print(ask_ai(sys.argv[1], sys.argv[2], sys.argv[3]))
  else:
    print(verify_code(ask_ai(sys.argv[1], sys.argv[2], sys.argv[3])))
