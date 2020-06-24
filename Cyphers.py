# Interactive cryptography playground
from Caeser import CaesarCypher
from Keyword import KeywordCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    def __init__(self):
        # Establishing set of cypher classes to be called upon
        self.cypher_set = {
            'Caeser Cypher': CaesarCypher,
            'Keyword Cypher': KeywordCypher,
            'Vigenere Cypher': VigenereCypher,
            'XOR Algorithm': XOR
        }

        self.history_set = {
            'Caeser Cypher': CaesarCypher.history,
            'Keyword Cypher': KeywordCypher.history,
            'Vigenere Cypher': VigenereCypher.history,
            'XOR Algorithm': XOR.history
        }
