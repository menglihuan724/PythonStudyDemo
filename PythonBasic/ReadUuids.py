# -*- coding: UTF8 -*-

import time
import datetime
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
            ct=get_FileCreateTime(file_path)
            mt=get_FileModifyTime(file_path)
            vt=get_FileAccessTime(file_path)
            uuids=[]
            list_name[file_path]=File(file_path,uuids,ct,mt,vt);
    return list_name
if __name__ == '__main__':
  uuids=[]
  for x in range(10):
            uuids.append(time.time())
  files={}
  files = listdir("H:/software/work/python_project/PythonStudyDemo/PythonBasic",files)
  for uuid in uuids:
    for filename in files:
      file=files[filename]
      if file.mt<uuid:
          file.uuids.append(uuid)
    continue
  for filename in files:
      file=files[filename]
      print("文件名:{},list:{}".format(file.name,file.uuids))
