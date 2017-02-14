'''
Created on 6  2017

@author: michar
'''

from workflow.engine_db import ObjectStatus
from workflow.engine import GenericWorkflowEngine


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params=None):
        '''
        Constructor
        '''
        self.params = params
        self.status = {}
        self.workflow = GenericWorkflowEngine()
    
    def get_params(self):
        return self.params

    
    def setCallbacks(self, callbaks_list):
        self.workflow.callbacks.replace(callbaks_list)
        pass


    def checkDivBy2(self, *args):
        self.status[self.checkDivBy2] = ObjectStatus.ERROR if args[0]%2 else ObjectStatus.COMPLETED
        pass

        
    def checkDivBy3(self, *args):
        self.status[self.checkDivBy3] =  ObjectStatus.ERROR if args[0]%3 else ObjectStatus.COMPLETED
        pass

    
    def checkDivBy5(self, *args):
        self.status[self.checkDivBy5] =  ObjectStatus.ERROR if args[0]%5 else ObjectStatus.COMPLETED
        pass

    
    def run(self):
        self.workflow.process([self.params])
        pass
    
    
    
    
    
    
    
    
    
    
        