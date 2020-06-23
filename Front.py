from GUI import UiForm

from PyQt5 import QtWidgets
import sys


class RunApplication:
    def __init__(self):
        # Printing instructions
        print('''
        --DESCRIPTION--
        This application is intended to be used as a Cypher Playground,
        Where users can understand and interact with various cyphers.
        
        --INSTRUCTIONS--
        To use this application, select the cypher from the multi-box in the top left of the GUI,
        Then enter the message and key in the respective text fields,
        Following that, select whether to encrypt or decrypt the message,
        Finally, select run, and the resulting text should appear in the lower right text field.
        ''')
        # Running the UI
        app = QtWidgets.QApplication(sys.argv)
        form = QtWidgets.QWidget()
        ui = UiForm(form)
        ui.setup_ui(form)
        form.show()
        sys.exit(app.exec_())


RunApplication()
