import sys
import socket
import threading
from queue import Queue

queue = Queue()
open_ports = []
http_ports = []


def get_arguments():
    threads = 5
    target = None

    if len(sys.argv) == 3:
        threads = sys.argv[1]
        target = socket.gethostbyname(sys.argv[2])
    elif len(sys.argv) == 2:
        threads = 5
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid argument")
    return threads, target


def port_scanner(port):
    try:
        arguments = get_arguments()
        target = arguments[1]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_l):
    for port in port_l:
        queue.put(port)


def detect_http_server(open_port):
    """
    In this method just check by port 80 (default http)
    :param open_port: this parameter refers to a open port
    :return: True if the port passed by parameter is equal to 80, otherwise it returns False
    """
    return open_port == 80


def worker():
    while not queue.empty():
        port = queue.get()

        if port_scanner(port):
            if detect_http_server(port):
                print('Port HTTP server (default) {} is open'.format(port))
                http_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []
cant_threads = int(get_arguments()[0])

for t in range(cant_threads):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()


print('Open http ports: {}'.format(http_ports))
