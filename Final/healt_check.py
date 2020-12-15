#!/usr/bin/env python3

import psutil
import socket
import emails

# Need to monitor:
# - CPU usage percentage
# - Available disk space percentage
# - Available memory
# - "localhost" can be resolved to "127.0.0.1"

cpu_limit = 80.0            # 80% usage
disk_limit = 80.0           # 80% usage
memory_limit = 5*1024*1024  # 500 MB available

def check_cpu():
    if psutil.cpu_percent(interval=1) > cpu_limit:
        send_alert("Error - CPU usage is over 80%")

def check_disk_space():
    if psutil.disk_usage("/").percent > disk_limit:
        send_alert("Error - Available disk space is less than 20%")

def check_memory():
    if psutil.virtual_memory().available < memory_limit:
        send_alert("Error - Available memory is less than 500MB")

def check_network():
    localhost = socket.gethostbyname('localhost')
    if localhost != "127.0.0.1":  
        send_alert("Error - localhost cannot be resolved to 127.0.0.1")

def send_alert(subject):
    message = emails.generate_error_report(subject)
    emails.send_email(message) 

def main():
    check_cpu()
    check_disk_space()
    check_memory()
    check_network()


if __name__ == "__main__":
    main()