from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Initialize instance provide word file path name"""
        self.file_path = file_path
        self.words_list = self.read_file()
        self.print_number_of_words()

    def __repr__(self):
        return f"""<WordFinder file_path= {self.file_path}
        words_list= {self.words_list}>"""

    def read_file(self):
        """Reads word file, returns list of words"""
        #TODO:strip new line char
        word_file = open(self.file_path)
        words_list = [word for word in word_file]

        word_file.close()
        return words_list

    def print_number_of_words(self):
        """Prints number of words in the word file"""
        print(f'{len(self.words_list)} words read')

    def return_random_word(self):
        """Returns random word from words list"""
        random_word = choice(self.words_list)
        return random_word.replace("\n", "")


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words and filters out comments
        and blank lines"""

    def __init__(self, file_path):
        """inherits attributes from Word Finder word file path name"""
        super().__init__(file_path)

    def print_number_of_words(self):
        """Prints number of words in the word file"""
        self.filter_only_words()
        print(f'{len(self.words_list)} words read')

    def filter_only_words(self):
        """remove white space and comments from word list"""
        self.words_list = [
            word for word in self.words_list if '#' not in word]
        self.words_list = [
            word for word in self.words_list if word !=
            '\n']
