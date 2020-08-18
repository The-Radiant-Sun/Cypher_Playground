# Atbash cypher
class AtbashCypher:
    def __init__(self, message, key):
        """Establish self dictionaries and variables for later calling"""
        # Establishing dictionaries for translation
        self.char_set_lower = {chr(i): chr(ord('z') - n) for n, i in enumerate(range(ord('a'), ord('z') + 1))}
        print(self.char_set_lower)
        self.char_set_upper = {char_text.upper(): self.char_set_lower[char_text].upper() for char_text in self.char_set_lower}
        self.message = message
        self.key = key

    @staticmethod
    def history():
        """Return basic history and instructions for Atbash"""
        history = '''There is a preset key alphabet, so no inputted key will affect the resulting message.
The Atbash Cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed.
I.e. all "A"s are replaced with "Z"s, all "B"s are replaced with "Y"s, and so on.

It was originally used for the Hebrew alphabet, but can be used for any alphabet.
The Atbash Cipher offers almost no security, and can be broken very easily. '''
        return history

    def cypher(self):
        """Return altered text"""
        # Empty base
        result = ''
        for char in self.message:
            # Passing char if it is not an alphabetic letter
            if not char.isalpha():
                result += char
            else:
                # Adding the translated lowercase or uppercase text to the result
                result += self.char_set_lower[char] if char in self.char_set_lower else self.char_set_upper[char]
        return result

    def encrypt(self):
        """Return result from cypher function"""
        return self.cypher()

    def decrypt(self):
        """Return result from cypher function"""
        return self.cypher()