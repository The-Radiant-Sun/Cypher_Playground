# Interactive cryptography playground
from Atbash import AtbashCypher
from Caesar import CaesarCypher
from Keyword import KeywordCypher
from Autokey import AutokeyCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    def __init__(self):
        """Create self definitions for classes and history"""
        # Establishing set of cypher classes to be called upon
        self.cypher_set = {
            'Select Cypher': Cypher,
            'Atbash Cypher': AtbashCypher,
            'Caesar Cypher': CaesarCypher,
            'Keyword Cypher': KeywordCypher,
            'Vigenere Cypher': VigenereCypher,
            'Autokey Cypher': AutokeyCypher,
            'XOR Algorithm': XOR
        }

        self.history_set = {cypher_text: self.cypher_set[cypher_text].history for n, cypher_text in enumerate(self.cypher_set)}

    @staticmethod
    def history():
        """Return basic description and instructions as history"""
        history = '--DESCRIPTION--\nThis application is a cryptography playground, where users can\nLearn about various cyphers\nUnderstand their uses\nInteract with different modes of encryption.\n\n'
        history += '--INSTRUCTIONS--\nTo use this application:\nSelect the cypher from the drop-down menu in the top left of the GUI.\nEnter the message and key into the respective text fields.\nSelect whether to encrypt or decrypt the message.\nClick run, and the resulting text should appear in the lower right text field.'
        return history
