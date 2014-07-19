'''
Created on Jun 29, 2014

@author: jason
'''

import os

includes_extentions = ['jpg','bmp','png','gif','JPG','BMP','GIF']

def list_all_images_in_folder(folder_path):
    out = []
    for fn in os.listdir(folder_path):
        for ext in includes_extentions:
            if fn.endswith(ext):
                out.append(folder_path+fn)
    return sorted(out)

def find_all_images_in_list(input_list):
    out = []
    for fn in input_list:
        for ext in includes_extentions:
            if fn.endswith(ext):
                out.append(fn)
    return sorted(out)


def is_images_contained(input_list):
    image_list = find_all_images_in_list(input_list)
    if len(image_list) > 0:
        return True
    else:
        return False


def find_fist_images_in_list(input_list):
    image_list = find_all_images_in_list(input_list)
    return image_list[0]


