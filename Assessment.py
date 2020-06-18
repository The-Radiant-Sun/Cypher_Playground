# Interactive cryptography playground
from Caeser import CaesarCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    def __init__(self):
        self.message = Cypher.get_input('message')
        self.key = Cypher.get_input('key')

    def run(self):
        print(CaesarCypher(self.message, self.key).encrypt())

    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            user_input = Cypher.get_input(string)
        return user_input


Cypher().run()
