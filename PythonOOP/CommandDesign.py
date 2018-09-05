#!/usr/bin/python
#coding:utf8

"""
Command 命令模式
"""

import os


class ChangeFileNameCommand:
    def __init__(self,old_name,new_name):
        self.old_name=old_name
        self.new_name=new_name
    def execute(self):
        self()

    def __call__(self):
        print(f'change {self.old_name} to {self.new_name}')
        os.rename(self.old_name,self.new_name)

    def undo(self):
        print(f'change {self.new_name} to {self.old_name}')
        os.rename(self.new_name,self.old_name)
if __name__=='__main__':

    command_list=[]
    command_list.append(ChangeFileNameCommand('terry.txt','menglihuan.txt'))
    command_list.append(ChangeFileNameCommand('xzj.txt','hsy.txt'))

    for cmd in command_list:
        cmd.execute()

    for cmd in reversed(command_list):
        cmd.undo()
