'''
Created on 6  2017

@author: michar
'''
import unittest


class Test(unittest.TestCase):


    def testItsWork(self):
        self.assertEqual(1, 1, "Its bad")
        pass
    def testItsNotWork(self):
        self.assertNotEqual(2, 1, "Its bad")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testItsWork']
    unittest.main()