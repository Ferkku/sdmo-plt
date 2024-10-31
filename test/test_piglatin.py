import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_get_phrase(self):
        translator = PigLatin("hello world")
        phrase = translator.get_phrase()

        self.assertEqual("hello world", phrase)

    def test_translate_empty_string(self):
        translator = PigLatin("")

        self.assertEqual("nil", translator.translate())

    def test_translate_string_ending_in_y(self):
        translator = PigLatin("any")

        self.assertEqual("anynay", translator.translate())

    def test_translate_string_ending_in_vowel(self):
        translator = PigLatin("apple")

        self.assertEqual("appleyay", translator.translate())
