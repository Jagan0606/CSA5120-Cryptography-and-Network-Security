# Q18: Show how subkey bits are split into 24 + 24 bits

initial_key_56 = "1"*28 + "0"*28  # 56-bit simulated key

left_28 = initial_key_56[:28]
right_28 = initial_key_56[28:]

subkey_first_24 = left_28[:24]
subkey_last_24  = right_28[:24]

print("Left 28 bits      =", left_28)
print("Right 28 bits     =", right_28)
print("Subkey First 24   =", subkey_first_24)
print("Subkey Second 24  =", subkey_last_24)
