# -*- coding: UTF8 -*-

import time
import os


class File():
    def __init__(self, name, uuids, ct, mt, vt):
        self.name = name
        self.uuids = uuids
        self.ct = ct
        self.mt = mt
        self.vt = vt

    def __str__(self) -> str:
        return super().__str__()


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileAccessTime(filePath):
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return t


def get_FileCreateTime(filePath):
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return t


def get_FileModifyTime(filePath):
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return t


def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            ct = get_FileCreateTime(file_path)
            mt = get_FileModifyTime(file_path)
            vt = get_FileAccessTime(file_path)
            uuids = []
            list_name[file_path] = File(file_path, uuids, ct, mt, vt);
    return list_name


if __name__ == '__main__':
    uuids = [1544494340.809236, 1544494341.809338, 1544494342.8098328, 1544494343.8105655,
             1544494344.8114219, 1544494345.8121765, 1544494346.8125079, 1544494347.8132424,
             1544494348.81386, 1544494349.8142257]
    # for uuid in uuids:
    #     abpath=os.path.abspath('.')
    #     with open(os.path.join(abpath,"{}.txt".format(uuid)),'x') as f:
    #             f.write("{}".format(uuid))
    files = {}
    files = listdir("H:\software\work\python_project\PythonStudyDemo\PythonBasic\FileReadTest",
                    files)
    for uuid in uuids:
        for filename in files:
            file = files[filename]
            strs = filename.split("\\")[-1].split(".")
            str=strs[0]+"."+strs[1]
            if str == "{}".format(uuid):
                file.uuids.append(uuid)
                break

    for index, filename in enumerate(files):
        strs = filename.split("\\")[-1].split(".")
        str=strs[0]+"."+strs[1]
        # print("文件名{}:{},list:{}".format(index, file.name, file.uuids))
        # list=file.uuids
        with open(filename)  as f:
            str =f.readline()
            print(str)
            with open("H:\software\work\python_project\PythonStudyDemo\PythonBasic\FileReadTest/res.txt","a") as res:
                res.write(str)