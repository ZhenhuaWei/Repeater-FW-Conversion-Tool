#!/usr/bin/python3
import sys
import hashlib
from shutil import copy
from os import path,makedirs
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from repeater import Ui_Repeater
from datetime import datetime
from PyQt5.QtGui import QPixmap,QPalette

updata_head_filename = "code_msg.txt"
updata_filename = "termin.txt"


def get_datetime_str():
    """ get current date time, as accurate as milliseconds
        
        Args: None
            
        Returns:
            str type
            eg: "20181001003239"
            
    """
    return str(datetime.now().strftime('%Y%m%d%H%M%S'))

def get_datetime():
    """ get current date time, as accurate as milliseconds
        
        Args: None
            
        Returns:
            list type
            eg: "(18,10,01)"
            
    """
    return datetime.now().strftime('%g'),datetime.now().strftime('%m'),datetime.now().strftime('%d')

def get_md5sum_and_filelen(filename):
    file_object = open(filename, 'rb')
    file_content = file_object.read()
    lenth = len(file_content)
    file_object.close()
    file_md5 = hashlib.md5(file_content)
    return file_md5, lenth

class OptionFile():
    def __init__(self, ui_obj, main_window_obj):
        self.ui_obj = ui_obj
        self.main_window_obj = main_window_obj
        self.fw_path = ""
        self.file_md5 = 0
        self.file_len = 0
        self.init()

    def init(self):
        self.ui_obj.chose_button.clicked.connect(self.chose_fw_path)
        self.ui_obj.make_button.clicked.connect(self.make_fw)


    def clear(self):
        self.ui_obj.complate_time_label.setText("")
        self.ui_obj.result_label.setText("")
        self.ui_obj.result_label.setAutoFillBackground(False)

    def chose_fw_path(self):
        open = QtWidgets.QFileDialog()
        filename,  _ = open.getOpenFileName()
        if filename:
            self.ui_obj.path_lineedit.setText(str(filename))
        else:
            self.ui_obj.path_lineedit.setText("")

        self.clear()

    def make_fw(self):
        # print("test make_fw")
        self.fw_path = self.ui_obj.path_lineedit.text()
        if self.fw_path == "" or path.exists(self.fw_path) == False:
            QtWidgets.QMessageBox.critical(self.main_window_obj, "打开错误", "请选择正确的文件！")
        else:
            try:
                #创建一个文件夹、文件，写入日期（3）+MD5（16）+长度（4）
                (folder, tempfilename) = path.split(self.fw_path)
                folder_path = str(folder)+"/"+get_datetime_str()
                if not path.exists(folder_path):
                    makedirs(folder_path)
                else:
                    return

                self.file_md5, self.file_len = get_md5sum_and_filelen(self.fw_path)
                data = get_datetime()
                md5_str = str(self.file_md5.hexdigest())
                # print (md5_str)

                updata_head_filename_fd = open(folder_path+"/"+updata_head_filename, "a+")
                updata_head_filename_fd.write(chr(int(data[0],16)))
                updata_head_filename_fd.write(chr(int(data[1],16)))
                updata_head_filename_fd.write(chr(int(data[2],16)))
                for x in range(0,16):
                    updata_head_filename_fd.write(chr(int(md5_str[x*2:(x+1)*2],16)))
                updata_head_filename_fd.write(chr(self.file_len))
                updata_head_filename_fd.close()

                copy(self.fw_path, folder_path+"/"+updata_filename)
                updata_filename_fd = open(folder_path+"/"+updata_filename, "a+")

                with open(folder_path+"/"+updata_head_filename, "r") as updata_head_filename_fd:
                    updata_head_data = updata_head_filename_fd.read()
                    updata_filename_fd.write(updata_head_data)

                updata_head_filename_fd.close()
                updata_filename_fd.close()

                self.ui_obj.result_label.setText("制作成功")
                self.ui_obj.result_label.setAutoFillBackground(True)
                palette=QPalette()
                palette.setColor(QPalette.Window,Qt.green)
                self.ui_obj.result_label.setPalette(palette)
                self.ui_obj.result_label.setAlignment(Qt.AlignCenter)
                self.ui_obj.complate_time_label.setText("本次制作完成时间："+
                    str(get_datetime_str() + " 长度：" + str(self.file_len)))
            except Exception as e:
                # print (repr(e))
                QtWidgets.QMessageBox.critical(self.main_window_obj, "错误", "制作失败，请重试！")
                self.clear()

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