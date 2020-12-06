import socket
HOST = 'localhost'
PORT = 10000
def echo_server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            with open('trans_file', 'wb') as f:
                f.write(data)
        conn.send(b'successfully transfered')
    except Exception as e:
        print(e)
        s.send(b'failed')
    finally:
        conn.close()
if __name__ == '__main__':
    echo_server()
