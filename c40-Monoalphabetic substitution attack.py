 # Monoalphabetic Substitution Cipher – Frequency Attack (Easy Version)

from collections import Counter

# English letter frequency order (most → least)
freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext):
    ciphertext = ciphertext.upper().replace(" ", "")
    
    # Count frequency of letters in ciphertext
    count = Counter(ciphertext)
    
    # Sort cipher letters by frequency (high → low)
    sorted_cipher_letters = [item[0] for item in count.most_common()]
    
    # Map: most frequent cipher letter → most frequent English letter
    mapping = {}
    for i in range(len(sorted_cipher_letters)):
        mapping[sorted_cipher_letters[i]] = freq_order[i]
    
    # Generate plaintext guess
    guessed_plaintext = ""
    for c in ciphertext:
        guessed_plaintext += mapping.get(c, c)
    
    return guessed_plaintext, mapping

# ------------ MAIN PROGRAM ----------------

cipher = input("Enter ciphertext: ")

plaintext, mapping = frequency_attack(cipher)

print("\n===== Frequency Attack Result =====")
print("Guessed Plaintext:", plaintext)
print("\nLetter Mapping:")
for c in mapping:
    print(c, "→", mapping[c])
