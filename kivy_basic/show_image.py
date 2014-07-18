'''
Created on Jun 28, 2014

@author: jason
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy_basic import images_finder
from kivy_basic import bidirection_iterator
import sys
import os

class ShowAPhoto(BoxLayout):
    
    def __init__(self, **kwargs):
        super(ShowAPhoto,self).__init__(**kwargs)
        
        self.prepare_image_list()
        self.add_image_widget()
        self.register_keydown_event()

    def prepare_image_list(self):
        if(images_finder.is_images_contained(sys.argv)) :
            image_arg = images_finder.find_fist_images_in_list(sys.argv)
            self.prepare_list(image_arg)
        else:
            self.prepare_list('./')

    def add_image_widget(self):
        self.aimage = AsyncImage(source=self.get_next_file())
        self.aimage.bind(source=self._on_image_load)
        self.add_widget(self.aimage)


    def register_keydown_event(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _on_image_load(self,image,source):
        self.set_app_title(source)
        
    def set_app_title(self, title):
        EventLoop.window.title = title

    def prepare_list(self,filepath):
        folderpath = os.path.dirname(filepath)+'/'
        file_list = images_finder.list_all_images_in_folder(folderpath)
        iterator= bidirection_iterator.BidirectionIterator(file_list)
        if filepath != './':
            iterator.move_before(filepath)
        self.file_iterator = iterator
        
        
    def get_next_file(self):
        return self.file_iterator.next()
        
    def get_previous_file(self):
        return self.file_iterator.previous()
 
    def _keyboard_closed(self):
        print('My keyboard have been closed')
        self._keyboard.unbind(on_key_down=self._on__keyboard_down)
        self._keyboard = None
        
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.aimage.source = self.get_previous_file()
        else:
            self.aimage.source = self.get_next_file()
        
        
class MyApp(App):
    
    def build(self):
        layout = ShowAPhoto()
        self.title = self.get_image_pathlayout(layout)
        return layout
    def get_image_pathlayout(self,layout):
        return layout.aimage.source

if __name__ == "__main__":
    MyApp().run()
         
