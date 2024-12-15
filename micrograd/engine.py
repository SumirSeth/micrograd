import numpy as np

class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0

        self._prev = set(_children)
        self._op = _op

    def __repr__(self) -> str:
        return f'Value (data = {self.data})'
    
    def __add__(self, other):
        self.other = other
        output = Value(self.data + other.data, (self, other), '+')
        return output
    def __sub__(self, other):
        self.other = other
        output = Value(self.data - other.data, (self, other), '*')
        return output
    def __mul__(self, other):
        self.other = other
        output = Value(self.data * other.data, (self, other), '*')
        return output

