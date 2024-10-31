
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        words = self.phrase.split()
        translated_words = []
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'

        for word in words:
            parts = word.split('-')
            translated_parts = []
            for part in parts:
                if part[0] in vowels:
                    if part[-1] in vowels:
                        translated_parts.append(part + 'yay')
                    elif part[-1] == 'y':
                        translated_parts.append(part + 'nay')
                    else:
                        translated_parts.append(part + 'ay')
                else:
                    prefix = ''
                    while part[0] not in vowels and part[0] in consonants:
                        prefix += part[0]
                        part = part[1:]
                    if part[-1] in vowels:
                        translated_parts.append(part + prefix + 'ay')
                    elif part[-1] == 'y':
                        translated_parts.append(part + prefix + 'nay')
                    else:
                        translated_parts.append(part + prefix + 'ay')
            translated_words.append('-'.join(translated_parts))

        return ' '.join(translated_words)

