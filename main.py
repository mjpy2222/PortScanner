import socket
import sys

# Saving original stdout
original_stdout = sys.stdout


def port_scanner():
    target = input("What is your target?")
    sockets = socket.gethostbyname(target)
    print(f"Scanning {target} ({sockets})")

    for port in range(1, 65001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((sockets, port))
        if result == 0:
            # Redirect stdout to a file by appending with a new line
            with open("ports.txt", mode="a") as f:
                sys.stdout = f
                f.write(f"Port {port}: Open\n")

        sock.close()


port_scanner()
