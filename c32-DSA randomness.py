# q32_dsa_demo.py
import random
p = 23  # tiny toy prime
q = 11
g = 2
x = 3  # private key
y = pow(g,x,p)

def sign(msg, k):
    r = pow(g, k, p) % q
    # s = (k^{-1} * (H(m) + x*r)) mod q ; use H(m)=msg mod q
    km_inv = pow(k, -1, q)
    s = (km_inv * ((msg % q) + x*r)) % q
    return (r,s)

m = 5
sig1 = sign(m, k=7)
sig2 = sign(m, k=9)
print("sig1:", sig1)
print("sig2:", sig2)

# If same k used twice, attacker can recover x:
k_same = 7
s1 = sign(6, k_same)[1]
s2 = sign(7, k_same)[1]
# extract x (toy algebra) - demonstration only
print("Signatures with same k leak info (reuse is dangerous).")
