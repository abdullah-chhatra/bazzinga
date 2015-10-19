__author__ = 'leena'

'''import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = raw_input(" -->")
    while message != 'q' :
        s.send(message)
        data = s.recv(1024)
        print("received from server : " + str(data))
        message = raw_input("->")
    s.close()

if __name__ == '__main__':
    Main()'''

#server
import socket
import threading
import time

SIZE = 4

soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(('127.0.0.1',5000))
soc.listen(5)
class CThread(threading.Thread):
    def __init__(self,c):
        threading.Thread.__init__(self)
        self.conn = c
        self.stopIt=False

    def mrecv(self):
        data = self.conn.recv(SIZE)
        self.conn.send('OK')
        msg = self.conn.recv(int(data))
        return msg

    def run(self):
        while not self.stopIt:
            msg = self.mrecv()
            print 'recieved->  ',msg

def setConn(con1,con2):
    dict={}
    state = con1.recv(9)
    con2.recv(9)
    if state =='WILL RECV':
        dict['send'] = con1 # server will send data to reciever
        dict['recv'] = con2
    else:
        dict['recv'] = con1 # server will recieve data from sender
        dict['send'] = con2
    return dict

def msend(conn,msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)


(c1,a1) = soc.accept()
(c2,a2) = soc.accept()
dict = setConn(c1,c2)
thr = CThread(dict['recv'])
thr.start()
try:
    while 1:
        msend(dict['send'],raw_input())
except:
    print 'closing'
thr.stopIt=True
msend(dict['send'],'bye!!!')# for stoping the thread
thr.conn.close()
soc.close()
