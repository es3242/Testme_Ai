from email import message
import socket
import json
from Blank_Fill.pdftotext_pdfminer import extract_text_pages


host = '127.0.0.1'
port =5050
Text_based_PDF = extract_text_pages('C:/Users/cpfld/Documents/GitHub/Testme_Ai/Blank_Fill/test.pdf')

while True:
    print("질문: ")
    query = input()
    if(query == "exit"):
        exit(0)
    print("-" * 40)

    mySocket = socket.socket()
    mySocket.connect((host,port))

    json_data = {
        'Query' : query,
        'BotType' : "TEST",
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)
    print("답변: ")
    print(ret_data['Answer'])
    # print('/n')

mySocket.close()

