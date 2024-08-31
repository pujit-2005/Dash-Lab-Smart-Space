import psutil
import csv
import time
from ping3 import ping

# File to save the stats
output_file = "system_network_stats.csv"

# Headers for the CSV file
headers = [
    "Timestamp", "Process CPU Percent", "Process Threads", "Disk Read Bytes", 
    "Disk Write Bytes", "Network Bytes Sent", "Network Bytes Received", 
    "Network Packets Sent", "Network Packets Received", "Network Latency (ms)"
]

# Function to get system stats
def get_system_stats():
    # Process-related stats
    process = psutil.Process()
    cpu_percent = process.cpu_percent(interval=1)
    threads_count = process.num_threads()

    # Disk I/O stats
    disk_io = psutil.disk_io_counters()
    disk_read_bytes = disk_io.read_bytes
    disk_write_bytes = disk_io.write_bytes

    # Network I/O stats
    net_io = psutil.net_io_counters()
    net_bytes_sent = net_io.bytes_sent
    net_bytes_recv = net_io.bytes_recv
    net_packets_sent = net_io.packets_sent
    net_packets_recv = net_io.packets_recv

    # Network latency (Ping to a known IP, e.g., Google's public DNS)
    latency = ping("8.8.8.8") * 1000  # Convert to milliseconds

    return [
        time.strftime("%Y-%m-%d %H:%M:%S"), cpu_percent, threads_count, 
        disk_read_bytes, disk_write_bytes, net_bytes_sent, net_bytes_recv, 
        net_packets_sent, net_packets_recv, latency
    ]

# Write the stats to a CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    try:
        while True:
            # Gather system stats
            stats = get_system_stats()

            # Write the stats to the CSV file
            writer.writerow(stats)
            print(f"Logged stats: {stats}")

            # Sleep for a defined interval (e.g., 5 seconds)
            time.sleep(5)

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
