alphabet_upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower_case = "abcdefghijklmnopqrstuvwxyz"

def encrypt():
    will_write_message = input("Digite 1 para escrever sua mensagem ou 2 para usar o padrao(MACHI NESCA NNOTT HINK)?\n")

    if (will_write_message == "1"):
        message = str(input("Digite sua mensagem(sera transformada em caixa alta)\n"))
        message = message.upper()
    else: message = "MACHI NESCA NNOTT HINK"
    
    will_write_secret_key = input("Digite 1 para escrever sua chave ou 2 para usar o padrao(iamie xistt hatis cert)?\n")

    if (will_write_secret_key == "1"):
        secret_key = str(input("Digite sua chave(sera transformada em minusculo)\n"))
        secret_key = secret_key.lower()
    else: secret_key = "iamie xistt hatis cert"

    encrypted_message = ""

    if (len(secret_key) < len(message)):
        initial_secret_key_length = len(secret_key)

        for i in range(initial_secret_key_length, len(message)):
            if len(secret_key) < len(message):
                if (message[i] in alphabet_upper_case):
                    for j in range(0, len(message) - initial_secret_key_length):
                        secret_key += secret_key[j]
                else: secret_key += message[i]

    for i in range(len(message)):
        if (message[i] in alphabet_upper_case):
            letter_secret_key_position = alphabet_lower_case.find(secret_key[i])
            secret_key_in_upper_case = alphabet_upper_case[letter_secret_key_position]

            encrypted_ascii = (ord(message[i]) + ord(secret_key_in_upper_case)) % 26
            encrypted_message += chr(encrypted_ascii + ord("a"))

        else: encrypted_message += message[i]

    print("CIFRA: " + encrypted_message + "\n")

def decrypt():
    will_write_message = input("Digite 1 para escrever sua mensagem cifrada ou 2 para usar o padrao(uaopm kmkvt unhbl jmed)?\n")

    if (will_write_message == "1"):
        message = str(input("Digite sua mensagem cifrada(sera transformada em minusculo)\n"))
        message = message.lower()
    else: message = "uaopm kmkvt unhbl jmed"

    will_write_secret_key = input("Digite 1 para escrever sua chave ou 2 para usar o padrao(iamie xistt hatis cert)?\n")
    
    if (will_write_secret_key == "1"):
        secret_key = str(input("Digite sua chave(sera transformada em minusculo)\n"))
        secret_key = secret_key.lower()
    else: secret_key = "iamie xistt hatis cert"

    decrypted_message = ""

    if (len(secret_key) < len(message)):
        initial_secret_key_length = len(secret_key)

        for i in range(initial_secret_key_length, len(message)):
            if len(secret_key) < len(message):
                if (message[i] in alphabet_upper_case):
                    for j in range(0, len(message) - initial_secret_key_length):
                        secret_key += secret_key[j]
                else: secret_key += message[i]

    for i in range(len(message)):
        if (message[i] in alphabet_lower_case):
            letter_secret_key_position = alphabet_lower_case.find(secret_key[i])
            secret_key_in_upper_case = alphabet_lower_case[letter_secret_key_position]

            encrypted_ascii = (ord(message[i]) - ord(secret_key_in_upper_case)) % 26
            decrypted_message += chr(encrypted_ascii + ord("A"))

        else: decrypted_message += message[i]

    print("DECIFRADA: " + decrypted_message + "\n")

encrypt()
decrypt()