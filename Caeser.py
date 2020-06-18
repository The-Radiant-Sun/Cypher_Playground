# Caeser cypher
from Assessment import Cypher


class CaesarCypher(Cypher):
    def __init__(self):
        self.message = Cypher.get_input('message')
        self.key = self.check_error(Cypher.get_input('key'))

    def encrypt(self):
        result = ''
        for character in self.message:
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
        return self.encrypt()

    def check_error(self, potential):
        try:
            potential = int(potential)
        except ValueError:
            potential = self.check_error(Cypher.get_input('numerically correct key'))
        return potential


print(CaesarCypher().encrypt())
