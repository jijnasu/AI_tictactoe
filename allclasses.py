
class Node():
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

class stackf():
    def __init__(self):
        self.stk = []

    def add(self,node):
        self.stk.append(node)

    def nodepresent(self,node):
        return node in self.stk

    def remove(self):
        if self.stk:
            return self.stk.pop()