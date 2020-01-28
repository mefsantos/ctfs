#! /usr/bin/python

from pwn import *
from re import findall


# after reversing the binary we found this buffer
sekrut_buffer = bytearray([0x29, 0x06, 0x16, 0x4f, 0x2b, 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14, 0x4b, 0x08, 0x5d, 0x2b, 0x52, 0x17, 0x01, 0x57, 0x16, 0x11, 0x5c, 0x07, 0x5d, 0x00])

greeting = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"

deciphered_text = xor(sekrut_buffer, greeting[:len(sekrut_buffer)])

flag = findall(r"picoCTF{.*}",deciphered_text)[0]

print flag

