# Interactive cryptography playground
from Atbash import AtbashCypher
from Caesar import CaesarCypher
from Keyword import KeywordCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    def __init__(self):
        # Establishing set of cypher classes to be called upon
        self.cypher_set = {
            'Select Cypher': Cypher,
            'Atbash Cypher': AtbashCypher,
            'Caesar Cypher': CaesarCypher,
            'Keyword Cypher': KeywordCypher,
            'Vigenere Cypher': VigenereCypher,
            'XOR Algorithm': XOR
        }

        self.history_set = {
            'Select Cypher': Cypher.history,
            'Atbash Cypher': AtbashCypher.history,
            'Caeser Cyphar': CaesarCypher.history,
            'Keyword Cypher': KeywordCypher.history,
            'Vigenere Cypher': VigenereCypher.history,
            'XOR Algorithm': XOR.history
        }

    @staticmethod
    def history():
        history = '--DESCRIPTION--\nThis application is a cryptography playground, where users can\nLearn about various cyphers\nUnderstand their uses\nInteract with different modes of encryption.\n\n'
        history += '--INSTRUCTIONS--\nTo use this application:\nSelect the cypher from the drop-down menu in the top left of the GUI.\nEnter the message and key into the respective text fields.\nSelect whether to encrypt or decrypt the message.\nClick run, and the resulting text should appear in the lower right text field.'
        return history
