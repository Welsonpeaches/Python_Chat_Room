import socket
from threading import Thread


SERVER_IP = "127.0.0.1"
PORT = 8888

client_list = []




# 处理客户端通信的方法
def client_thread(conn):
    while True:
        data = conn.recv(81920)
        if not data:
            break
        else:
            print((data.decode()))

            for c in client_list:
                c.sendall(data)





# 1.实例化一个 socket
ss = socket.socket()

# 2.绑定 ip 和 端口
ss.bind((SERVER_IP, PORT))
print("服务器已启动。")

# 3.开始侦听
ss.listen(6)
print(f"服务器开始侦听：{SERVER_IP}:{PORT}")

# 4.接收客户端, 没接收一个客户端, 就产生一个新的 socket
#   使用这个新的 socket 来和服务器通信
while True:
    conn, addr = ss.accept()  # 阻塞方法
    print(f"一个用户已连接：{addr}")
    client_list.append(conn)

    t = Thread(target=client_thread,
             args=(conn,),
             daemon = True)
    t.start()



# while True:
#     data = conn.recv(1024)
#     print(data.decode())
#
#     if data.decode() == "/boom":
#         time.sleep(1)
#         time.sleep(1)
#         time.sleep(1)
#         time.sleep(1)
#         time.sleep(1)
#         break
