__author__ = 'leena'

'''import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept() # c = connection , addr = address
    print("connection from : " +str(addr))
    while True:
          data = c.recv(1024)
          if not data:
                break
          print("from connected user :" + str(data))
          data = str(data).upper()
          print("sending :" + str(data))
          c.send(data)
    c.close()


if __name__ == '__main__':
    Main( )'''

#client
import socket
import threading
SIZE =4
class client(threading.Thread):
    def __init__(self,c):
        threading.Thread.__init__(self)
        self.conn = c
        self.stopIt = False

    def mrecv(self):
        data = self.conn.recv(SIZE)
        self.conn.send('OK')
        return self.conn.recv(int(data))

    def run(self):
        while not self.stopIt:
            msg = self.mrecv()
            print 'recieved-> ',msg

soc1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc1.connect(('127.0.0.1',5000))
soc1.send('WILL SEND') # telling server we will send data from here

soc2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc2.connect(('127.0.0.1',5000))
soc2.send('WILL RECV') # telling server we will recieve data from here

def msend(conn,msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)


thr = client(soc2)
thr.start()
try:
    while 1:
        msend(soc1,raw_input())
except:
    print 'closing'
thr.stopIt=True
msend(soc1,'bye!!') # for stoping the thread
thr.conn.close()
soc1.close()
soc2.close()
