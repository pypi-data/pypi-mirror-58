# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_image_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveImageDialog(object):
    def setupUi(self, SaveImageDialog):
        SaveImageDialog.setObjectName("SaveImageDialog")
        SaveImageDialog.resize(722, 284)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveImageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(SaveImageDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(SaveImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(SaveImageDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.width_box = QtWidgets.QSpinBox(SaveImageDialog)
        self.width_box.setMinimum(100)
        self.width_box.setMaximum(9999)
        self.width_box.setProperty("value", 1280)
        self.width_box.setObjectName("width_box")
        self.gridLayout.addWidget(self.width_box, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputFile_box = QtWidgets.QLineEdit(SaveImageDialog)
        self.outputFile_box.setEnabled(True)
        self.outputFile_box.setObjectName("outputFile_box")
        self.horizontalLayout.addWidget(self.outputFile_box)
        self.outputFile_chooser = QtWidgets.QPushButton(SaveImageDialog)
        self.outputFile_chooser.setEnabled(True)
        self.outputFile_chooser.setObjectName("outputFile_chooser")
        self.horizontalLayout.addWidget(self.outputFile_chooser)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(SaveImageDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(SaveImageDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(SaveImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.height_box = QtWidgets.QSpinBox(SaveImageDialog)
        self.height_box.setMinimum(100)
        self.height_box.setMaximum(9999)
        self.height_box.setProperty("value", 720)
        self.height_box.setObjectName("height_box")
        self.gridLayout.addWidget(self.height_box, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(SaveImageDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.dpi_box = QtWidgets.QSpinBox(SaveImageDialog)
        self.dpi_box.setMinimum(10)
        self.dpi_box.setMaximum(1000)
        self.dpi_box.setProperty("value", 80)
        self.dpi_box.setObjectName("dpi_box")
        self.gridLayout.addWidget(self.dpi_box, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(SaveImageDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(SaveImageDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(SaveImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(SaveImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)
        self.writeScriptsAndConfig = QtWidgets.QCheckBox(SaveImageDialog)
        self.writeScriptsAndConfig.setChecked(True)
        self.writeScriptsAndConfig.setObjectName("writeScriptsAndConfig")
        self.gridLayout.addWidget(self.writeScriptsAndConfig, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(SaveImageDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaveImageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SaveImageDialog)
        self.buttonBox.accepted.connect(SaveImageDialog.accept)
        self.buttonBox.rejected.connect(SaveImageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveImageDialog)
        SaveImageDialog.setTabOrder(self.width_box, self.height_box)
        SaveImageDialog.setTabOrder(self.height_box, self.dpi_box)
        SaveImageDialog.setTabOrder(self.dpi_box, self.outputFile_box)
        SaveImageDialog.setTabOrder(self.outputFile_box, self.outputFile_chooser)
        SaveImageDialog.setTabOrder(self.outputFile_chooser, self.writeScriptsAndConfig)
        SaveImageDialog.setTabOrder(self.writeScriptsAndConfig, self.buttonBox)

    def retranslateUi(self, SaveImageDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveImageDialog.setWindowTitle(_translate("SaveImageDialog", "Save Image"))
        self.label_3.setText(_translate("SaveImageDialog", "Save image"))
        self.label_4.setText(_translate("SaveImageDialog", "Export the current view to an image."))
        self.outputFile_chooser.setText(_translate("SaveImageDialog", "Browse"))
        self.label_8.setText(_translate("SaveImageDialog", "Output file:"))
        self.label_5.setText(_translate("SaveImageDialog", "DPI:"))
        self.label_11.setText(_translate("SaveImageDialog", "(Dots/pixels per inch)"))
        self.label_6.setText(_translate("SaveImageDialog", "Width:"))
        self.label.setText(_translate("SaveImageDialog", "Height:"))
        self.label_7.setText(_translate("SaveImageDialog", "Output file:"))
        self.label_12.setText(_translate("SaveImageDialog", "(The width of the image in pixels)"))
        self.label_14.setText(_translate("SaveImageDialog", "(The height of the image in pixels)"))
        self.writeScriptsAndConfig.setText(_translate("SaveImageDialog", "Write scripts and config file"))

