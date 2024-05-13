
# HTTPH4mm3r: HTTP Flood Script

HTTPH4mm3r is a Python-based script designed for educational purposes to simulate HTTP flood attacks as a part of network security training. It allows users to send multiple HTTP requests to a specified target URL to understand and analyze the impact of high traffic on web servers.

## Features

- **HTTP Flood Attack Simulation**: Simulate an HTTP flood attack by sending numerous requests to a target server.
- **Concurrent Requests**: Control the number of concurrent requests sent to the server.
- **Customizable Request Delay**: Set a delay between requests for each thread.
- **ASCII Art Interface**: Includes a unique ASCII art interface displaying script information and server health.
- **Command-Line Arguments**: Easily configure the script using command-line arguments.
- **Dummy/Fake Server Health Display**: Includes a simulated server health display for demonstration purposes, not reflecting actual server conditions.

## Warning

This tool is designed strictly for educational and testing purposes. Unauthorized use on servers that you do not own or do not have permission to test could be illegal.

## Requirements

- Python 3.x
- Modules: socket, threading, argparse, os, random, time, urlparse

## Usage

Run the script using Python and specify the necessary arguments:

```bash
python http_h4mm3r.py -u <TARGET_URL> [-c <CONCURRENT_REQUESTS>] [-p <PORT>] [-d <DELAY>]
```
## Screenshots

![test](https://github.com/Gadzhovski/HTTPH4mm3r/assets/93713208/234302d0-3626-489a-b938-ec131ebd9cf9)


Arguments:
- `-u` or `--url`: Target URL for the attack (required).
- `-c` or `--concurrent`: Number of concurrent requests (default: 2).
- `-p` or `--port`: Port of the target server (default: 80).
- `-d` or `--delay`: Delay between requests for each thread in seconds (default: 0).

## Example

```bash
python http_h4mm3r.py -u http://example.com -c 10 -d 0.1
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer

This tool is intended for educational and research purposes only. Any misuse of this software will not be the responsibility of the author or any affiliates.

