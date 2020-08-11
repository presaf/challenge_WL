import sys
import socket


def port_scanner():
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid argument")
        raise Exception("Missing the argument")
    try:
        for port in range(1, 1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except socket.gaierror:
        print("Hostname Could not be resolved")
        sys.exit()


port_scanner()
