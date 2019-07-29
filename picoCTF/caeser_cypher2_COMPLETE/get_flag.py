#! /usr/bin/python

from pwn import *
import string as s

ciphertext = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"
# using the order in the ascii table
alphabet = "!\"#%&\'()*+,-./" + s.digits + "/:;<=>?@" + s.uppercase + "[]^`_" + s.lowercase + "|{~}"

def caeser(text, rotation):
	result = ""
	for c in text:
		result+=alphabet[(alphabet.find(c)+rotation) % len(alphabet)]
	return result

ts = "picoCTF\{coisas\}"

i = 60
print caeser(ciphertext, i)

# closest match:
# i=29 PICO$5'\C"ESA3?$I1H&R4?JU45?A3&N5?S&C6R&^
# removed '$' from alphabet.
# closest match: 
# i=60 ohbnCTF{bAdr`R_ChPgEqS_itST_`REmT_rEbUqE}
# removed "\\"
# 60 picoCTF|cAesaR`CiPhErS`juST`aREnT`sEcUrE~
# now was just a matter of fixing the alphabet, changing special chars from place
