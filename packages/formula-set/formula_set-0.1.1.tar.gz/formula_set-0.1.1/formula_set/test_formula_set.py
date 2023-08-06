import unittest
import formula_set as fs

class TestBasics(unittest.TestCase):
    def test_basic(self):
        formula_set = fs.Formula_set()
        formula_set.add_formula(["b - 26 = 4 * 3 + 6 * 2", "c = b + 2", "a = c + b", "d = 3"])
        self.assertEqual(formula_set.see('b'), 50)