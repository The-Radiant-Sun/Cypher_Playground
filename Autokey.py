# Autokey cypher
class AutokeyCypher:
    def __init__(self, message, key):
        self.char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.message = message
        self.key = key

    @staticmethod
    def history():
        history = 'Autokey Filler'
        return history

    def cypher(self):
        result = ''
        for char in self.message:
            if not char.isalpha():
                result += char

        return result

    def encrypt(self):
        return self.cypher()

    def decrypt(self):
        return self.cypher()
