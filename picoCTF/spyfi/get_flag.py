#! /usr/bin/python

# ORIGINAL SOURCE CODE
from Crypto.Cipher import AES

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')


from pwn import *

local = False

host, port = "2018shell.picoctf.com", 37131

if local:

	welcome = "Welcome, Agent 006!"
	print welcome

	sitrep = raw_input("Please enter your situation report: ")
	message = """Agent,
	Greetings. My situation report is as follows:
	{0}
	My agent identifying code is: {1}.
	Down with the Soviets,
	006
	""".format( sitrep, agent_code )

	message = pad(message)
	print encrypt( """key""", message )

else:
	# we probably want to do a known plaintext attack on AES
	# take a look at https://zachgrace.com/posts/attacking-ecb/
	con = remote(host, port)

	con.recv()
	statur_report = ""
	con.sendline(status_report)
