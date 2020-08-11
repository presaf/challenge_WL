import random
import sys
import socket
import threading
from queue import Queue

queue = Queue()
open_ports = []


def get_arguments():
    threads = 5
    target = None
    ports_random = None

    if len(sys.argv) == 4:
        threads = sys.argv[1]
        target = socket.gethostbyname(sys.argv[3])
        ports_random = True if sys.argv[2] == 'f' else False
        check_flag_firewall(ports_random)
    elif len(sys.argv) == 3:
        threads = sys.argv[1]
        target = socket.gethostbyname(sys.argv[2])
    elif len(sys.argv) == 2:
        threads = 5
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid argument")
    return threads, target, ports_random


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


def worker():
    while not queue.empty():
        port = queue.get()

        if port_scanner(port):
            print('Port {} is open'.format(port))
            open_ports.append(port)


def check_flag_firewall(ports_random):
    if ports_random:
        port_list = random.sample(range(1024), 1024)
        fill_queue(port_list)
    else:
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

print('Open ports: {}'.format(open_ports))
