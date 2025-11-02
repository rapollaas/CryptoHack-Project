# make a function to find the gcd of 2 numbers
def gcd(a, b):
	#loop continues until b becomes 0
	while b != 0:
		# temporarily store the value of b
		temp = b
		# make b a mod b
		b = a % b
		# make a the previous b value
		a = temp
	# when b is 0 then a contains the gcd
	return a

# set values for x and y you want to find the gcd of
x = 66528
y = 52920

# print gcd of 2 picked out numbers
print("GCD is:", gcd(x, y))
