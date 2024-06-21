def vigenere_cipher(text, key):
    text = text.upper()
    key = key.upper()
    result = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():
            offset = ord(key[key_index % key_length]) - ord('A')
            encoded_char = chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
            result.append(encoded_char)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

def shift_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encoded_char = chr(((ord(char) - offset + shift) % 26) + offset)
            result.append(encoded_char)
        else:
            result.append(char)
    return ''.join(result)
