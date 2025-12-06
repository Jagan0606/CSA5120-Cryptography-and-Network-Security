# q28_diffie_hellman.py
import random
def powmod(a,b,m): return pow(a,b,m)

# small example (toy)
q =  0xF7  # 247 prime? (toy)
g = 5
# secrets
a = 6
b = 15
A = powmod(g,a,q)
B = powmod(g,b,q)
# shared keys
KA = powmod(B,a,q)
KB = powmod(A,b,q)
print("A sends:", A, "B sends:", B)
print("Shared keys equal?:", KA==KB, "Key:", KA)
