# gdb debug script
from pwn import *

sh = process("./restrictedshell")

gdbscript = """
b *handle_connection+337
define hook-stop
x/100xw $esp
end
continue
"""
# script breakpoints don't work every time 
attach(sh)
sh.recv()
sh.sendline("prompt")
sh.recv()
sh.sendline("A"* 90)

# canary at: 0xffffd02b, value: 0x9170a100