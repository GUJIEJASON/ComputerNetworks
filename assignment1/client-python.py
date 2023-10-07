###############################################################################
# client-python.py
# Name:
# NetId:
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # 连接到服务器
        client_socket.connect((server_ip, server_port))
        while True:
            message = sys.stdin.buffer.read(SEND_BUFFER_SIZE)
            # 检查是否达到EOF（文件结尾）
            if not message:
                break
            try:
                # 发送消息
                client_socket.sendall(message)
            except socket.error as e:
                print("Error: {}".format(e))
                break
    except socket.error as e:
        print("Error: {}".format(e))
    finally:
        # 关闭套接字
        client_socket.close()
    pass


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
