from KaraPy.Enums import Sensor, Move

class State:
    global Transitions
    global Name
    global isStart


    def __init__(self, _Name, _isStart=False):
        super().__init__(_Name)
        global Name, isStart, Transitions
        Name = _Name
        isStart = _isStart
        Transitions = []

    def AddTransition(self, t):
        global Transitions
        Transitions.append(t)
        
        

    def getStart(self):
        global isStart
        return isStart

    def getTransitions(self):
        global Transitions
        return Transitions


class Transition:
    global condition
    global output
    global nextState


    def __init__(self, _condition, _output=[], _nextState=None):
        super().__init__("Hi")
        global condition, output, nextState
        condition = _condition
        output = _output
        nextState = _nextState

    def getConditions(self):
        global condition
        return condition

    def getOutput(self):
        global output
        return output

    def getNextState(self):
        global nextState
        return nextState

