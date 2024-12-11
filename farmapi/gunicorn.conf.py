import multiprocessing
import socket
import fcntl
import struct

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])

# bind = f"0.0.0.0:8000"
bind = f"{get_ip('eth0')}:8000"
print("BIND ============", bind)

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 2
preload = True
loglevel = "info"

