#! /usr/bin/python

# converted assembly to python

"""
.intel_syntax noprefix
.bits 32
	
.global asm2

#  asm2(0x6,0x28)

asm2:
	push   	ebp
	mov    	ebp,esp 					# ebp = esp
	sub    	esp,0x10 					# esp -= 10
	mov    	eax,DWORD PTR [ebp+0xc] 	# eax = 0x28
	mov 	DWORD PTR [ebp-0x4],eax 	# ebp-4 = eax = 0x28
	mov    	eax,DWORD PTR [ebp+0x8] 	# eax = 0x6
	mov	DWORD PTR [ebp-0x8],eax 		# ebp-8 = 0x6
	jmp    	part_b 						# JUMP
part_a:									# *** LOOP ***
	add    	DWORD PTR [ebp-0x4],0x1 	# ebp-0x4(0x28) += 1
	add	DWORD PTR [ebp+0x8],0x8f 		# ebp+0x8
part_b:	 				
	cmp    	DWORD PTR [ebp+0x8],0x8f90	# ebp+8 == 0x8f90
	jle    	part_a  					# JUMP(loop), ebp+8(0x6) < 0x8f90
	mov    	eax,DWORD PTR [ebp-0x4]		# save ebp-0x4 to return (eax)
	mov	esp,ebp
	pop	ebp
	ret 								# return eax

asm2(0x6,0x28)

"""

invar1 = 0x6
invar2 = 0x28

eax = invar2
ret_var = eax
eax = invar1

ebp_minus0x8 = eax


# cycle condition
while invar1 <= 0x8f90:
	ret_var +=1
	invar1 += 0x8f

eax = ret_var
print(hex(eax)) # 0x129