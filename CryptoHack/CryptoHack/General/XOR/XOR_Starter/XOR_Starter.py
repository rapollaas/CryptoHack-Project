# make variable with string label
text = "label"

# for loop to turn each letter in label to ascii
for c in text:
	# XOR it with 13 and then turn it back into a character
	text+=chr(ord(c) ^ 13)

# print answer
print(text)
