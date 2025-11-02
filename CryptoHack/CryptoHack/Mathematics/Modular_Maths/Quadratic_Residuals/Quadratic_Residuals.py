# modulus
p = 29

# numbers that are going to be tested
ints = [14, 6, 11]

# made array that will store the square roots and residue that has square root
roots = []
resideue = 0

# for loop to get through every number in the list
for x in ints:
	# range to test from 0 to 28
	for i in range(p):
		#checks if i squared and mod 29 is x
		if(i*i) % p == x:
			# save the number that worked and save the range value that made it work
			residue = x
			roots.append(i)
# print the results
print(residue, roots)


