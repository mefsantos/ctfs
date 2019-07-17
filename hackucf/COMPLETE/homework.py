from pwn import *
import re
import time 

sh=remote("ctf.hackucf.org", 10104)


_ = sh.recvuntil("return!")
first_val = -99
while True:
	if sh.can_recv():
		rem_line = sh.recv()
	
		if "flag{" in rem_line:
			print(rem_line)
			exit(0)
		expression = rem_line.strip().split("=")[0]
		print(expression)
		result = eval(expression)
		print(expression +"= "+str(result))
		sh.sendline(str(result))
else:
		time.sleep(0.1)	
		
