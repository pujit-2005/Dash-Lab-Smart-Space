#!/bin/bash

# Number of clients to launch
NUM_CLIENTS=3

# Function to start the server
start_server() {
    echo "Starting the server..."
    python server.py &
    SERVER_PID=$!
    echo "Server started with PID $SERVER_PID"
}

# Function to start clients
start_clients() {
    echo "Starting $NUM_CLIENTS clients..."
    for i in $(seq 1 $NUM_CLIENTS); do
        echo "Starting client $i..."
        python client.py &
        CLIENT_PIDS[$i]=$!
        echo "Client $i started with PID ${CLIENT_PIDS[$i]}"
    done
}

# Function to stop the server and clients
stop_all() {
    echo "Stopping all clients and the server..."
    for i in $(seq 1 $NUM_CLIENTS); do
        kill ${CLIENT_PIDS[$i]}
        echo "Client $i with PID ${CLIENT_PIDS[$i]} stopped."
    done
    kill $SERVER_PID
    echo "Server with PID $SERVER_PID stopped."
}

# Trap the script termination to ensure cleanup
trap stop_all EXIT

# Start the server
start_server

# Give the server some time to start (optional)
sleep 2

# Start the clients
start_clients

# Wait for all clients to finish (this script will keep running)
wait
