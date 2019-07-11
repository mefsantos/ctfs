def get_numb2():
	for v in range(0, 0xffffff):
		if (((v & 0xff) == 0x0) and ((v >> 12) == 0) and ((v >> 8 ^ 0xf) == 0x4)):
			print("we got one!")
			print(v)
			break
	pass
 
print("coiso")
 
#get_numb2()


def get_numb_4_1():
	
	for n in range(0, 555555555):
		original_n = n
		n2 = n % 10
		n /= 10
		n3 = n % 10
		n /= 10
		if not (n3 % 2 != 0):
			continue
		if not (n2 != n3 / 2 * 3):
			continue
		for i in range(0,3):
		    if (n % 10 != n2):
		        continue
		    n /= 10
		    if (n % 10 != n3):
		        continue

		    n /= 10;
	
		if ((n == 0) and ((n2 % 2) != 0) and ((n2 ^ n3) == 0xF)):
			print("We got it...")
			print(original_n)
			exit(1)			
		


def get_numb_4_2():
	
	for n in range(555555555, 999999999):
		original_n = n
		n2 = n % 10
		n /= 10
		n3 = n % 10
		n /= 10
		if not (n3 % 2 != 0):
			continue
		if not (n2 != n3 / 2 * 3):
			continue
		for i in range(0,3):
		    if (n % 10 != n2):
		        continue
		    n /= 10
		    if (n % 10 != n3):
		        continue

		    n /= 10;
	
		if ((n == 0) and ((n2 % 2) != 0) and ((n2 ^ n3) == 0xF)):
			print("We got it...")
			print(original_n)
			exit(1)			
			#break
			

get_numb_4_1()	
get_numb_4_2()	
