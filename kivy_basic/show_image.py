'''
Created on Jun 28, 2014

@author: jason
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.core.window import Window
from kivy_basic import images_finder
from kivy_basic import bidirection_iterator
import sys
import os

class ShowAPhoto(BoxLayout):
    
    def __init__(self, **kwargs):
        super(ShowAPhoto,self).__init__(**kwargs)
        
        self.file_index = -1
        image_list = images_finder.find_all_images_in_list(sys.argv)
        
        if len(image_list)>0:
            self.prepare_list(image_list[0])
        else:
            self.prepare_list('./')
                    
        self.aimage = AsyncImage(source=self.get_next_file())
        
        self.add_widget(self.aimage)
        
        self._keyboard = Window.request_keyboard(self._keyboard_closed,self,'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    
    def prepare_list(self,filepath):
    	folderpath = os.path.dirname(filepath)+'/'
        file_list = images_finder.list_all_images_in_folder(folderpath)
        iterator= bidirection_iterator.BidirectionIterator(file_list)
        if filepath != './':
            iterator.move_before(filepath)
        self.file_iterator = iterator
        
        
    def get_next_file(self):
        return self.file_iterator.next();
        
    def get_previous_file(self):
        return self.file_iterator.previous();
 
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
        return ShowAPhoto()

if __name__ == "__main__":
    MyApp().run()
         
