# Vigenere cypher
class VigenereCypher:
    def __init__(self, message, key):
        self.char_set = [char for char in (chr(i) for i in range(32, 127))]
        self.message = message
        self.key = key

    def encrypt(self):
        result = ''
        for i, char in enumerate(self.message):
            if char not in self.char_set:
                result += char
            else:
                result += self.char_set[self.char_set.index(char) + self.char_set.index(self.key[i % len(self.key)]) % len(self.char_set)]
        return result

    def decrypt(self):
        result = ''
        for i, char in enumerate(self.message):
            if char not in self.char_set:
                result += char
            else:
                result += self.char_set[self.char_set.index(char) - self.char_set.index(self.key[i % len(self.key)]) % len(self.char_set)]
        return result
