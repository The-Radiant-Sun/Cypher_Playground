# Autokey cypher
class AutokeyCypher:
    def __init__(self, message, key):
        """Save char_set, message and key as self variables"""
        # Defining base alphabet
        self.char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # Passing message and key
        self.message = message
        self.key = key.lower()

    @staticmethod
    def history():
        """Return history for Keyword"""
        history = 'Autokey Filler'
        return history

    def cypher(self, encrypt_decrypt):
        """Return altered text based on encrypt_decrypt input"""
        # Base result
        result = ''
        # Variation for non-alpha characters
        alter = 0
        for i, char in enumerate(self.message):
            # Passing non-alpha characters in message
            if not char.isalpha():
                result += char
                continue
            # Passing non-alpha characters in message
            if self.key[i] not in self.char_set:
                alter += 1
            # Establishing lowercase while recording if uppercase
            upper = True if char.isupper() else False
            char = char.lower()
            # Encrypt and decrypt alterations
            if encrypt_decrypt == 'encrypt':
                # Altering the char
                char_alter = self.char_set[(self.char_set.index(char) + self.char_set.index(self.key[i + alter])) % len(self.char_set)]
                # Uppercase if uppercase
                result += char_alter.upper() if upper else char_alter
                self.key += char
            else:
                # Altering the char
                char_alter = self.char_set[(self.char_set.index(char) - self.char_set.index(self.key[i + alter])) % len(self.char_set)]
                # Uppercase if uppercase
                result += char_alter.upper() if upper else char_alter
                self.key += char_alter
        return result

    def encrypt(self):
        """Return result from cypher function with encrypt input"""
        return self.cypher('encrypt')

    def decrypt(self):
        """Return result from cypher function with decrypt input"""
        return self.cypher('decrypt')
