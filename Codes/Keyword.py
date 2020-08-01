# Keyword cypher
class KeywordCypher:
    def __init__(self, message, key):
        """Save the message and ord of each character in the key as self variables"""
        self.message = message
        self.key = [ord(char) for char in key]

    @staticmethod
    def history():
        """Return history for Keyword"""
        history = 'The Keyword Cypher is identical to the Ceaser Cypher, exept that a word can be used as a key.'
        return history

    def cypher(self, encrypt_decrypt):
        """Return altered text based on encrypt_decrypt input"""
        # Empty base
        result = ''
        for i, character in enumerate(self.message):
            upper = False
            # Adding the character if it is not a space
            if character == ' ':
                result += character
                continue
            # Recording if character is uppercase or not
            upper = False if character.islower() else True
            character = character.lower()
            # Committing the alteration, + if encrypt, - if decrypt
            if encrypt_decrypt == 'encrypt':
                alter = ord(character) + self.key[i % len(self.key)]
            else:
                alter = ord(character) - self.key[i % len(self.key)]
            # Ensuring that the value is within reasonable range
            while alter > ord('z') or alter < ord('a'):
                alter -= 26 if alter > ord('z') else 0
                alter += 26 if alter < ord('a') else 0
            # Changing the alteration back to a character
            alter = chr(alter)
            # Updating the alteration if it was uppercase
            alter = alter.upper() if upper else alter
            result += alter
        return result

    def encrypt(self):
        """Return result from cypher function with encrypt input"""
        return self.cypher('encrypt')

    def decrypt(self):
        """Return result from cypher function with decrypt input"""
        return self.cypher('decrypt')


