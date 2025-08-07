import socket
import os

HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 12345))  # получаем порт от Render, иначе fallback на 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Listening on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("<<<", data.decode())
