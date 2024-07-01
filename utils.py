import string
from itertools import product

# Функция для загрузки и фильтрации словаря
def load_filtered_words(file_path):
    with open(file_path) as f:
        words = set(word.strip() for word in f if word.strip().isalpha() and len(word.strip()) > 2)
    additional_words = {'a', 'are', 'we', 'me', 'he', 'she', 'is', 'hi', 'to', 'my'}
    words.update(additional_words)
    return words

# Загрузка отфильтрованного словаря
ENGLISH_WORDS = load_filtered_words('filtered_words_alpha.txt')

# Функции для шифрования и дешифрования Виженера и Цезаря
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

def vigenere_decipher(ciphertext, key):
    key = key.upper()
    decrypted_text = []
    key_index = 0
    key_length = len(key)

    for char in ciphertext:
        if char.isalpha():
            offset = ord(key[key_index % key_length]) - ord('A')
            decoded_char = chr(((ord(char) - ord('A') - offset + 26) % 26) + ord('A'))
            decrypted_text.append(decoded_char)
            key_index += 1
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

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

def shift_decipher(text, shift):
    return shift_cipher(text, -shift)

# Вспомогательные функции
def is_meaningful(text):
    words = text.split()
    meaningful_word_count = sum(1 for word in words if word.lower() in ENGLISH_WORDS)
    return meaningful_word_count

def generate_possible_keys():
    alphabet = string.ascii_uppercase
    possible_keys = []
    for key_length in range(1, 5):  # Trying key lengths from 1 to 4
        for key_tuple in product(alphabet, repeat=key_length):
            possible_keys.append(''.join(key_tuple))
    return possible_keys

def generate_word_keys():
    word_keys = [word.upper() for word in ENGLISH_WORDS if len(word) <= 4]
    return word_keys

# Взлом шифра Виженера
def vigenere_brute_force(ciphertext):
    possible_keys = generate_possible_keys() + generate_word_keys() + ["WORD"]
    possible_decryptions = []

    for key in possible_keys:
        decrypted_text = vigenere_decipher(ciphertext, key)
        meaningful_score = is_meaningful(decrypted_text)
        possible_decryptions.append((decrypted_text, key, meaningful_score))

    return possible_decryptions

# Взлом шифра Цезаря
def shift_brute_force(ciphertext):
    possible_decryptions = []
    for shift in range(1, 26):
        decrypted_text = shift_decipher(ciphertext, shift)
        meaningful_score = is_meaningful(decrypted_text)
        possible_decryptions.append((decrypted_text, f"Shift {shift}", meaningful_score))
    
    return possible_decryptions

# Объединение и сортировка
def combined_brute_force(ciphertext, target_word=None):
    vigenere_results = vigenere_brute_force(ciphertext)
    shift_results = shift_brute_force(ciphertext)

    all_results = vigenere_results + shift_results


    unique_results = list(set(all_results))


    if target_word:
        target_word = target_word.lower()
        filtered_results = [res for res in unique_results if target_word in res[0].lower()]
    else:
        filtered_results = unique_results


    filtered_results.sort(key=lambda x: -x[2])


    top_decryptions = [{"decryption": decryption, "key": key, "meaningful_score": score} for decryption, key, score in filtered_results[:10]]

    return top_decryptions

# Тест
ciphertext = "DW DB JODH EG DDT"
target_word = "max"
top_decryptions = combined_brute_force(ciphertext, target_word)
print(top_decryptions)
