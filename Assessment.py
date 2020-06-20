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
            'Encrypt': {
            'CaeserCypher': CaesarCypher(self.message, self.key).encrypt,
            'KeywordCypher': KeywordCypher(self.message, self.key).encrypt,
            'VigenereCypher': VigenereCypher(self.message, self.key).encrypt,
            'XOR': XOR(self.message, self.key).encrypt
        },
            'Decrypt': {
            'CaeserCypher': CaesarCypher(self.message, self.key).decrypt,
            'KeywordCypher': KeywordCypher(self.message, self.key).decrypt,
            'VigenereCypher': VigenereCypher(self.message, self.key).decrypt,
            'XOR': XOR(self.message, self.key).decrypt
        }}

    def run(self, encrypt_decrypt, method):
        print(self.cyphers[encrypt_decrypt][method])
        print(self.cyphers[encrypt_decrypt][method]())

    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            user_input = Cypher.get_input(string)
        return user_input


Cypher().run('Encrypt', 'KeywordCypher')
