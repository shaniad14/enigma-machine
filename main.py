SHIFT = 3  # how many letters to move



# removes extra spaces
def clean_input(text):
    return text.strip()


# encrypts the message
def encrypt(message_list):
    result = []

    for char in message_list:
        if char.isalpha():  # only change letters
            # FIX: proper Caesar shift (wrap around alphabet)
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + SHIFT) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)  # keep spaces/punctuation

    return "".join(result)


# decrypts the message
def decrypt(message_list):
    result = []

    for char in message_list:
        if char.isalpha():
            # FIX: proper reverse shift
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - SHIFT) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)  # FIX: moved outside loop


# main part of program
def main():
    print("=== Cipher Program ===")
    print("This program can encrypt or decrypt your message.\n")

    choice = input("Encrypt or Decrypt (E/D): ").strip().lower()

    message = input("Enter message: ")
    message = clean_input(message)

    # OPTIONAL (to show dictionary use)
    data = {"message": message}

    message_list = list(data["message"])  # turn into list

    if choice == "e":
        result = encrypt(message_list)
        print("Encrypted message:", result)

    elif choice == "d":
        result = decrypt(message_list)
        print("Decrypted message:", result)

    else:
        print("Invalid choice. Please enter E or D.")


# FIX: proper program start
if __name__ == "__main__":
    main()


