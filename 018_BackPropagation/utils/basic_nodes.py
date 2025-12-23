import numpy as np

class plus_node:
    def __init__(self):
        self._x, self._y = None, None
        self._z = None
    
    def forward(self, x, y):
        self._x, self._y = x, y
        self._z = self._x + self._y
        return self._z
    
    def backward(self, dz):
        return dz, dz
    
class minus_node:
    ##### Start Your Code(minus_node) #####

    ##### End Your Code(minus_node) #####
    
class mul_node:
    ##### Start Your Code(mul_node) #####

    ##### End Your Code(mul_node) #####

class square_node:
    ##### Start Your Code(square_node) #####

    ##### End Your Code(square_node) #####
    
class mean_node:
    ##### Start Your Code(mean_node) #####

    ##### End Your Code(mean_node) #####
