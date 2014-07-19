'''
Created on 2014/7/19

@author: jason
'''
import unittest
from kivy_basic import images_finder
import os
from util import folder_operation


class Test(unittest.TestCase):


    def prepare_test_folder(self):
        self.test_folder = './test_image_folder/'
        self.image_files = ['a.jpg', 'b.png', 'c.bmp']
        folder = folder_operation.creat_folder(self.test_folder)
        for image_name in self.image_files:
            folder.create_empty_file(image_name)
        
        self.image_paths = []
        for i in range(len(self.image_files)):
            self.image_paths.append(os.path.join(self.test_folder, self.image_files[i]))

    def setUp(self):
        self.prepare_test_folder()

    def tearDown(self):
        folder_operation.delete_folder(self.test_folder)
        pass

    def test_list_all_image_in_folder(self):
        images = images_finder.list_all_images_in_folder(self.test_folder)
        self.assertEquals(images, self.image_paths, "Error finding images in a folder")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()