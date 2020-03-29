from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front = None
    self.__back = None
    # TODO replace pass with any additional initializations you need.
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
      return '[ ]'
    list_str = '[ '
    cur = self.__front
    if self.__size == self.__capacity:
      for i in range(self.__size):
        list_str = list_str + str(self.__contents[cur])
        cur += 1
        cur = cur % self.__capacity
        if i != self.__size - 1:
          list_str = list_str + ', '
    else:
      while self.__contents[cur] is not None:
        list_str = list_str + str(self.__contents[cur])
        cur += 1
        cur = cur % self.__capacity
        if self.__contents[cur % self.__capacity] is not None:
          list_str = list_str + ', '
    list_str = list_str + ' ]'
    return list_str
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity = self.__capacity * 2
    temp = [None] * self.__capacity
    cur = self.__front
    for i in range(self.__size):
      temp[i] = self.__contents[(cur % self.__size)]
      cur += 1
    self.__contents = temp
    self.__front = 0
    self.__back = self.__size - 1
    
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == 0:
      self.__front = 0
      self.__back = 0
      self.__contents[self.__front] = val
    else:
      if self.__capacity == self.__size:
        self.__grow()
      loc = (self.__front + self.__capacity - 1) % self.__capacity
      self.__contents[loc] = val
    self.__size += 1
    if self.__size != 1:
      self.__front = self.__front - 1
      self.__front = (self.__front + self.__capacity) % self.__capacity
    

    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return
    remove = self.__contents[self.__front]
    self.__contents[self.__front] = None
    self.__front = (self.__front + 1) % self.__capacity
    self.__size -= 1
    return remove
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size==0:
      return
    return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == 0:
      self.__front = 0
      self.__back = 0
      self.__contents[self.__back] = val
    else:
      if self.__capacity == self.__size:
        self.__grow()
      loc = (self.__back + self.__capacity + 1) % self.__capacity
      self.__contents[loc] = val
    self.__size += 1
    if self.__size != 1:
      self.__back = self.__back + 1
      self.__back = (self.__back + self.__capacity) % self.__capacity
    
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return
    remove = self.__contents[self.__back]
    self.__contents[self.__back] = None
    self.__back = (self.__back - 1) % len(self.__contents)
    self.__size -= 1
    return remove

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return
    return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
