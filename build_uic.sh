#########################################################################
# File Name: build_uic.sh
# Author: ZhenhuaWei
# mail: weizhenhua94@163.com 
# Created Time: 2019-5-8 14:28:42
#########################################################################
#!/bin/bash

#local system Source file path
LOCAL_FILE=$(cd "$(dirname "$0")";pwd)
ui_file_list=""

echo "============================Start============================"

ui_file_list=`ls *.ui`
if [ $? -ne 1 ];then
    for ui_file in $ui_file_list
    do
        if [ -d $ui_file ] 
        then
            continue
        fi
        temp_file=${ui_file%%.ui}".py"
        pyuic5 $ui_file -o $temp_file
        if [ $? -ne 0 ];then
            pyuic $ui_file -o $temp_file
            if [ $? -ne 0 ];then
                echo "[ERR ]Exc pyuic/pyuic5 fail and exit !!!"
                exit
            fi
        fi

        echo "[INFO]pyuic $ui_file -o $temp_file"
    done
	
else
    echo "[ERR ]Not have .ui files !!!"
    exit
fi

echo "[INFO]Leave $FLODER"
echo "[INFO]pyuic execute success and pyuic floder's files have beed covered"
echo "=============================end============================="
echo ""
exit