#! /usr/bin/python

from pwn import *
import string as s

#ciphertext = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA" # old
ciphertext = "d]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q"
# using the order in the ascii table

old_alphabet = "!\"#%&\'()*+,-./" + s.digits + "/:;<=>?@" + s.uppercase + "[]^`_" + s.lowercase + "|{~}"
alphabet = "!\"#%&\'()*+,-./" + s.digits + ":/;<=>?" + s.uppercase + "[\\]^_`" + s.lowercase + "{|}"

def caesar(text, rotation):
	result = ""
	for c in text:
		result+=alphabet[(alphabet.find(c)+rotation) % len(alphabet)]
	return result

ts = "picoCTF\{coisas\}"

for i in range(0, len(alphabet)):
	res = caesar(ciphertext, i)
	# print "\n", i, ciphertext
	# print i, res
	# if i==12:
	# 	exit(0)

	if "pico" in res:
		print(re.findall(r"picoCTF{.*}", res)[0])
		exit(0)

# closest match:
# i=29 PICO$5'\C"ESA3?$I1H&R4?JU45?A3&N5?S&C6R&^
# removed '$' from alphabet.
# closest match: 
# i=60 ohbnCTF{bAdr`R_ChPgEqS_itST_`REmT_rEbUqE}
# removed "\\"
# 60 picoCTF|cAesaR`CiPhErS`juST`aREnT`sEcUrE~
# now was just a matter of fixing the alphabet, changing special chars from place


"""
recent solve:
closest matches: 
i = 12, pidoBTF|d@fsbR_BiP-DrS_juST_bRDnT_sDdUrD~

recent solution: i = 12
changing the special chars around we reached the solution
picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}

"""

