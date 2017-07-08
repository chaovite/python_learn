# Construct a simulation, an application to simulate digital circuits.
# Based on the online book: Problem Solving with Algorithms and Data Structures.
# http://interactivepython.org/runestone/static/pythonds/index.html

class LogicGate:
    def __init__(self, label):
        self.label  = label
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    def __str__(self):
        return self.label
#    def performGateLogic():
#        """NOT implemented in this general calss"""
#        return None


# Now define two child classes for LogicGate class
class BinaryGate(LogicGate):
    """Binary gate that has two pins"""
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate %s -->" % (self.getLabel())))
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB==None:
            return int(input("Enter Pin B input for gate %s -->" % (self.getLabel())))
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self, source):
        """set next pin using source (a connector)"""
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise ValueError('Cannot connect: NO EMPTY PINS on this gate')

class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate %s -->" % (self.getLabel())))
        else:
            return self.pin.getFrom().getOutput()
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise ValueError('Cannot connect: NO EMPTY PIN on this gate')


# Now build specific gates.

class AddGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0
class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)
    def performGateLogic(self):
        pin = self.getPin()
        if pin==1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fromGate, toGate):
        self.fromGate = fromGate
        self.toGate   = toGate
        toGate.setNextPin(self)
    def getFrom(self):
        return self.fromGate
    def getTo(self):
        return self.toGate

def main():
    gate = LogicGate('ADD')
    g1 = AddGate('G1')
    g2 = AddGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate('G4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

main()
