# coding:utf-8

import os

basePath = "E:\\workplace\\Python\\PythonToolsProject\\files"
rootFileOutPutPath = "D:\\output\\"


# 2017/4/9
# 遍历目录下内容并判断是否包含关键字,筛选存在关键字的内容并保存在对应的文件中
def __main__():
    for root, dirs, files in os.walk(basePath, topdown=True):
        for file in files:
            print os.path.join(root, file)
            read_one(root, file)


def read_one(root, file):
    f = open(os.path.join(root, file), "r")
    lines = f.readlines()
    out_data = ''
    for line in lines:
        if "多媒体" in line:
            out_data = out_data + line

        if "保存照片" in line:
            out_data = out_data + line
    f.close()

    if not os.path.exists(rootFileOutPutPath):
        os.makedirs(rootFileOutPutPath)
    write_one(rootFileOutPutPath + os.path.basename(file), out_data)


def write_one(fileName, str):
    f = file(fileName, "w+")
    f.writelines(str)
    f.close()


if __name__ == '__main__':
    __main__()
