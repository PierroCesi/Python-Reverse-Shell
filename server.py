import socket

host = ""
port = 12800

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind((host, port))
connexion.listen(5)

print("listening on port ", port)

connexion_client, info_connexion = connexion.accept()
print("Client connected")


msg = ""
while msg != "end":
    msg = input()
    connexion_client.send(msg.encode('utf-8'))
    result = connexion_client.recv(1024).decode("utf-8")

    print(result)

print("Connexion closed")
connexion_client.close()
connexion.close()
