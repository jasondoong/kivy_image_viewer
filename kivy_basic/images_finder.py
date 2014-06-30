'''
Created on Jun 29, 2014

@author: jason
'''

import os

includes_extentions = ['jpg','bmp','png','gif']
list = []

def list_all_images_in_folder(folder_path):
    for fn in os.listdir(folder_path):
        for ext in includes_extentions:
            if fn.endswith(ext):
                print(folder_path+fn)
                list.append(folder_path+fn)
    return list