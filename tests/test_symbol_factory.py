import unittest
from symbol_factory import SymbolFactory
from .helpers import (
    plus,
    space,
    number_one,
    number_five,
    number_eight,
    number_nine,
)

class TestPhone(unittest.TestCase):

    def test_get_string(self):
        symbol = SymbolFactory()
        assert plus == symbol.get_string(single_simbol="+")
        assert space == symbol.get_string(single_simbol=" ")
        assert number_one == symbol.get_string(single_simbol="1")
        assert number_five == symbol.get_string(single_simbol="5")
        assert number_eight == symbol.get_string(single_simbol="8")
        assert number_nine == symbol.get_string(single_simbol="9")

    def calling_unknown_function_1(self):
        return "hello there"

    def calling_unknown_function_2(self):
        return "my name is francisco."

    def test_learning_how_to_use_ipdb(self):
        x = self.calling_unknown_function_1()
        y = self.calling_unknown_function_2()
        assert x+", "+y == "hello there, my name is francisco."