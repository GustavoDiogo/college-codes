alphabet = "abcdefghijklmnopqrstuvwxyz"

# PT: Cifrar
def encrypt(
    message = "MACHI NESCA NNOTT HINK",
    secret_key = "iamie xistt hatis cert"
):
    encrypted_message = ""
    
    if (len(secret_key) < len(message)):
        message_length = len(message)
        initial_secret_key_length = len(secret_key)

        while len(secret_key) < len(message):
            for i in range(0, message_length - initial_secret_key_length):
                secret_key += secret_key[i]

encrypt()