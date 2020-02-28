import pickle
import os
from os import path

#文件复制
def File_Copy(f_1, f_2):
    #文件打开
    file_1 = open(f_1, "rb")
    file_2 = open(f_2, "wb")

    #文件复制
    pickle.dump(file_1.read(), file_2)

    #文件的关闭
    file_2.close
    file_1.close


#文件遍历
def File_Trav(url_1, url_2):
    for i in os.listdir(url_1):
        #文件名拼接
        file_1 = path.join(url_1, i)
        
        
        #是不是文件夹
        if path.isdir(file_1):
            #新建复制文件夹
            file_2 = path.join(url_2, i)
            os.makedirs(file_2)
            #递归遍历
            File_Trav(file_1, file_2)
        #是不是文件:
        elif path.isfile(file_1):
            #调用文件拷贝
            File_Copy(file_1, path.join(url_2, i))
        else:
            print("错误!")
            break




url_1 = input("请输入被copy的磁盘：")
url_2 = input("请输入copy到的磁盘：")
File_Trav(url_1, url_2)
