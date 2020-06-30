# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CypherPlaygroundGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from Cyphers import Cypher


class UiForm(object):
    def __init__(self, form):
        # Forming initial ratios
        self.width_ratio = 1
        self.height_ratio = 1
        # Establishing base widgets
        self.comboBox = QtWidgets.QComboBox(form)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(form)
        self.radioButton = QtWidgets.QRadioButton(form)
        self.radioButton_2 = QtWidgets.QRadioButton(form)
        self.pushButton = QtWidgets.QPushButton(form)

    def ratio_alter(self, x, y, width, height):
        # Returns coordinates and dimensions altered by the form size
        alter_x = self.width_ratio * x
        alter_y = self.height_ratio * y
        alter_width = self.width_ratio * width
        alter_height = self.height_ratio * height
        return QtCore.QRect(alter_x, alter_y, alter_width, alter_height)

    def setup_ui(self, form):
        def setup_widget(self_name, geometry, name):
            # Quick setup widget to save space and time
            self_name.setGeometry(geometry)
            self_name.setObjectName(name)
        # Creating the form
        form.setObjectName("Form")
        form.resize(1000, 750)
        # Altering the ratios
        self.width_ratio = form.width()/565
        self.height_ratio = form.height()/399
        # Creating the widgets
        setup_widget(self.comboBox, self.ratio_alter(20, 20, 131, 21), 'comboBox')
        setup_widget(self.radioButton, self.ratio_alter(20, 59, 62, 14), 'radioButton')
        setup_widget(self.radioButton_2, self.ratio_alter(90, 59, 62, 14), 'radioButton_2')
        setup_widget(self.plainTextEdit, self.ratio_alter(169, 20, 372, 152), 'plainTextEdit')
        setup_widget(self.plainTextEdit_2, self.ratio_alter(20, 90, 131, 82), 'plainTextEdit_2')
        setup_widget(self.plainTextEdit_3, self.ratio_alter(169, 190, 372, 151), 'plainTextEdit_3')
        setup_widget(self.plainTextEdit_4, self.ratio_alter(20, 190, 131, 151), 'plainTextEdit_4')
        setup_widget(self.pushButton, self.ratio_alter(479, 360, 62, 14), 'pushButton')
        # Adding spaces for the comboBox
        for i in range(len(Cypher().cypher_set)):
            self.comboBox.addItem("")
        # Setting options for widgets
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_4.setReadOnly(True)
        self.radioButton.setChecked(True)
        # Binding the run button to the cypher_text function
        self.pushButton.clicked.connect(self.cypher_text)
        # Binding the comboBox to update_fields function
        self.comboBox.activated[str].connect(self.update_fields)
        # Updating the widget text
        self.retranslate_ui(form)
        # Connecting slots to the form
        QtCore.QMetaObject.connectSlotsByName(form)

    def update_fields(self):
        # Clearing the text fields, while updating the history field
        self.plainTextEdit.setPlainText("Input message")
        self.plainTextEdit_2.setPlainText("Input key")
        self.plainTextEdit_3.setPlainText("Resulting text")
        self.plainTextEdit_4.setPlainText(Cypher().history_set[self.comboBox.currentText()]())

    def cypher_text(self):
        # Establishing break condition for Select Cypher option
        if self.comboBox.currentIndex() != 0:
            if self.plainTextEdit.toPlainText() != '' or self.plainTextEdit_2.toPlainText() != '':
                # Establishing variables to save space
                inputs = [self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()]
                encryption = Cypher().cypher_set[self.comboBox.currentText()](inputs[0], inputs[1])
                # Encrypts or decrypts depending on selected radioButton
                if self.radioButton.isChecked():
                    self.plainTextEdit_3.setPlainText(encryption.encrypt())
                else:
                    self.plainTextEdit_3.setPlainText(encryption.decrypt())

    def retranslate_ui(self, form):
        # Updating all text
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Cypher Playground"))
        for i, cypher in enumerate(Cypher().cypher_set):
            self.comboBox.setItemText(i, _translate("Form", cypher))
        self.plainTextEdit.setPlainText(_translate("Form", "Input message"))
        self.plainTextEdit_2.setPlainText(_translate("Form", "Input key"))
        self.plainTextEdit_3.setPlainText(_translate("Form", "Resulting text"))
        self.plainTextEdit_4.setPlainText(_translate("Form", Cypher().history_set[self.comboBox.currentText()]()))
        self.radioButton.setText(_translate("Form", "Encrypt"))
        self.radioButton_2.setText(_translate("Form", "Decrypt"))
        self.pushButton.setText(_translate("Form", "Run"))
