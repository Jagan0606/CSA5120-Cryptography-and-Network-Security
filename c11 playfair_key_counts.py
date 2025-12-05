# playfair_key_counts.py
import math

fact25 = math.factorial(25)
approx_pow2 = math.log2(fact25)
fact25_half = fact25 // 2
approx_pow2_half = math.log2(fact25_half)

print("25! =", fact25)
print("log2(25!) ≈", approx_pow2)
print("Approx: 25! ≈ 2^{%.2f}" % approx_pow2)
print()
print("If we divide by 2 (simple estimate for duplicate keys):")
print("25!/2 ≈ 2^{%.2f}" % approx_pow2_half)
