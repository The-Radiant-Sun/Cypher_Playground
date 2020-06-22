# Keyword cypher
class KeywordCypher:
    def __init__(self, message, key):
        # Saving the message and each value of the key
        self.message = message
        self.key = [ord(char) for char in key]

    def cypher(self, encrypt_decrypt):
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
            # Commiting the alteration, + if encrypt, - if decrypt
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
        return self.cypher('encrypt')

    def decrypt(self):
        return self.cypher('decrypt')


