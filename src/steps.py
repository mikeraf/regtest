'''
Created on 2017-02-14

@author: michar
'''

class StepStatus(object):
    UNCHECKED = 0
    SUCCESS = 1
    FAIL = 2    
    NEW = 3

class BasicStep(object):
    def __init__(self, initial_status):
        self._status = initial_status
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    def execute(self):
        raise NotImplementedError    
    
    
class AssertionStep(BasicStep):
    def __init__(self, val, should_be, msg=None):
        super(AssertionStep, self).__init__(StepStatus.UNCHECKED)
        self._val = val
        self._should_be_val = should_be
        self._msg = msg
    
    def execute(self):
        if callable(self._val):
            try:
                val = self._val()
            except:
                self.status = StepStatus.FAIL
                return
        else:
            val = self._val
            
        if callable(self._should_be_val):
            try:
                should_be_val = self._should_be_val()
            except:
                self.status = StepStatus.FAIL
        else:
            should_be_val = self._should_be_val
        
            
        if val == should_be_val:
            self.status = StepStatus.SUCCESS
        else:
            self.status = StepStatus.FAIL

class SimpleExecutionStep(BasicStep):
    '''a step which consists purely of executing scriptfile'''
    def __init__(self, scriptname):
        super(SimpleExecutionStep, self).__init__(StepStatus.NEW)
        self._scriptname = scriptname 
    
    def execute(self):
        try:
            env = {}
            execfile(self._scriptname, env)
        except Exception:
            self.status = StepStatus.FAIL
        else:
            self.status = StepStatus.SUCCESS
        finally:
            self._env = env
        
    pass


class ExecutionStepWithArtifact(SimpleExecutionStep):
    def __init__(self, scriptname, art=None):
        super(ExecutionStepWithArtifact, self).__init__(scriptname)
        self._art = art
        
    def execute(self):
        super(ExecutionStepWithArtifact, self).execute()
        if self.status == StepStatus.FAIL:
            return
        try:
            self._art = self._env['artifact']
        except:
            self.status = StepStatus.FAIL
        
    def getArtifact(self):
        if self.status != StepStatus.NEW:
            return self._art
        else:
            raise RuntimeError("Attempt to access artifact before execution")
        
    pass


