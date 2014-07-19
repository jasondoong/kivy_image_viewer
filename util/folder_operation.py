'''
Created on 2014/7/19

@author: jason
'''
from os.path import os
import shutil


class Folder(object):
    
    def __init__(self, folder_path):
        self.path = folder_path
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def create_empty_file(self, filename):
        fo = open(os.path.join(self.path, filename), 'wb')
        fo.close()

def creat_folder(folder_path):
    return Folder(folder_path)

def delete_folder(folder_path):
    shutil.rmtree(folder_path)
