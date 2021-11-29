
class Tree:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def add_child(self, child):
        if self.children is None:
            self.children = [child]
        else:
            self.children.append(child)

    def __repr__(self):
        return self.val


def tree_from_sequence(sequence):
    trees = [Tree(val=i) for i in range(len(sequence))]
    for pos, par in enumerate(sequence):
        if par == -1:
            root = pos
        else:
            trees[par].add_child(trees[pos])
    return trees[root]

def traverse(tree):
    return _traverse(tree, 1)

def _traverse(tree, level):
    if tree.children is None:
        return '{}(val={})'.format(type(tree).__name__,tree.val)
    else:
        indentation = '\t' * level
        child_strings = '\n'.join(['{}{}'.format(indentation, _traverse(child, level +1)) for child in tree.children])
        return '{}(val={}, children=\n{})'.format(type(tree).__name__,tree.val, child_strings)


def calculate_height(tree):
    if tree is None:
        return 0
    else:
        return _calculate_height(tree, 1)


def _calculate_height(tree, height):
    if tree.children is None:
        return height
    else:
        heights = [_calculate_height(child, height + 1) for child in tree.children]
        return max(heights)
