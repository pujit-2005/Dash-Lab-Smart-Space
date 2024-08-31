import socket
import threading
import json
import google.generativeai as genai
import os

# Ensure that the API key is set as an environment variable
os.environ["API_KEY"] = "AIzaSyAOUiha5ea2d93-uZ2kyH1S7yio7qM3uxk"
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set.")

# Configure the API key
genai.configure(api_key=api_key)

def handle_client(client_socket):
    try:
        # Receive the prompt from the client
        prompt = client_socket.recv(1024).decode('utf-8')

        # Specify the model and generate content
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        # Send the response back to the client
        client_socket.send(response.text.encode('utf-8'))
    except Exception as e:
        client_socket.send(f"An error occurred: {e}".encode('utf-8'))
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))
    server.listen(5)
    print("Server is listening...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
