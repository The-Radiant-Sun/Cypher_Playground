# Interactive cryptography playground
from GUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from Vigenere import VigenereCypher
from XOR import XOR


class Cypher:
    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            user_input = Cypher.get_input(string)
        return user_input


Cypher().run()
