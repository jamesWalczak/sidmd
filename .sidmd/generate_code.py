from openai import OpenAI
import os
import sys

ai_api_key = os.getenv("AI_API_KEY")

def ask_chatgpt(usage, load, structure=''):

  client = OpenAI(api_key=ai_api_key)

  if usage == "feature":
    load = 'From now on, you are a code generator. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Implement a feature according to the following description:' + load + 'Make comments in the code to improve understanding of the changes. You are allowed to create new files and add to the existing ones. it is of great importance that the response is in the same format as the list of files ("path" and "content" are placeholders for actual values) {"path": "content", "path": "content", ...}, as it will afterwards be turned into a JSON format. Use the line break character instead of multiline. Here is the file structure: ' + structure
  elif usage == "initiation":
    load = "From now on, you are a code generator. You are generating .sh files. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Response in a way that will make console execute your output." + " " + load
  elif usage =="bug":
    load = 'From now on you are a code repair tool. Analyse the file or files given. Propose fixes according to the description. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Response in a way that will make console execute your output. Description: ' + load + 'Make comments in the code to improve understanding of the changes. You are allowed to create new files and add to the existing ones. it is of great importance that the response is in the same format as the list of files ("path" and "content" are placeholders for actual values) {"path": "content", "path": "content", ...}, as it will afterwards be turned into a JSON format. Use the line break character instead of multiline. Here is the file structure: ' + structure
  elif usage == "validation":
    load = "From now on, you are a code generator. You prepare json files in a text format. In your response, avoid additional text, other than the code itself and send it in a plain format, instead of markdown. skip the indication of the language and ``` as well. Please correct the text below, so that it contains a valid JSON." + load
  completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "user", "content": load}]
  )

  return completion.choices[0].message.content

if __name__ == "__main__":
  print(ask_chatgpt(sys.argv[1], sys.argv[2], sys.argv[3]))
