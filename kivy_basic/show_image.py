'''
Created on Jun 28, 2014

@author: jason
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.core.window import Window
from kivy_basic import images_finder

class ShowAPhoto(BoxLayout):
    
    def __init__(self, **kwargs):
        super(ShowAPhoto,self).__init__(**kwargs)
        self.prepare_list()
        self.file_index = -1
        self.aimage = AsyncImage(source=self.get_next_file())
        self.add_widget(self.aimage)
        
        self._keyboard = Window.request_keyboard(self._keyboard_closed,self,'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    
    def prepare_list(self):
        self.file_list = images_finder.list_all_images_in_folder('./')
        
        
    def get_next_file(self):
        self.file_index = self.file_index + 1
        if self.file_index >= len(self.file_list):
            self.file_index = 0
        return self.file_list[self.file_index]
    
    def _keyboard_closed(self):
        print('My keyboard have been closed')
        self._keyboard.unbind(on_key_down=self._on__keyboard_down)
        self._keyboard = None
        
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.aimage.source = self.get_next_file()
        
class MyApp(App):
    
    def build(self):
        return ShowAPhoto()

if __name__ == "__main__":
    MyApp().run()
         