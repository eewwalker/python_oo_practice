from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.words_list = self.read_file()
        self.print_number_of_words()

    def read_file(self):
        #Reads word file, returns list of words
        word_file = open(self.file_path)
        words_list = [word for word in word_file]

        word_file.close()
        return words_list

    def print_number_of_words(self):
        #Prints number of words in the word file
        print (f'{len(self.words_list)} words read')

    def return_random_word(self):
        #Returns random word from words list
        random_word = choice(self.words_list)
        return random_word.replace("\n","")

test = WordFinder("words.txt")