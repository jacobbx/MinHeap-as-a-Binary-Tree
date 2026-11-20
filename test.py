import unittest
from unittest.case import _AssertRaisesBaseContext

from BinaryTreeWeighted import BinaryTreeWeighted
from solution import insert
from solution import extract

class TestSolution(unittest.TestCase):
    
    
    def test_extract_empty_raises_value_error(self):
        empty_tree = BinaryTreeWeighted()
        
        with self.assertRaisesRegex(ValueError, "Cannot extract from empty tree."):
            extract(empty_tree)
            
    def test_insert_is_not_comparable_to_other_nodes(self):
        tree = BinaryTreeWeighted(15)
        value = "hi"

        with self.assertRaisesRegex(TypeError, "Value must match type of existing tree values"):
            insert(tree, value)