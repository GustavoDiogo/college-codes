alphabet_upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower_case = "abcdefghijklmnopqrstuvwxyz"

def encrypt(
    message = "MACHI NESCA NNOTT HINK",
    secret_key = "iamie xistt hatis cert"
):
    encrypted_message = ""
    
    if (len(secret_key) < len(message)):
        initial_secret_key_length = len(secret_key)

        for i in range(initial_secret_key_length, len(message)):
            if len(secret_key) < len(message):
                if (message[i] in alphabet_upper_case):
                    for j in range(0, len(message) - initial_secret_key_length):
                        secret_key += secret_key[j]
                else: secret_key += message[i]

    print(secret_key)

    for i in range(len(message)):
        if (message[i] in alphabet_upper_case):
            letter_secret_key_position = alphabet_lower_case.find(secret_key[i])
            secret_key_in_upper_case = alphabet_upper_case[letter_secret_key_position]

            encrypted_ascii = (ord(message[i]) + ord(secret_key_in_upper_case)) % 26
            encrypted_message += chr(encrypted_ascii + ord("a"))

        else: encrypted_message += message[i]

    print(encrypted_message)

encrypt()