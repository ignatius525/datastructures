class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation

    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    newest = self.__Node(val)
    newest.next = self.__trailer
    newest.prev = self.__trailer.prev
    self.__trailer.prev = newest
    newest.prev.next = newest
    self.__size +=1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    if index > self.__size:
      return IndexError
    if index == self.__size:
      return self.append_element(val)
    newest = self.__Node(val)
    cur = self.__header.next
    count = 1
    while count < index:
      cur = cur.next
      count += 1
    newest.prev = cur.next.prev
    cur.next.prev = newest
    newest.next = cur.next
    cur.next = newest
    self.__size +=1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index > self.__size:
      return IndexError
    cur = self.__header.next
    count = 1
    while count < index-1:
      cur = cur.next
      count += 1
    cur.next = cur.prev
    cur.prev = cur.next 
    self.__size -=1
    pass
    

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size:
      return IndexError
    cur = self.__header.next
    count = 0
    while(cur):
      if (count == index):
        return cur.val
      count +=1
      cur = cur.next


     

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    pass
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    if self.__size == 0:
      return '[]'
    cur = self.__header.next
    list_str = '['
    while cur is not self.__trailer:
      list_str = list_str + str(cur.val)
      if cur.next is not self.__trailer:
        list_str = list_str + ', '
      cur = cur.next
    list_str = list_str + ']'
    return list_str
    

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_index = 0
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__iter_index == self.__size:
      return StopIteration
    
    pass

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  my_list = Linked_List()
  my_list.append_element(2)
  my_list.append_element(4)
  my_list.append_element(-3)
  my_list.append_element(69)
  print(my_list)
  print(len(my_list))
  print(my_list.get_element_at(1))
  my_list.insert_element_at(5,1)
  print(my_list)
  my_list.remove_element_at(2)
  print(my_list)