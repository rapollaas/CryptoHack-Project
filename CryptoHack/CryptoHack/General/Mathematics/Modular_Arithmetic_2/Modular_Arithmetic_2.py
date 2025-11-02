# values given in the question
a = 273246787654
p = 65537

# fermats little theorum says a^p−1 ≡ 1 (mod p)
# every number from 1 to p - 1 has a multiplicative inverse mod p
n = pow(a, p-1, p)

# print answer and pick smaller one
print(n)
