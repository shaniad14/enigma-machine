#uCipher Program 

SHIFT = 3  # how many letters to move


# removes extra spaces
def clean_input(text):
    return text.strip()


# encrypts the message
def encrypt(message_list):
    result = []


    for char in message_list:
        if char.isalpha():  # only change letters
            new_char = chr(ord(char) + SHIFT)
            result.append(new_char)
        else:
            result.append(char)  # keep spaces/punctuation

    return "".join(result)

    # decrypts the message
def decrypt(message_list):
    result = []

    for char in message_list:
        if char.isalpha():
            new_char = chr(ord(char) - SHIFT)
            result.append(new_char)
        else:
            result.append(char)

            return "".join(result)


# main part of program
def main():
    choice = input("Encrypt or Decrypt (E/D): ").strip().lower()

    message = input("Enter message: ")
    message = clean_input(message)

    message_list = list(message)  # turn into list

    if choice == "e":
        result = encrypt(message_list)
        print("Encrypted:", result)
    else:

     result = decrypt(message_list)
     print("Decrypted:", result)



