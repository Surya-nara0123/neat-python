import random


# creating the node class 
class node:
    def __init__(self, key, value = 0.0, bias = 0.5):
        self.key = key
        self.value = value
        self.bias = bias
    
# creating the gene class
class gene:
    def __init__(self, inNode, outNode, innov, enabled = True, weight = 0.5):
        self.inNode = inNode
        self.outNode = outNode
        self.weight = weight
        self.enabled = enabled
        self.innov = innov
    def randomize(self):
        self.weight = random.randint(-100000, 100000)/100000

# creating the genome class
class genome:
    def __init__(self, inputNo, outputNo):
        # initializing the basic variables
        self.inputNodes = []
        self.hiddenNodes = []
        self.outputNodes = []
        self.nodes = []

        # initializing the matrices variables
        
