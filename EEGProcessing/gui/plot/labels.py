# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EEGProcessing\gui\plot\labels.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_label(object):
    def setupUi(self, label):
        label.setObjectName("label")
        label.resize(343, 369)
        label.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(label)
        self.gridLayout.setObjectName("gridLayout")
        self.OkBt = QtWidgets.QPushButton(label)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.OkBt.setFont(font)
        self.OkBt.setObjectName("OkBt")
        self.gridLayout.addWidget(self.OkBt, 1, 0, 1, 1)
        self.cancelBt = QtWidgets.QPushButton(label)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.cancelBt.setFont(font)
        self.cancelBt.setObjectName("cancelBt")
        self.gridLayout.addWidget(self.cancelBt, 1, 1, 1, 1)
        self.listView = QtWidgets.QListView(label)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.listView.setFont(font)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.listView.setTabKeyNavigation(True)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)

        self.retranslateUi(label)
        QtCore.QMetaObject.connectSlotsByName(label)

    def retranslateUi(self, label):
        _translate = QtCore.QCoreApplication.translate
        label.setWindowTitle(_translate("label", "Select label"))
        self.OkBt.setText(_translate("label", "OK"))
        self.cancelBt.setText(_translate("label", "Cancel"))
