import functools
import os
import sys
import unittest
import examples

PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PATH, os.path.pardir, "scangen"))

from rnd import ExprSymbols, convert, Dfa, DfaSymbols
from rnd.internals import crnd

TEST_DATA = {}

def sym(a=None, b=None):
    if a is None:
        return ExprSymbols()
    return ExprSymbols(ord(a), None if b is None else ord(b))

def closed_range(a, b=None):
    a = ord(a)
    if b:
        b = ord(b)+1
    else:
        b = min(0xffffffff, a+1)
    return ExprSymbols(a, b)

def optional(expr):
    return expr.union(sym())

def to_dfa(expr):
    """Converts expr to dfa and destroys expr."""
    dfa = convert(expr)
    expr.destroy()
    return dfa

def empty_expr():
    return sym()

def identifier_expr():
    letters = closed_range('_').union(closed_range('a', 'z')).union(closed_range('A', 'Z'))
    return letters.concatenation(letters.union(closed_range('0', '9')).closure())

def integer_expr():
    return closed_range('0').union(closed_range('1', '9').concatenation(closed_range('0', '9').closure()))

def whitespace_expr():
    return closed_range(' ').union(closed_range('\t')).union(closed_range('\n'))

def number_expr():
    digit = closed_range('0', '9')
    decimal = closed_range('.').concatenation(digit).concatenation(digit.closure())
    sign = optional(closed_range('-').union(closed_range('+')))
    exponent = (closed_range('e').union(closed_range('E'))).concatenation(sign).concatenation(integer_expr())
    return integer_expr().concatenation(optional(decimal)).concatenation(optional(exponent))

def string_expr():
    char = functools.reduce(lambda a, b: a.union(b),
            [ ExprSymbols(32, 33+1), ExprSymbols(35, 91+1), ExprSymbols(93, 126+1) ])
    char = char.union(closed_range("\\").concatenation(ExprSymbols(32, 126+1)))
    string = char.closure()
    return closed_range('"').concatenation(string).concatenation(closed_range('"'))

def character_expr():
    escape = closed_range("\\").concatenation(functools.reduce(lambda a, b: a.union(b),
        [closed_range("'"), closed_range("\\"), closed_range("t"), closed_range("n")]))
    middle = functools.reduce(lambda a, b: a.union(b),
            [ ExprSymbols(32, 38+1), ExprSymbols(40, 91+1), ExprSymbols(93, 126+1),
                escape ])
    return closed_range("'").concatenation(middle).concatenation(closed_range("'"))

EXPR_FN = {
    "empty": empty_expr,
    "number": number_expr,
    "identifier": identifier_expr,
    "string": string_expr,
    "character": character_expr,
    "whitespace": whitespace_expr,
}

def parametrize_expr_test(test_case, expr_type):
    test_case.dfa = to_dfa(EXPR_FN[expr_type]())
    test_case.assertTrue(TEST_DATA[expr_type])
    for word, label in TEST_DATA[expr_type]:
        word = word.encode().decode()
        accepted = test_case.dfa.compute(map(ord, word))
        label = bool(label)
        test_case.assertEqual(accepted, label)

class RndConversionTest(unittest.TestCase):
    def setUp(self):
        self.dfa = Dfa()

    def tearDown(self):
        self.dfa = Dfa()

    def test_leaks(self):
        for expr_fn in EXPR_FN.values():
            to_dfa(expr_fn())
        self.assertEqual(0, crnd.rnd_get_expr_counter())

    def test_random_data(self):
        for expr_type in EXPR_FN:
            with self.subTest(expr_type=expr_type):
                parametrize_expr_test(self, expr_type)

if __name__ == "__main__":
    for expr_type in EXPR_FN:
        with open(f"{PATH}/data/{expr_type}.csv", "r") as file:
            TEST_DATA[expr_type] = examples.read(file)
    unittest.main()
