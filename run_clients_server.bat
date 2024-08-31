@echo off
REM Start the server
start /B python server.py

REM Wait a few seconds to ensure the server is up
timeout /t 5 /nobreak

REM Start multiple clients
start /B python client.py
start /B python client.py
start /B python client.py
REM Add more client commands as needed

echo Server and clients started.
