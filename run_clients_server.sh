#!/bin/bash

# Start the server
python3 server.py &


# Allow the server to start properly
sleep 2

# Launch multiple clients
for i in {1..5}
do
    python3 client.py &
done

wait
