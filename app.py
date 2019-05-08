#!/usr/bin/python3
import sys
import hashlib
from os import path
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from repeater import Ui_Repeater
from datetime import datetime
from PyQt5.QtGui import QPixmap,QPalette

def get_datetime():
    """ get current date time, as accurate as milliseconds
        
        Args: None
            
        Returns:
            str type
            eg: "20181001003239"
            
    """
    return str(datetime.now().strftime('%Y%m%d%H%M%S'))

def get_md5sum_and_filelen(filename):
    file_object = open(filename, 'rb')
    file_content = file_object.read()
    lenth = len(file_content)
    file_object.close()
    file_md5 = hashlib.md5(file_content)
    return file_md5, lenth

class OptionFile():
    def __init__(self, ui_obj, main_window_obj):
        print("test __init__")
        self.ui_obj = ui_obj
        self.main_window_obj = main_window_obj
        self.fw_path = ""
        self.file_md5 = 0
        self.file_len = 0
        self.init()

    def init(self):
        print("test init")

        self.ui_obj.chose_button.clicked.connect(self.chose_fw_path)
        self.ui_obj.make_button.clicked.connect(self.make_fw)
        print("end")
        
    def clear(self):
        pass

    def chose_fw_path(self):
        print("test chose_fw_path")
        open = QtWidgets.QFileDialog()
        filename,  _ = open.getOpenFileName()
        if filename:
            self.ui_obj.path_lineedit.setText(str(filename))
        else:
            self.ui_obj.path_lineedit.setText("")

        self.ui_obj.complate_time_label.setText("")
        self.ui_obj.result_label.setText("")
        self.ui_obj.result_label.setAutoFillBackground(False)

    def make_fw(self):
        print("test make_fw")
        self.fw_path = self.ui_obj.path_lineedit.text()
        if self.fw_path == "" or path.exists(self.fw_path) == False:
            QtWidgets.QMessageBox.critical(self.main_window_obj, "打开错误", "请选择正确的文件！")
        else:
            self.ui_obj.result_label.setText("制作成功")
            self.ui_obj.result_label.setAutoFillBackground(True)
            palette=QPalette()
            palette.setColor(QPalette.Window,Qt.green)
            self.ui_obj.result_label.setPalette(palette)
            self.ui_obj.result_label.setAlignment(Qt.AlignCenter)
            self.file_md5, self.file_len = get_md5sum_and_filelen(self.fw_path)
            #创建一个文件夹、文件，写入日期（3）+MD5（16）+长度（4）



            print (self.file_md5.hexdigest())
            self.ui_obj.complate_time_label.setText("本次制作完成时间："+
                str(get_datetime() + " 长度：" + str(self.file_len)))

if __name__ == '__main__':
    app =QtWidgets.QApplication(sys.argv)
    form=QtWidgets.QMainWindow()  
    myapp=Ui_Repeater()
    myapp.setupUi(form)

    # to do something
    opt = OptionFile(myapp,form)
    #end

    form.show()
    sys.exit(app.exec_())