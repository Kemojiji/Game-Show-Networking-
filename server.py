import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

number_win = 0
number_lose = 0

def handle_client(conn, addr):  # handle all connection between client and server
    print(f" new connection{addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: #the first time masg can be none so if not none
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == "1":
                global number_win
                number_win +=1
            elif msg == "0":
                global number_lose
                number_lose +=1

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print("number of player win: " + str(number_win))
                print("number of player lose: " + str(number_lose))
                print("number of player played game: " + str(number_win + number_lose))

            print(f"[{addr}]{msg}")
            conn.send("Comfirmed from server ".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[listen] server is listenning on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")  # number of the thread running right now, -1 is beacuse the listennig

print("[starting] server is starting ..")

start()