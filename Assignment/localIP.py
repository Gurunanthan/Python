import socket
def get_local_ip_addresses():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip
if __name__ == "__main__":
    local_ip = get_local_ip_addresses()
    print(f"Local IP Address: {local_ip}")
