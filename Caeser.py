# Caeser cypher
class CaesarCypher:
    def __init__(self, message, key):
        # Saving char_set, message and key
        self.char_set = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.message = message
        self.key = self.check_error(key)
        # Restricting the key to reasonable ranges
        while self.key > 25 or self.key < 0:
            self.key -= 26 if self.key > 25 else 0
            self.key += 26 if self.key < 0 else 0

    def encrypt(self):
        # Empty base
        result = ''
        for character in self.message:
            # Adding the character if it is not a standard alphabet character
            if character == ' ' or not character.isalpha():
                result += character
                continue
            # Recording if character is uppercase or not
            upper = False if character.islower() else True
            character = character.lower()
            # Committing the alteration
            alter = self.char_set[self.char_set.index(character) + self.key]
            # Updating the alteration if character was uppercase
            alter = alter.upper() if upper else alter
            result += alter
        return result

    def decrypt(self):
        # The decryption of Caeser Cypher is the same with the reversed key
        return CaesarCypher(self.message, -self.key).encrypt()

    def check_error(self, potential):
        # Checking if the key is actually an integer
        try:
            potential = int(potential)
        except ValueError:
            potential = self.check_error(input('Please enter a numerically correct key: '))
        return potential
