import socket
def main():
    sock=socket.socket()
    sock.connect(('46.242.8.172', 7890))
    if sock == -1:
        exit()
    sent=input("Enter a phrase...\n")
    sent=sent.encode('utf-8')
    sock.send(sent)
    adat=(sock.recv(1024))
    adat.decode('utf-8')
    print(adat)
    sock.close()
if __name__=='__main__':
    main()
    exit()
