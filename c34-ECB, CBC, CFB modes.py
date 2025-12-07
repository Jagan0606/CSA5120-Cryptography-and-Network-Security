# q34_modes_padding.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
key = b'0123456789ABCDEF'
iv = b'1234567890ABCDEF'
msg = b'TWOBLOCKS16BYT'  # 16 bytes exactly

# Pad always
padded = pad(msg, 16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(padded)
print("Ciphertext (CBC):", ct)

# On receive, unpad to get original msg
dec = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
print("Recovered (after unpad):", unpad(dec,16))
