# Caeser cypher
class CaesarCypher:
    def __init__(self, message, key):
        self.message = message
        self.key = self.check_error(key)

    def encrypt(self):
        result = ''
        for character in self.message:
            upper = False
            if character == ' ' or not character.isalpha():
                result += character
                continue
            upper = False if character.islower() else True
            character = character.lower()
            alter = ord(character) + self.key
            while alter > ord('z') or alter < ord('a'):
                alter -= 26 if alter > ord('z') else 0
                alter += 26 if alter < ord('a') else 0
            alter = chr(alter)
            alter = alter.upper() if upper else alter
            result += alter
        return result

    def decrypt(self):
        return CaesarCypher(self.message, -self.key).encrypt()

    def check_error(self, potential):
        try:
            potential = int(potential)
        except ValueError:
            potential = CaesarCypher(self.message, input('Please enter a numerically correct key: ')).key
        return potential
