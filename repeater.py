# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repeater.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Repeater(object):
    def setupUi(self, Repeater):
        Repeater.setObjectName("Repeater")
        Repeater.resize(453, 195)
        Repeater.setMinimumSize(QtCore.QSize(453, 195))
        Repeater.setMaximumSize(QtCore.QSize(453, 195))
        self.centralwidget = QtWidgets.QWidget(Repeater)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(431, 111))
        self.textBrowser.setMaximumSize(QtCore.QSize(431, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.path_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_lineedit.setObjectName("path_lineedit")
        self.gridLayout_2.addWidget(self.path_lineedit, 0, 0, 1, 1)
        self.complate_time_label = QtWidgets.QLabel(self.centralwidget)
        self.complate_time_label.setText("")
        self.complate_time_label.setObjectName("complate_time_label")
        self.gridLayout_2.addWidget(self.complate_time_label, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chose_button = QtWidgets.QPushButton(self.centralwidget)
        self.chose_button.setObjectName("chose_button")
        self.gridLayout.addWidget(self.chose_button, 0, 0, 1, 1)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setMinimumSize(QtCore.QSize(75, 40))
        self.result_label.setMaximumSize(QtCore.QSize(75, 40))
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.gridLayout.addWidget(self.result_label, 0, 1, 2, 1)
        self.make_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_button.setObjectName("make_button")
        self.gridLayout.addWidget(self.make_button, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)
        Repeater.setCentralWidget(self.centralwidget)

        self.retranslateUi(Repeater)
        QtCore.QMetaObject.connectSlotsByName(Repeater)

    def retranslateUi(self, Repeater):
        _translate = QtCore.QCoreApplication.translate
        Repeater.setWindowTitle(_translate("Repeater", "中继器固件转换工具-v0.0.1"))
        self.textBrowser.setHtml(_translate("Repeater", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">使用说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">1. 选择将要制作的bin文件；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">2. 点击制作；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">3. 制作成功后会在bin目录下以当前时间创建一个带时间戳文件夹，文件夹中有code_msg.txt、termin.txt两个文件；</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">4. 将code_msg.txt、termin.txt两个文件复制至U盘，该两文件即为中继器升级所必须的文件。</span></p></body></html>"))
        self.chose_button.setText(_translate("Repeater", "选择固件"))
        self.make_button.setText(_translate("Repeater", "制作"))

