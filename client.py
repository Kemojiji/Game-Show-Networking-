import socket
import random


HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = "104.255.13.91"
DISCONNECT_MESSAGE = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) #first need to send the length of the message
    send_length += b' ' * (HEADER - len(send_length)) #make sure how many 64 bits in send
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# send("Received a message from client")

win = "1"
lose = "0"

def main():

    print("Welcome to Tango Game")
    choose = int(input("We have three briefcases but only one of the briefcase has the prize."
                       "Now, you can choose one of briefcase to win the prize by entering numbner <1> or <2> or <3>"))

    number = random.randint(1, 3)

    if choose == number:
        if choose == 1:
            drop = random.randint(2, 3)
            swith =swith_afterdrop (choose, drop)

        elif choose == 2:
            list_1 = [1, 3]
            # Remove random element from list
            list_1.pop(random.randrange(len(list_1)))
            drop = list_1[0]
            swith = swith_afterdrop(choose, drop)

        elif choose == 3:
            drop = random.randint(1, 2)
            swith = swith_afterdrop(choose, drop)

    else: # choose != number
        list_2 = [1,2,3]
        for i in range (len(list_2)):
            if list_2[i] != choose and list_2[i] != number:
                drop = list_2[i]

        swith = number


    choose_second = input("Now the host going to eliminating a empty briefcase to increase Probability of winning."
                          "The elinated empty briefcase is " + str(drop) + ", your current choose is " + str(choose) +
                          ", do you want swith to " + str(swith) + " by entering <Y> or <N>")

    if choose_second == "Y":
        choose = swith

    if choose == number:
        print("You win!")
        send(win)

    else:
        print("Try next time!")
        send(lose)

def swith_afterdrop (choose, drop):
    list_3 = [1, 2, 3]
    list_3.pop(list_3.index(choose))
    list_3.pop(list_3.index(drop))

    s = list_3[0]
    return s

main()

send(DISCONNECT_MESSAGE)