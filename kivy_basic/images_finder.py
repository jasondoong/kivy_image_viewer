'''
Created on Jun 29, 2014

@author: jason
'''

import os

includes_extentions = ['jpg','bmp','png','gif','JPG','BMP','GIF']

def list_all_images_in_folder(folder_path):
    list = []
    for fn in os.listdir(folder_path):
        for ext in includes_extentions:
            if fn.endswith(ext):
                print(folder_path+fn)
                list.append(folder_path+fn)
    return sorted(list)

def find_all_images_in_list(input_list):
    out = []
    for fn in input_list:
        for ext in includes_extentions:
            if fn.endswith(ext):
                out.append(fn)
    return sorted(out)
