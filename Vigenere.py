# Vigenere cypher
class VigenereCypher:
    def __init__(self, message, key):
        """Save char_set, message and key as self variables"""
        self.char_set = [char for char in (chr(i) for i in range(32, 127))]
        self.message = message
        self.key = self.check_error(key)

    @staticmethod
    def history():
        """Return history for Keyword"""
        history = 'Vigenere filler'
        return history

    def cypher(self, encrypt_decrypt):
        """Return altered text based on encrypt_decrypt input"""
        # Empty base
        result = ''
        for i, char in enumerate(self.message):
            # Adding all characters outside the char_set
            if char not in self.char_set:
                result += char
            else:
                # Enacting the different encryption and decryption
                if encrypt_decrypt == 'encrypt':
                    char_alter = self.char_set.index(char) + self.char_set.index(self.key[i % len(self.key)])
                else:
                    char_alter = self.char_set.index(char) - self.char_set.index(self.key[i % len(self.key)])
                result += self.char_set[char_alter % len(self.char_set)]
        return result

    def encrypt(self):
        """Return result from cypher function with encrypt input"""
        return self.cypher('encrypt')

    def decrypt(self):
        """Return result from cypher function with decrypt input"""
        return self.cypher('decrypt')

    def check_error(self, key):
        checked = ''
        for char in key:
            checked += char if char in self.char_set else ''
        return checked
