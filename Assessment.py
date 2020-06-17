# Interactive cryptography playground
from GUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

from Caeser import CaesarCypher
from Vigenere import VigenereCypher
from XOR import XOR


class Assessment:
    def __init__(self):
        self.message = Assessment.get_input('message')
        self.key = Assessment.get_input('key')

    def run(self):
        print(CaesarCypher(self.message, self.key).encrypt())

    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            Assessment.get_inputs(string)
        return user_input


Assessment().run()
