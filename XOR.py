# XOR algorithm
class XOR:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def encrypt(self):
        result = ''
        for i in range(len(self.message)):
            result += chr(ord(self.message[i]) ^ ord(self.key[i % len(self.key)]))
        return result

    def decrypt(self):
        return XOR(self.message, self.key).encrypt()
