"""
1 2 3 4 5
A B C D E
F G H I J 
L M N O P 
Q R S T U 
V W Z Y Z

4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5
"""

cipher_matrix = [[], [[], "A", "B", "C", "D", "E"],
				 	 [[], "F", "G", "H", "I", "J"],
				 	 [[], "L", "M", "N", "O", "P"],
				 	 [[], "Q", "R", "S", "T", "U"],
				 	 [[], "V", "W", "Z", "Y", "Z"]
				]

if __name__ == "__main__":
	in_text = "1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}"

	in_text_list = in_text.split(",")

	res = ""
	for c in in_text_list:
		if c == "{" or c == "}" or c == "_":
			res += c
		else:
			ixs = c.split("-")
			print ixs
			i, j = ixs[0], ixs[1]
			dec_char = cipher_matrix[int(i)][int(j)]
			res += dec_char

	print res