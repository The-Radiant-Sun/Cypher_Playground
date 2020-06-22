# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CypherPlaygroundGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Assessment import Cypher



class UiForm(object):
    @staticmethod
    def ratio_alter(ratio_width, ratio_height, x, y, width, height):
        alter_x = ratio_width * x
        alter_y = ratio_height * y
        alter_width = ratio_width * width
        alter_height = ratio_height * height
        return QtCore.QRect(alter_x, alter_y, alter_width, alter_height)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1000, 750)
        form_width_ratio = form.width()/565
        form_height_ratio = form.height()/399
        self.comboBox = QtWidgets.QComboBox(form)
        self.comboBox.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 20, 20, 131, 21))
        self.comboBox.setObjectName("comboBox")
        for i in range(4):
            self.comboBox.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 180, 20, 361, 151))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit_2.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 20, 90, 131, 281))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(form)
        self.plainTextEdit_3.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 180, 190, 361, 151))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.radioButton = QtWidgets.QRadioButton(form)
        self.radioButton.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio,20, 60, 62, 14))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(form)
        self.radioButton_2.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 90, 60, 62, 14))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(self.ratio_alter(form_width_ratio, form_height_ratio, 479, 360, 62, 14))
        self.pushButton.setObjectName("pushButton")
        self.retranslate_ui(form)
        self.comboBox.activated[str].connect(self.cypher_text)
        QtCore.QMetaObject.connectSlotsByName(form)

    def cypher_text(self):
        self.plainTextEdit_2.setPlainText(Cypher().cyphers[self.comboBox.currentText()]().encrypt())

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Caeser Cypher"))
        self.comboBox.setItemText(1, _translate("Form", "Keyword Cypher"))
        self.comboBox.setItemText(2, _translate("Form", "Vigenere Cypher"))
        self.comboBox.setItemText(3, _translate("Form", "XOR Algorithm"))
        self.plainTextEdit.setPlainText(_translate("Form", "Input message"))
        self.plainTextEdit_2.setPlainText(_translate("Form", "Input key"))
        self.plainTextEdit_3.setPlainText(_translate("Form", "Resulting text"))
        self.radioButton.setText(_translate("Form", "Encrypt"))
        self.radioButton_2.setText(_translate("Form", "Decrypt"))
        self.pushButton.setText(_translate("Form", "Run"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(form)
    form.show()
    sys.exit(app.exec_())
