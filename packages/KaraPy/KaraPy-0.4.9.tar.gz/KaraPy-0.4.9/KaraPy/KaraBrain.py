from KaraPy.Enums import Sensor, Move

class State(object):
    global Transitions
    global Name
    global isStart
    Transitions = []
    Name = "Stanadrt"
    isStart = False

    def __init__(self, _Name, _isStart=False):
        global Name, isStart
        Name = _Name
        isStart = _isStart

    def AddTransition(self, t):
        global Transitions
        Transitions.extend(t)
        
        

    def getStart(self):
        global isStart
        return isStart

    def getTransitions(self):
        global Transitions
        return Transitions


class Transition(object):
    global condition
    global output
    global nextState
    condition = [[Sensor.L, True]]
    output = [Move.Down]
    nextState = None

    def __init__(self, _condition, _output=[], _nextState=None):
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

