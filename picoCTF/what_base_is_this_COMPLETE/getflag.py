#! /usr/bin/python

from pwn import * 


def bin2str(binary_str, bits_per_char=8):
	str_data = ""
	for i in range(0, len(binary_str), bits_per_char): 
		temp_data = binary_str[i:i + bits_per_char]
		str_data += chr(int(temp_data, 2))
	return str_data
    

def hex2str(hexa_str):
    return hexa_str.decode("hex")


def oct2str(oct_str):
	res_string = ""
	oct_chars = oct_str.split(" ")
	for char in oct_chars:
		res_string += chr(int(bin(int(char, 8))[2:], 2))
	return res_string
   

host, port = "2018shell.picoctf.com", 1225
local = True
context.log_level="critical"

con = connect(host, port)

try:
	con.recvuntil("Please give me the")
	str_to_compute = con.recvuntil(" as").replace(" as", "").strip()
	con.recv()
	res_str = bin2str(str_to_compute.replace(" ", ""))
	# print(str_to_compute, res_str)
	con.sendline(res_str)

	con.recvuntil("Please give me the")
	str_to_compute = con.recvuntil(" as").replace(" as", "").strip()
	con.recv()
	res_str = hex2str(str_to_compute.replace(" ", ""))
	# print(str_to_compute, res_str)
	con.sendline(res_str)

	con.recvuntil("Please give me the")
	str_to_compute = con.recvuntil(" as").replace(" as", "").strip()
	con.recv()
	res_str = oct2str(str_to_compute)
	# print(str_to_compute, res_str)
	con.sendline(res_str)
	
	last_str = con.recvuntil("Flag:")
	flag = con.recv().strip()
	print(flag)
except Exception as e:
	print e

con.close()
