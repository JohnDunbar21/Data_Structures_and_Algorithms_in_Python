# Nodes are the foundations of most data structures, containing data and links to other nodes.
#
# Each data structure adds additional constraints or behaviour to these features to create the desired structure.
#
# Below is the most fundamental implementation of a Node.

class Node:

  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node

# Getters can be implemented to retrieve data from a Node.

  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node

# Setters can also be implemented to modify data in a Node.

  def set_value(self, new_value):
    self.value = new_value

  def set_link_node(self, new_node):
    if isinstance(new_node, Node):
        self.link_node = new_node
    else:
        raise Exception("The node provided is of a different type, and so cannot be linked.")

