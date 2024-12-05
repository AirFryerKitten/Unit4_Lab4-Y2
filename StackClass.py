# Your Code & Heading go Here!
# Jonas York
# U4 L1
# Array Stack

class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = 0

  def push(self,element):
    """Adds one element to the stack"""
    self.__stack.append(element)
    self.__size += 1 

  def pop(self):
    """Removes the top item from stack and returns it"""
    if self.__is_empty():
      raise Exception("There is no items in the stack")
    else:
      item = self.__stack[-1]
      del self.__stack[-1]
      self.__size -= 1
      return item

  def top(self):
    """Returns the top element in stack"""
    if self.__is_empty():
      raise Exception("There is no items in the stack")
    else:
      return self.__stack[-1]

  def __is_empty(self):
    """Checks if stack has no items and returns a Boolean"""
    if len(self) == 0:
      return True
    else:
      return False

  def __len__(self):
    """Gets the size of stack"""
    return self.__size

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out