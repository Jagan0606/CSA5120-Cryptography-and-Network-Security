import math

n = 3599
plaintext = 59  # common factor with n
g = math.gcd(plaintext, n)

if g > 1:
    print("Yes! We can factor n because gcd =", g)
else:
    print("No help")
