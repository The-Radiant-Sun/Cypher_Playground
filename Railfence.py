# Railfence cypher
class RailfenceCypher:
    def __init__(self, message, key):
        self.message = message
        self.key = self.check_error(key)

    def cypher(self, encrypt_decrypt):
        fence = [[None] * len(self.message) for n in range(self.key)]
        rails = range(self.key - 1) + range(self.key - 1, 0, -1)
        for i, char in enumerate(self.message):
            fence[rails[i % len(rails)]][i] = char

        return [c for rail in fence for c in rail if c is not None]

    def encrypt(self):
        return ''.join(self.cypher('encrypt'))

    def decrypt(self):
        rng = range(len(self.message))
        pos = self.cypher('decrypt')
        return ''.join(self.message[pos.index(n)] for n in rng)

