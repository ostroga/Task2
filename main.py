alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ123456789"

# Encrypts message with caesar cipher
def Encrypt(message, key):
    result = ""
    for item in message:
        try:
            current_index = alphabet.index(item)
            if current_index + key > len(alphabet):
                new_index = current_index + key - len(alphabet)
                result += alphabet[new_index]
            else:
                new_index = current_index + key
                result += alphabet[new_index]

        except ValueError:
            result += item
    return result

# Decrypts message with caesar cipher
def Decrypt(message, key):
    result = ""
    for item in message:
        try:
            current_index = alphabet.index(item)
            if current_index - key < 0:
                new_index = current_index - key + len(alphabet)
                result += alphabet[new_index]
            else:
                new_index = current_index - key
                result += alphabet[new_index]

        except ValueError:
            result += item
    return result



while True:
    message = str(input("Введіть речення для шифровки: "))

    key = 3

    encryptedMessage = Encrypt(message, key)
    print(f'Encrypted message: {encryptedMessage}')

    decryptedMessage = Decrypt(encryptedMessage, key)
    print(f'Decrypted message: {decryptedMessage} \n')