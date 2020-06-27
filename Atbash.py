# Atbash cypher
class AtbashCypher:
    def __init__(self, message, key):
        self.char_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.message = message
        self.key = key

    @staticmethod
    def history():
        history = 'There is a preset key alphabet, so no inputted key will affect the resulting message. Atbash filler'
        return history

    def cypher(self):
        result = ''
        for char in self.message:
            if not char.isalpha():
                result += char
            else:
                upper = False if char.islower() else True
                char = char.lower()
                alter = self.char_set[-self.char_set.index(char)]
                result += alter.upper() if upper else alter
        return result

    def encrypt(self):
        return self.cypher()

    def decrypt(self):
        return self.cypher()
