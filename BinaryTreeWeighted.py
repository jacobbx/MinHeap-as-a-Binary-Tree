# Class that implements binary tree with features to support
# A heap
from collections.abc import Container


class BinaryTreeWeighted(Container):
    __emptyflag = object()
    strict_checking = (
        False  # Set to True for richer sanity checking
    )

    def __init__(self, value = __emptyflag, parent=None):
        self.value = value
        self.parent = parent
        self.weight = 1
        self.left = None
        self.right = None

    # Makes it possible to say btw[i] to access level i in tree btw
    # Note we carefully don't define __len__, so the tree is NOT iterable
    # And not a Collection
    def __getitem__(self, key):
        try:
            if key < 0:
                raise (
                    ValueError,
                    "key ({key}) must be positive integer",
                )
        except ValueError:
            raise  # reraise
        except Exception:
            raise (TypeError, "invalid key ({key})")

        return self._level(key)

    # Most trees don't support x in tree, but we do as it is
    # Useful for debugging
    # Warning, if tree has loops (e.g. a leaf that points to root)
    # This will fail with an excess recursion error
    def __contains__(self, value):
        self.__valid_key(value)
        if self.value == value:
            return True
        if self.left and value in self.left:
            return True
        if self.right and value in self.right:
            return True
        return False

    # Prints entire subtree rooted by self
    # For just self, use repr()
    def __str__(self):
        level = 0
        tree_by_levels = []
        while new_level := self[level]:
            tree_by_levels += new_level
            level += 1
        return f"{tree_by_levels}"

    # Prints the values and weights of self, parent, left, and right nodes, in that order
    # This method is SLOW and str() also uses this method to build your tree
    # Your solution should NOT use either, these are just to help visualize
    def __repr__(self):
        right_value = left_value = parent_value = self_value = "*"
        right_weight = left_weight = parent_weight = self_weight = "*"

        if self.right:
            right_value = self.right.value
            right_weight = self.right.weight

        if self.left:
            left_value = self.left.value
            left_weight = self.left.weight

        if self.parent:
            parent_value = self.parent.value
            parent_weight = self.parent.weight           

        if not self.is_empty():
            self_value = self.value
            self_weight = self.weight

        return (f"S:({self_value=},{self_weight=}) P:({parent_value},{parent_weight}) " + 
            f"L:({left_value},{left_weight}) R:({right_value},{right_weight})")

    # Check that node's value can be compared nodes already in the
    # Tree (we just do a comparison -- this means we can store any
    # Comparable [strings, numbers, etc] but all keys in a given tree
    # Are compatible)
    def __valid_key(self, key):
        if self.strict_checking:
            try:
                if key < self.value:  # confirm can compare
                    pass
            except Exception:
                raise (
                    ValueError,
                    "{key} must match type of existing tree values ",
                )

    def __valid_child(self, btwnode):
        self.__valid_key(btwnode.value)
        if self.strict_checking and btwnode.parent:
            raise (
                ValueError,
                "node to be added already has parent",
            )

    # Return a list of nodes at a given level
    def _level(self, key):
        if key == 0:
            return [repr(self)]

        rside = []
        lside = []
        if self.right:
            rside = self.right._level(key - 1)
        if self.left:
            lside = self.left._level(key - 1)
        return lside + rside

    def add_right(self, btwnode):
        self.__valid_child(btwnode)
        if self.strict_checking and self.right:
            raise (ValueError, "node already has a right child")
        self.right = btwnode
        btwnode.parent = self
        return self

    def add_left(self, btwnode):
        self.__valid_child(btwnode)
        if self.strict_checking and self.left:
            raise (ValueError, "node already has a left child")
        self.left = btwnode
        btwnode.parent = self
        return self

    def is_empty(self):
        if self.value == BinaryTreeWeighted.__emptyflag:
            return True
        else:
            return False

    def make_empty(self):
        self.value = BinaryTreeWeighted.__emptyflag


if __name__ == "__main__":
    # Initialize an empty tree
    test_tree = BinaryTreeWeighted()

    # This should print a completely Empty Node
    print(f"{test_tree.is_empty()=}")
    print(repr(test_tree))

    # Manually change the value
    test_tree.value = 6

    # This should print self with two empty children and empty parent
    print(f"{test_tree.is_empty()=}")
    print(repr(test_tree))

    # Add left and right children, manually adjust the weight of the parent
    test_tree.add_left(BinaryTreeWeighted(12))
    test_tree.add_right(BinaryTreeWeighted(11))
    test_tree.weight += 2

    # This should print everything so far
    print(repr(test_tree))

    # Add one more node on the far left, manually adjust the relevant weights
    test_tree.left.add_left(BinaryTreeWeighted(15))
    test_tree.weight += 1
    test_tree.left.weight += 1

    # Compare these two outputs
    # repr() only returns information about the current node and its immediate family
    # str() returns the repr() of every existing node from the given node and lower
    # str() can get confusing if you print the whole tree from the root
    print("repr():\n" + repr(test_tree))
    print("str():\n" + str(test_tree))


        
