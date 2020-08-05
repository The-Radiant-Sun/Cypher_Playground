# XOR algorithm
class XOR:
    def __init__(self, message, key):
        """Save message and key as self variables"""
        self.message = message
        self.key = key

    @staticmethod
    def history():
        """Return XOR history"""
        history = '''The XOR Cypher is a simple additive cypher.
        It focuses on the use of the additive disjunction operation,
        otherwise known as the XOR operation, which is how it got its name.'''
        return history

    def cypher(self):
        """Return altered text"""
        # Empty base
        result = ''
        for i in range(len(self.message)):
            # Enacting the encryption
            result += chr(ord(self.message[i]) ^ ord(self.key[i % len(self.key)]))
        return result

    def encrypt(self):
        """Return result from cypher function"""
        return self.cypher()

    def decrypt(self):
        """Return result from cypher function"""
        return self.cypher()
