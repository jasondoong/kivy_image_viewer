'''
Created on 2014/7/19

@author: jason
'''
import unittest
from kivy_basic import bidirection_iterator


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass



    def prepare_bidirection_iterator(self):
        test_list = ['a', 'b', 'c', 'd', 'e']
        it = bidirection_iterator.BidirectionIterator(test_list)
        return it

    def test_next(self):
        it = self.prepare_bidirection_iterator()
        it.next()
        second_element = it.next()
        self.assertEqual(second_element, 'b', 'Error getting second element of list')
        
    def test_move_before(self):
        it = self.prepare_bidirection_iterator()
        it.move_before('c')
        self.assertEqual(it.next(), 'c', 'Error moving before a element')
        
    def test_previous(self):
        it = self.prepare_bidirection_iterator()
        it.previous()
        last_second_element = it.previous()
        self.assertEqual(last_second_element, 'd' ,"Error in previous()")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()