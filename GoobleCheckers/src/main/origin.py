'''
Created on 2011-10-02

@author: Gooble
'''

def get_top():
    return Origin('TOP', 1)

def get_bottom():
    return Origin('BOTTOM', -1)

class Origin(object):

    def __init__(self, desc, value):
        self.desc = desc
        self.value = value
        
    def __eq__(self, other):
        if other is None: return False
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
