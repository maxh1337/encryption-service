def is_abbreviation(word):
    # Правило 1: если слово состоит только из заглавных букв и длиннее 1 символа
    if word.isupper() and len(word) > 1:
        return True
    # Правило 2: если слово содержит мало гласных (настраиваемый порог)
    vowels = 'AEIOU'
    vowel_count = sum(1 for char in word.upper() if char in vowels)
    if vowel_count < 1:
        return True
    return False

def filter_words(input_file, output_file, min_word_length=3, significant_words=None):
    if significant_words is None:
        significant_words = {
            'a', 'are', 'we', 'me', 'he', 'she', 'am', 'an', 'as', 'at', 'be', 'by', 'do', 'go', 'he', 'if', 'in', 'is',
            'it', 'me', 'my', 'no', 'of', 'on', 'or', 'so', 'to', 'up', 'us', 'we'
        }

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip()
            if len(word) < min_word_length and word not in significant_words:
                continue
            if not is_abbreviation(word):
                outfile.write(word + '\n')

input_file = 'words_alpha.txt'
output_file = 'filtered_words_alpha.txt'
significant_words = {
    'a', 'are', 'we', 'me', 'he', 'she', 'am', 'an', 'as', 'at', 'be', 'by', 'do', 'go', 'he', 'if', 'in', 'is', 'it', 
    'me', 'my', 'no', 'of', 'on', 'or', 'so', 'to', 'up', 'us', 'we', 'hi'
}
filter_words(input_file, output_file, significant_words=significant_words)
