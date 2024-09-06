import google.generativeai as genai
import os
import json


os.environ["API_KEY"] = "AIzaSyAOUiha5ea2d93-uZ2kyH1S7yio7qM3uxk"
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set.")


genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    

    with open("input.txt", "r") as file:
        prompts = [line.strip() for line in file.readlines()]
    
    responses = []
    for prompt in prompts:
        
        response = model.generate_content(prompt)
        responses.append(response.text)
    
    
    with open("output.json", "w") as outfile:
        json.dump(responses, outfile, indent=4)

    print("Responses saved to output.json")

except Exception as e:
    print(f"An error occurred: {e}")
