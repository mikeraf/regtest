'''
Created on 2017-02-14

@author: michar
'''
import unittest
from src.steps import AssertionStep, SimpleExecutionStep, ExecutionStepWithArtifact, StepStatus
from operator import isCallable

class Test(unittest.TestCase):

    def testAssertionStepSuccess(self):
        my_assertion = AssertionStep(val=5, should_be=5)
        self.assertEquals(my_assertion.status, StepStatus.UNCHECKED)
        my_assertion.execute()
        self.assertEqual(my_assertion.status, StepStatus.SUCCESS)           
        pass
    
    def testAssertionStepFailure(self):
        my_assertion = AssertionStep(val=3, should_be=5)
        self.assertEquals(my_assertion.status, StepStatus.UNCHECKED)
        my_assertion.execute()
        self.assertEqual(my_assertion.status, StepStatus.FAIL)           
        pass
    
    def testSimpleExecutionStepFailure(self):
        my_step = SimpleExecutionStep("simple_fail_execution.py")
        self.assertEquals(my_step.status, StepStatus.NEW)
        my_step.execute()
        # the file doesn't exist
        self.assertEqual(my_step.status, StepStatus.FAIL)
    
    def testSimpleExecutionStepSuccess(self): 
        my_step = SimpleExecutionStep("simple_success_execution.py")
        self.assertEquals(my_step.status, StepStatus.NEW)
        my_step.execute()
        self.assertEqual(my_step.status, StepStatus.SUCCESS)
        
    def testExecutionWithArtifact(self):
        my_step = ExecutionStepWithArtifact("execution_with_artifact.py")
        self.assertEquals(my_step.status, StepStatus.NEW)
        self.assertRaises(RuntimeError, my_step.getArtifact)
        my_step.execute()
        self.assertEqual(my_step.status, StepStatus.SUCCESS)
        self.assertEqual(my_step.getArtifact(), 5)
    
    def testExecutionFollowedByAssertionGood(self):
        step1 = ExecutionStepWithArtifact("execution_with_artifact.py")
        step2 = AssertionStep(step1.getArtifact, 5)
        
        step1.execute()
        step2.execute()
        
        self.assertEqual(step2.status, StepStatus.SUCCESS)
    
    
    def testExecutionFollowedByAssertionBad(self):
        step1 = ExecutionStepWithArtifact("simple_success_execution.py")
        step2 = AssertionStep(step1.getArtifact, 5)
        
        step1.execute()
        step2.execute()
        
        self.assertEqual(step2.status, StepStatus.FAIL)
               
         

    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAssertionStep']
    unittest.main()