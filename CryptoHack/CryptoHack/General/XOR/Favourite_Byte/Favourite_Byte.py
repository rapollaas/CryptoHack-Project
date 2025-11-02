# given hex made into string since it needs to be decoded
xor = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# make hex into bytes. every 2 hex characters give the byte equivalent
xor = bytes.fromhex(xor)

# for loop every single-byte xor key is tried 0-255
for key in range(256):
	# creates bytes sequence from keys(b)
	# ^ xors the byte with the byte key 
	# for builds list of xor results 
	xor = bytes([b ^ key for b in xor])
	# if crypto is found when going through the keys it prints the message
	if b"crypto" in xor:
		# prints answer
		print(xor)
