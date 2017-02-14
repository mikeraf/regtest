from workflow.engine import GenericWorkflowEngine
from workflow.errors import HaltProcessing
from workflow.engine_db import DbWorkflowEngine

my_engine = GenericWorkflowEngine()

def prepare(obj, eng):
    print "Preparing...", obj, eng.current_taskname
    eng.jump_call(2)

def process(obj, eng):
    print "processing...", obj, eng.current_taskname

def postprocess(obj, eng):
    print "post-processing...",obj,eng.current_taskname

my_workflow = [prepare, process, postprocess] 

my_engine.callbacks.replace(my_workflow)

my_engine.process([()])

class PersistentWorkflow(object):
    '''
    This object represents a workflow which may be paused after each step
    and then resumed.
    Each step may be either FINISHED, WAITING or FAILED.
    When resuming into a FINISHED step, the execution continues to next step.
    When resuming into a WAITING step, a check is performed to check if the status
    was changed to either FINISHED or FAILED.
    '''
    def __init__(self, persistency=None):
        self.objects = [persistency]
        self.workflow = []

            
    def prepare(self, obj, eng):
        print "Preparing...", obj, eng.current_taskname

    def process(self, obj, eng):
        print "processing...", obj, eng.current_taskname

    def postprocess(self, obj, eng):
        print "post-processing...",obj,eng.current_taskname
            