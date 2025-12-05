# Caesar Cipher Program

def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():             # check alphabet
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char             # keep spaces/symbols same
    return result

text = input("Enter text: ")
k = int(input("Enter shift (1-25): "))

encrypted = caesar_cipher(text, k)
print("Encrypted Text:", encrypted)
