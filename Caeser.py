# Caeser cypher
class CaesarCypher:
    def __init__(self, message, key):
        # Saving char_set, message and key
        self.char_set = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.message = message
        self.key = self.check_error(key)

    def cypher(self, encrypt_decrypt):
        if self.key == 'error':
            return 'Please enter a numerically correct key.'

        # Restricting the key to reasonable ranges
        while self.key > 25 or self.key < 0:
            self.key -= 26 if self.key > 25 else 0
            self.key += 26 if self.key < 0 else 0

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
            if encrypt_decrypt == 'encrypt':
                alter = self.char_set[self.char_set.index(character) + self.key]
            else:
                alter = self.char_set[self.char_set.index(character) - self.key]
            # Updating the alteration if character was uppercase
            alter = alter.upper() if upper else alter
            result += alter
        return result

    def encrypt(self):
        return self.cypher('encrypt')

    def decrypt(self):
        return self.cypher('decrypt')

    @staticmethod
    def check_error(key):
        # Checking if the key is actually an integer
        try:
            key = int(key)
        except ValueError:
            key = 'error'
        return key
