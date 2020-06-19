# Keyword cypher
class KeywordCypher:
    def __init__(self, message, key):
        self.message = message
        self.key = [ord(char) for char in key]

    def encrypt(self):
        result = ''
        for i, character in enumerate(self.message):
            upper = False
            if character == ' ':
                result += character
                continue
            upper = False if character.islower() else True
            character = character.lower()
            alter = ord(character) + self.key[i % len(self.key)]
            alter -= 26 if alter > ord('z') else 0
            alter += 26 if alter < ord('a') else 0
            alter = chr(alter)
            alter = alter.upper() if upper else alter
            result += alter
        return result

    def decrypt(self):
        result = ''
        for i, character in enumerate(self.message):
            upper = False
            if character == ' ':
                result += character
                continue
            upper = False if character.islower() else True
            character = character.lower()
            alter = ord(character) - self.key[i % len(self.key)]
            alter -= 26 if alter > ord('z') else 0
            alter += 26 if alter < ord('a') else 0
            alter = chr(alter)
            alter = alter.upper() if upper else alter
            result += alter
        return result
