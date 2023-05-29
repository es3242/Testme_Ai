from email import message
import socket
import json

host = '127.0.0.1'
port =5050
Text_based_PDF = [['as'],['fgd']]

query = Text_based_PDF

mySocket = socket.socket()
mySocket.connect((host,port))

json_data = {
    'pdf' : query,
    'pages' : len(query),
    'reqType' : "TEST",
}

#데이터 보냄

message = json.dumps(json_data)
mySocket.send(message.encode())

#데이터 받음

data = mySocket.recv(2048).decode()
ret_data = json.loads(data)
print("답변: ")
print(ret_data['Answer'])
# print('/n')

mySocket.close()

