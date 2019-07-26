#! /usr/bin/python

from pwn import *
from re import findall


# after reversing the binary we found this buffer
sekrut_buffer = bytearray([0x29, 0x6, 0x16, 0x4F, 0x2B, 0x35, 0x30, 0x1E, 0x51, 0x1B, 0x5B, 0x14, 0x4B, 0x8, 0x5D, 0x2B, 0x5C, 0x10, 0x6, 0x6, 0x18, 0x45, 0x51, 0x0, 0x5D, 0x0])

greeting = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"

deciphered_text = xor(sekrut_buffer, greeting[:len(sekrut_buffer)])

flag = findall(r"picoCTF{.*}",deciphered_text)[0]

print flag

