from pwn import *
import re
import time 

sh=remote("ctf.hackucf.org", 10101)


_ = sh.recvuntil("seconds!")
while True:
	if sh.can_recv():
		rem_line = sh.recv()
		#rem_line = sh.clean()
		if "flag{" in rem_line:
			print(rem_line)
			exit(0)
		print("received : " + rem_line)
		res = re.findall(r'\d+', rem_line)
		if len(res) != 0:
			sh.sendline(res[0])
			print("Sending : " + re.findall(r'\d+', rem_line)[0])
	else:
		time.sleep(0.1)	
		
		#time.sleep(0.3)


# when we get a shell
#sh.interactive()
