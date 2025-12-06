# Q24 RSA: find p, q, d

n = 3599
e = 31

# factor n
for p in range(2, 100):
    if n % p == 0:
        q = n // p
        break

phi = (p-1)*(q-1)

# Find d such that (d*e) mod phi = 1
def egcd(a,b):
    if b==0: return a,1,0
    g,x,y = egcd(b, a%b)
    return g, y, x - (a//b)*y

g, x, y = egcd(e, phi)
d = x % phi

print("p =", p)
print("q =", q)
print("phi =", phi)
print("private key d =", d)
