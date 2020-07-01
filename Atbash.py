# Atbash cypher
class AtbashCypher:
    def __init__(self, message, key):
        """Establish self dictionaries and variables for later calling"""
        # Establishing dictionaries for translation
        self.char_set_lower = {
            'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
            'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
            'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
            'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
            'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
            'z': 'a'}
        self.char_set_upper = {
            'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
            'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
            'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
            'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
            'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
            'Z': 'A'}
        self.message = message
        self.key = key

    @staticmethod
    def history():
        """Return basic history and instructions for Atbash"""
        history = 'There is a preset key alphabet, so no inputted key will affect the resulting message. Atbash filler'
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
