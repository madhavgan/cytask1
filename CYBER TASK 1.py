def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetical characters are added as is
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    if choice in ['e', 'encrypt']:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice in ['d', 'decrypt']:
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid choice! Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
