alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter 26-letter substitution key: ").upper()

text = input("Enter plaintext: ").upper()
result = ""

for ch in text:
    if ch in alphabet:
        pos = alphabet.index(ch)
        result += key[pos]
    else:
        result += ch

print("Encrypted:", result)
