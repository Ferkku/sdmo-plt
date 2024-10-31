
from string import punctuation

class PigLatinError(Exception):
    pass

class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase
        self.vowels = 'aeiou'
        self.allowed_chars = 'aeioubcdfghjklmnpqrstvwxyz-.,;:\'?!()'
        self.punctuation = '.,;:\'?!()'

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        words = self.phrase.split()
        translated_words = []

        for word in words:
            if word[-1] not in self.allowed_chars:
                raise PigLatinError
            if '-' in word:
                translated_words.append(self.handle_composite_word(word))
            else:
                translated_words.append(self.apply_word_rules(word))
        return ' '.join(translated_words)

    def apply_word_rules(self, word: str) -> str:
        punc = ''
        if word[-1] in punctuation:
            punc = word[-1]
            word = word[:-1]
        if word[0] not in self.vowels:
            while word[0] not in self.vowels:
                word = word[1:] + word[0]
        if word[-1] == 'y':
            return word + 'nay' + punc
        elif word[-1] in self.vowels:
            return word + 'yay' + punc
        else:
            return word + 'ay' + punc

    def handle_composite_word(self, word: str):
        composite_words = word.split('-')
        temp_comp_words = []
        for comp_word in composite_words:
            temp_comp_words.append(self.apply_word_rules(comp_word))
        return '-'.join(temp_comp_words)

