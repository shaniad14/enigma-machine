#uCipher Program 

SHIFT = 3  # how many letters to move


# removes extra spaces
def clean_input(text):
    return text.strip()


# encrypts the message
def encrypt(message_list):
    result = []