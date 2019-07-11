#!/usr/bin/env python2

def encrypt(plaintext, key):

    ciphertext = []
    for i in xrange(0, len(plaintext)):
        ciphertext.append(ord(plaintext[i]) ^ ord(key[i%len(key)])) 

    return ''.join(map(chr, ciphertext))

decrypt = encrypt

'''
I'll give you a sample of how this works:

Plaintext: 
"Here is a sample. Pay close attention!"

Ciphertext: (encoded in hex)
2e0c010d46000048074900090b191f0d484923091f491004091a1648071d070d081d1a070848

Flag: (encoded in hex, encrypted with the same key)
0005120f1d111c1a3900003712011637080c0437070c0015
'''


# cipher + plain == key

# flag + key == plain flag
plaintext = "Here is a sample. Pay close attention!"
ciphertext = "2e0c010d46000048074900090b191f0d484923091f491004091a1648071d070d081d1a070848"
flag="0005120f1d111c1a3900003712011637080c0437070c0015"

if __name__ == '__main__':
	key = decrypt(ciphertext, plaintext)
	print(key.encode("hex"))
	flag = decrypt(flag,key)
	print(flag)

# DEBUG
#	ct = "my fummy phrase"
#	key = "superkey"
#	cipher = encrypt(ct, key)
#	print(cipher.encode("hex"))
#	nk = decrypt(cipher, ct)
#	print(nk)
#	nt = decrypt(cipher, nk)
#	print(nt)