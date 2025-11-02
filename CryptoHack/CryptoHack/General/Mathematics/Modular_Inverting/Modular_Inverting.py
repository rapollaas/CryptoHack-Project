# Fermat's little theorum
# p is prime and a % p cannot = 0
# divide by a
a = 3
p = 13

# get the inverse by a^(p-2) mod p. got it from a^(p-1) = 1 (mod p)
n = pow(a, p - 2, p)

# print answer
print(n)
