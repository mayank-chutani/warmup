""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def util(node, min, max):

    if node is None:
        return True

    if node.data < min or node.data > max:
        return False

    return util(node.left, min, node.data - 1) and util(node.right, node.data + 1, max)


def check_binary_search_tree_(root):
    if root is None:
        return True

    node = root

    return util(node, -1, float('inf'))
