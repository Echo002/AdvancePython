import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        deal_data = data.decode("utf8")
        print(deal_data)
        if deal_data == 'exit':
            print("client close session!")
            break
        re_data = input()
        sock.send(re_data.encode("utf8"))
# 获取客户端发来的数据
# 一次获取1k的数据
while True:
    sock, addr = server.accept()
    # 用线程处理新接受的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))
    # server.close()
    # sock.close()