# take 1 away from prime numbers to make it coprime
p = 857504083339712752489993810777 - 1
q = 1029224947942998075080348647219 - 1

# get phi from multiplying together
modulo = p*q

# exponent value
exponent = 65537

# finding inverse of exponent. finds d key
n = pow(exponent, -1, modulo)

# prints answer
print(n)
