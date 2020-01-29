#! /usr/bin/python

from pwn import *
from Crypto.Util.number import inverse, long_to_bytes
import primefac
import time as t
import re

def phi(p, q):
	return (p-1) * (q-1)

context.log_level = "critical"

host, port ="2018shell.picoctf.com", 18148

con = remote(host, port)




if context.log_level != 50: # "critical"
	print("#### Q1")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
p = int(re.findall(r"p : (.*)", output)[0])
q = int(re.findall(r"q : (.*)", output)[0])
is_feasible = "Y" if primefac.isprime(p) and primefac.isprime(q) else "N"
con.sendline(is_feasible)
if is_feasible == "Y":
	con.recv()
	n = int(p)*int(q)
	con.sendline(str(n))


# t.sleep(0.5)
if context.log_level != 50:
	print("#### Q2")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
p = int(re.findall(r"p : (.*)", output)[0])
n = int(re.findall(r"n : (.*)", output)[0])

# we already have p
newp, q = primefac.factorint(n).keys()
is_feasible = "Y" if newp == p else "N"
con.sendline(is_feasible)

if is_feasible == "Y":
	con.recv()
	con.sendline(str(q))




# t.sleep(0.5)
if context.log_level != 50:
	print("#### Q3")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
e = int(re.findall(r"e : (.*)", output)[0])
n = int(re.findall(r"n : (.*)", output)[0])

## this takes to long and crashes...so we assume we cannot factorize it
# try:
# 	p, q = primefac.factorint(n).keys()	
# 	con.sendline("Y")
# 	con.recv()
# 	con.sendline(str(p)+"\n"+str(q))
# except:
# 	# unable to factorize n
# 	con.sendline("N")

con.sendline("N")



# t.sleep(0.5)
if context.log_level != 50:
	print("#### Q4")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
p = int(re.findall(r"p : (.*)", output)[0])
q = int(re.findall(r"q : (.*)", output)[0])
is_feasible = "Y" if primefac.isprime(p) and primefac.isprime(q) else "N"

con.sendline(is_feasible)
if is_feasible == "Y":
	totient_n = phi(p, q)
	con.recv()
	con.sendline(str(totient_n))



# t.sleep(0.5)
if context.log_level != 50:
	print("#### Q5")

output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
plaintext = int(re.findall(r"plaintext : (.*)", output)[0])
e = int(re.findall(r"e : (.*)", output)[0])
n = int(re.findall(r"n : (.*)", output)[0])
con.sendline("Y")
# want ciphertext
con.recvuntil(":")
ciphertext = pow(plaintext, e, n)
con.sendline(str(ciphertext))



t.sleep(0.5)
if context.log_level != 50:
	print("#### Q6")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
ciphertext = int(re.findall(r"ciphertext : (.*)", output)[0])
e = int(re.findall(r"e : (.*)", output)[0])
n = int(re.findall(r"n : (.*)", output)[0])
# want plaintext
# we can attack rsa if n is smaller than cipher text
is_feasible = "Y" if ciphertext >= n else "N"
con.sendline(is_feasible)

if is_feasible == "Y":
	print is_feasible
	# here we could try to factorize n, compute the totient(n) and the inverse of e to obtain the private key d:
	p, q = primefac.factorint(n).keys()
	d = inverse(e, phi(p, q))
	plaintext = pow(ciphertext, d, n)
	con.recv()
	con.sendline(str(plaintext))



if context.log_level != 50:
	print("#### Q7")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
q = int(re.findall(r"q : (.*)", output)[0])
p = int(re.findall(r"p : (.*)", output)[0])
e = int(re.findall(r"e : (.*)", output)[0])
# want d
# since 'd' = inverse(e, phi(p, q))
con.sendline("Y")
con.recv()
d = inverse(e, phi(p, q))
con.sendline(str(d))



# t.sleep(0.5)
# last computation
if context.log_level != 50:
	print("#### Q8")
output = con.recvuntil("IS THIS POSSIBLE and FEASIBLE? (Y/N):")
p = int(re.findall(r"p : (.*)", output)[0])
ciphertext = int(re.findall(r"ciphertext : (.*)", output)[0])
e = int(re.findall(r"e : (.*)", output)[0])
n = int(re.findall(r"n : (.*)", output)[0])
# want plain text. we should try to factorize n to extract q, compute phi and obtain with inverse of e mod phi
# we cannot factorize if with primefac: overflowError
# factors = primefac.factorint(n).keys()

# using factor db 
# later use pytohn requests to do this one:
# mq = "http://factordb.com/index.php?id=1100000001172306014"
# r1 = r.get(mq)
# r1.resposnse
# and parse the 'value' - try to remember the package to 
q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
con.sendline("Y")

con.recv()

d = inverse(e, phi(p, q))
plain = pow(ciphertext, d, n)

# we dont need to send the line, the answer will say the flag is the plain text
print long_to_bytes(plain)

#con.sendline(str(plain))
#print con.recv()

con.close()
