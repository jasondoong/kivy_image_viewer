'''
Created on Jun 28, 2014

@author: jason
'''

class BidirectionIterator:
    
    def __init__(self, list):
        self.list = list
        self.list_size = len(list)
        self.index = -1
    
    def next(self):
        self.__increase_index()
        return self.list[self.index]
        
        
    def previous(self):
        self.__decrease_index()
        return self.list[self.index]

    def move_before(self,element): # TODO what if no such element in the list
        position = self.list.index(element)
        self.index = position
        self.__decrease_index()
        return self.list[self.index]
    
    def __increase_index(self):
        self.index = self.index + 1
        if self.index >= self.list_size :
            self.index = 0
    
    def __decrease_index(self):
        self.index = self.index -1
        if self.index < 0:
            self.index = self.list_size -1
