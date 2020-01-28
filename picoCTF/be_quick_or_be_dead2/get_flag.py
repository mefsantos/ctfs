#! /usr/bin/python

from pwn import *
import re
import os

context.log_level = "critical"
# from https://www.bigprimes.net/archive/fibonacci/1026/
key = 11798692818055232550147578884125865608089028544560913468519228968187430794620907976123201977895385245239705082830656904630178314159866370495211539023461052682811230321796555930907722724384131648527339458407317543768

elf = ELF("./be-quick-or-be-dead-2")

# we can check the symbols and addresses
# for key, address in elf.symbols.iteritems():
# 	print key, hex(address)

# exit()

# patch the binary to:
# first remove the alarm - replace the instruction from set_timer() 
# to return before setting the 3 seconds alarm
elf.asm(elf.symbols["alarm"], "ret")

# to avoid waiting the fib sequence to be calculated we can set the value of the 
# key (fib(0x402)) to the register that is used for functions parameters(eax)
# which is the one used by decrypt_flag(key). also we want to 'pack' the key into
# a value that caan fit into the (32bit) register. so we can do : & 0xFFFFFFFF
elf.asm(elf.symbols["calculate_key"], "mov eax,%s\nret\n" % (hex(key & 0xFFFFFFFF)))

elf.save("./new")

# mark as executable
os.system("chmod +x new")

# now just run the file and cat the flag
p = process("./new")
flag = re.findall(r"picoCTF{.*}", p.recv())[0]

print flag
p.close()