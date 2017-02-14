'''
Created on 6  2017

@author: michar
'''
import unittest
from src.BasicTest import MyClass

from workflow.engine_db import ObjectStatus

class Test(unittest.TestCase):


    def testGetParams(self):
        mycls = MyClass(5)
        self.assertEqual(5, mycls.get_params())
        pass
    
    def testDeploy(self):
        mycls = MyClass(30)
        mycls.setCallbacks([mycls.checkDivBy2, mycls.checkDivBy3, mycls.checkDivBy5])
        mycls.run()
        self.assertEqual(mycls._status[mycls.checkDivBy2], ObjectStatus.COMPLETED)
        self.assertEqual(mycls._status[mycls.checkDivBy3], ObjectStatus.COMPLETED)
        self.assertEqual(mycls._status[mycls.checkDivBy5], ObjectStatus.COMPLETED)
    
    def testDeployWithFail(self):        
        mycls = MyClass(6)
        mycls.setCallbacks([mycls.checkDivBy2, mycls.checkDivBy3, mycls.checkDivBy5])
        mycls.run()
        self.assertEqual(mycls._status[mycls.checkDivBy2], ObjectStatus.COMPLETED)
        self.assertEqual(mycls._status[mycls.checkDivBy3], ObjectStatus.COMPLETED)
        self.assertEqual(mycls._status[mycls.checkDivBy5], ObjectStatus.ERROR)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetParams']
    unittest.main()