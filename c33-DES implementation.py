# q33_des_example.py
from Crypto.Cipher import DES
key = b'8bytekey'  # DES key is 8 bytes (56 bits + parity)
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'ABCDEFGH'  # 8 bytes
ct = cipher.encrypt(plaintext)
pt = cipher.decrypt(ct)
print("Plain:", plaintext)
print("Ciphertext:", ct)
print("Decrypted:", pt)
