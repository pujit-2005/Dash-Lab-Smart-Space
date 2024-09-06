import socket
import json

def send_prompt(prompt):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    client.send(prompt.encode('utf-8'))
    response = client.recv(4096).decode('utf-8')
    client.close()
    return response

if __name__ == "__main__":
  
    with open("input.txt", "r") as file:
        prompts = [line.strip() for line in file.readlines()]

    responses = []
    for prompt in prompts:
        response = send_prompt(prompt)
        responses.append({"Prompt": prompt, "Response": response})

  
    with open("client_output.json", "w") as outfile:
        json.dump(responses, outfile, indent=4)

    print("Responses saved to client_output.json")
