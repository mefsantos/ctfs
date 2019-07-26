.intel_syntax noprefix
.bits 32
	
.global asm1

# input argument 0xc8 = 200
# ebp+0x8 (eax) : function argument, i.e., 200
			
asm1:												
	push	ebp						# ebp = stack
	mov	ebp,esp						# ebp = esp

#  stack look after the two operations
# 			+---------+
# 			| old ebp | <-- ebp
# 			+---------+
# 			| ret     | <-- ebp + 0x4
# 			+---------+
# 			| 0xc8    | <-- ebp + 0x8
# 			+---------+

	cmp	DWORD PTR [ebp+0x8],0x9a	# compare 154 with eax (200) 
	jg 	part_a 						# jump if greated (Jump Taken)
	cmp	DWORD PTR [ebp+0x8],0x8 	
	jne	part_b 						
	mov	eax,DWORD PTR [ebp+0x8] 	
	add	eax,0x3 					
	jmp	part_d 					
part_a: 							
	cmp	DWORD PTR [ebp+0x8],0x2c 	# compare 0x2c (44) with eax (200)
	jne	part_c 						# jump if not equal (JUMP TAKEN)
	mov	eax,DWORD PTR [ebp+0x8] 	
	sub	eax,0x3 					
	jmp	part_d 						
part_b: 							
	mov	eax,DWORD PTR [ebp+0x8] 	
	sub	eax,0x3 				
	jmp	part_d 				
	cmp	DWORD PTR [ebp+0x8],0xc8
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8] 	# mv ebp+0x8 (0xc8) to eax
	add	eax,0x3 					# eax(0xc8) += 3 = 0xcb
part_d:	
	pop	ebp							# pop the ebp 
	ret 							# return the value in eax (0xcb)


# What does asm1(0xc8) return? answer: 0xcb

# FLAG: 0xcb