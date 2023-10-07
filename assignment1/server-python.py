###############################################################################
# server-python.py
# Name:
# NetId:
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定套接字到地址和端口
    server_socket.bind(('127.0.0.1', server_port))
    # 监听客户端连接
    server_socket.listen(QUEUE_LENGTH)
    while 1:
        try:
            # 接受客户端连接
            client_socket, client_address = server_socket.accept()
            # 接收并处理客户端消息
            while 1:
                data = client_socket.recv(RECV_BUFFER_SIZE)
                if not data:
                    break
                try:
                    sys.stdout.write(data.decode())
                    sys.stdout.flush()
                except:
                    sys.stdout.buffer.write(data)
                    sys.stdout.flush()
        except socket.error as e:
            print("Error: {}".format(e))
        finally:
            client_socket.close()
    # 关闭服务器套接字
    server_socket.close()
    pass


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
