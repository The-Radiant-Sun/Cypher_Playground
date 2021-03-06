# Interactive cryptography playground
from Codes.Atbash import AtbashCypher
from Codes.Caesar import CaesarCypher
from Codes.Keyword import KeywordCypher
from Codes.Autokey import AutokeyCypher
from Codes.Vigenere import VigenereCypher
from Codes.XOR import XOR


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

        self.history_set = {cypher_text: self.cypher_set[cypher_text].history for cypher_text in self.cypher_set}

    @staticmethod
    def history():
        """Return basic description and instructions as history"""
        history = '''--DESCRIPTION--
This application is a cryptography playground,
where users can learn about various cyphers,
understand their uses and interact with different modes of encryption.

--INSTRUCTIONS--
To use this application, select the cypher from the drop-down menu in the top left of the GUI.
Enter the message and key into the respective text fields.
Select whether to encrypt or decrypt the message.
Click run, and the resulting text should appear in the lower right text field. '''
        return history
