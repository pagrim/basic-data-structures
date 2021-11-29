from tree import Tree, tree_from_sequence, calculate_height, traverse

import pytest


@pytest.fixture
def mock_tree_seq():
    return [4, -1, 4, 1, 1]


def test_from_seq(mock_tree_seq):
    root = tree_from_sequence(mock_tree_seq)
    assert(len(root.children) == 2 and len(root.children[1].children) == 2)


def test_calculate_height(mock_tree_seq):
    tree = tree_from_sequence(mock_tree_seq)
    assert(calculate_height(tree) == 3)


def test_calculate_height_none():
    assert(calculate_height(None)==0)


def test_traverse():
    tree = Tree(val=4, children=[Tree(val=0), Tree(val=2)])
    traversed = 'Tree(val=4, children=\n\tTree(val=0)\n\tTree(val=2))'
    assert traverse(tree) == traversed
