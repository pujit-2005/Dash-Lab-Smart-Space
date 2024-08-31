import google.generativeai as genai
import os
import json

# Ensure that the API key is set as an environment variable
os.environ["API_KEY"] = "AIzaSyAOUiha5ea2d93-uZ2kyH1S7yio7qM3uxk"
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set.")

# Configure the API key
genai.configure(api_key=api_key)

try:
    # Specify the model you want to use
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Read prompts from the input file
    with open("input.txt", "r") as file:
        prompts = [line.strip() for line in file.readlines()]
    
    responses = []
    for prompt in prompts:
        # Generate content based on each prompt
        response = model.generate_content(prompt)
        responses.append(response.text)
    
    # Save the responses to output.json
    with open("output.json", "w") as outfile:
        json.dump(responses, outfile, indent=4)

    print("Responses saved to output.json")

except Exception as e:
    print(f"An error occurred: {e}")
