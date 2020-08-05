# Caesar cypher
class CaesarCypher:
    def __init__(self, message, key):
        """Save char_set, message and key as self variables"""
        self.char_set = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.message = message
        self.key = self.check_error(key)

    @staticmethod
    def history():
        """Return history and instructions for Caesar"""
        history = '''Use a numeric key, it is recommended to be within range ONE - TWENTY-SIX, but if numbers outside 
        this range is inputted, then the program will lag. The Caesar Cipher is one of the earliest known and 
        simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is "shifted" a 
        certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, 
        B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate 
        with his generals. The Caesar cipher offers essentially no communication security, and it will be shown that 
        it can be easily broken even by hand. '''
        return history

    def cypher(self, encrypt_decrypt):
        """Return altered text if no error
        Vary altered text if encrypt input"""
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
            if not character.isalpha():
                result += character
                continue
            # Recording if character is uppercase or not
            upper = False if character.islower() else True
            character = character.lower()
            # Committing the alteration
            if encrypt_decrypt == 'encrypt':
                alter = self.char_set[(self.char_set.index(character) + self.key) % len(self.char_set)]
            else:
                alter = self.char_set[(self.char_set.index(character) - self.key) % len(self.char_set)]
            # Updating the alteration if character was uppercase
            result += alter.upper() if upper else alter
        return result

    def encrypt(self):
        """Return result from cypher function with encrypt input"""
        return self.cypher('encrypt')

    def decrypt(self):
        """Return result from cypher function with decrypt input"""
        return self.cypher('decrypt')

    @staticmethod
    def check_error(key):
        """Check if the key is actually an integer
        Return error if not"""
        try:
            key = int(key)
        except ValueError:
            key = 'error'
        return key
