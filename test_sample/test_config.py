import pytest

class OutOfRange(Exception):
    def __init__(self, input_, message = "value not within range"):
        self.input_ = input_
        self.message = message
        super()._init_(self.message)

def test_pret():
    a = 2
    b = 4
    assert a!=b