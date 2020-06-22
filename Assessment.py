# Interactive cryptography playground
from Caeser import CaesarCypher
from Keyword import KeywordCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    def __init__(self):
        # Establishing the message and key
        self.message = Cypher.get_input('message')
        self.key = Cypher.get_input('key')
        # Establishing set of cyphers separated by encrypt / decrypt
        self.cyphers = {
            'CaeserCypher': CaesarCypher,
            'KeywordCypher': KeywordCypher,
            'VigenereCypher': VigenereCypher,
            'XOR': XOR
        }

    def run(self, method, encrypt_decrypt):
        if encrypt_decrypt == 'encrypt':
            return self.cyphers[method](self.message, self.key).encrypt()
        else:
            return self.cyphers[method](self.message, self.key).decrypt()

    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            user_input = Cypher.get_input(string)
        return user_input


print(Cypher().run('CaeserCypher', 'encrypt'))
