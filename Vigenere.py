# Vigenere cypher
class VigenereCypher:
    def __init__(self, message, key):
        self.char_set = [char for char in (chr(i) for i in range(32, 127))]
        self.message = message
        self.key = self.check_error(key)

    @staticmethod
    def history():
        history = 'Vigenere filler'
        return history

    def cypher(self, encrypt_decrypt):
        # Empty base
        result = ''
        for i, char in enumerate(self.message):
            # Adding all characters outside the char_set
            if char not in self.char_set:
                result += char
            else:
                # Enacting the different encryption and decryption
                if encrypt_decrypt == 'encrypt':
                    result += self.char_set[(self.char_set.index(char) + self.char_set.index(self.key[i % len(self.key)]) % len(self.char_set)) % len(self.char_set)]
                else:
                    result += self.char_set[(self.char_set.index(char) - self.char_set.index(self.key[i % len(self.key)]) % len(self.char_set)) % len(self.char_set)]
        return result

    def encrypt(self):
        return self.cypher('encrypt')

    def decrypt(self):
        return self.cypher('decrypt')

    def check_error(self, key):
        checked = ''
        for char in key:
            checked += char if char in self.char_set else ''
            print()
        return checked
