# Linked lists are made up of a series of nodes pointing to each other in a one-way sequence.
#
# They will always contain a head node at the beginning of the list.
#
# The last node is called the tail node.
#
# Similar to generic nodes, we define a node class for Linked Lists.

class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    if isinstance(next_node, Node):
      self.next_node = next_node
    else:
      raise Exception("Node Type Error")

# Now we can define a basic Linked List.

class LinkedList:

  def __init__(self, value = None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

# To insert a new head node and preserve the original order, we can implement an 'insert_beginning' method.
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  
# To visualise the data stored in the list, we can stringify it as shown below.

  def stringify_list(self):
    current_node = self.head_node
    string_list = ""
    while current_node is not None:
      string_list += (str(current_node.get_value()) + "\n")
      current_node = current_node.get_next_node()
    return string_list

# To remove a node from the Linked List containing a specific value, we can implement a 'remove_node' method. This will remove the FIRST instance of this value.

  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      current_node = self.head_node.get_next_node()
      while current_node is not None:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

# Swapping elements in a Linked List can be done through the following 'swap_values' function. These will only swap the FIRST instances of each value.

def swap_values(val1, val2):

  node1_prev = None
  node2_prev = None
  node1 = self.head_node
  node2 = self.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    self.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    self.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)