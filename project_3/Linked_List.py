class Linked_List:
  
  class __Node:
    
    def __init__(self, val):

      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):

    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):

    return self.__size

  def append_element(self, val):

    newest = self.__Node(val)
    newest.next = self.__trailer
    newest.prev = self.__trailer.prev
    self.__trailer.prev = newest
    newest.prev.next = newest
    self.__size +=1

  def insert_element_at(self, val, index):

    if index >= self.__size or index < 0:
      raise IndexError
    newest = self.__Node(val)
    if index == 0:
      cur = self.__header
    elif index < (self.__size / 2):
      count = 1
      cur = self.__header.next
      while count < index:
        cur = cur.next
        count += 1
    else:
      cur = self.__trailer.prev
      count = self.__size
      while count > index :
        cur = cur.prev
        count -= 1
    newest.prev = cur.next.prev
    cur.next.prev = newest
    newest.next = cur.next
    cur.next = newest
    self.__size +=1

  def remove_element_at(self, index):

    if index >= self.__size or index < 0:  #out of bounds
      raise IndexError
    elif index == 0:  #remove at beginning
      to_return = self.__header.next.val
      self.__header.next = self.__header.next.next
      self.__header.next.prev = self.__header
    elif index == self.__size-1:  #remove at end
      to_return = self.__trailer.prev.val
      self.__trailer.prev.prev.next = self.__trailer
      self.__trailer.prev = self.__trailer.prev.prev
    else:
      if index < self.__size / 2:  
        cur = self.__header.next
        count = 1
        while count < index:
          cur = cur.next
          count += 1
      else:
        cur = self.__trailer.prev
        count = self.__size
        while count > index:
          cur = cur.prev
          count -= 1
      to_return = cur.next.val
      cur.next = cur.next.next
      cur.next.prev = cur
    self.__size -=1
    return to_return
    
    

  def get_element_at(self, index):

    if index >= self.__size or index < 0:
      raise IndexError
    if index < self.__size+1 / 2:
      cur = self.__header.next
      count = 0
      while(count != index):
        count +=1
        cur = cur.next
      return cur.val
    else:
      cur = self.__trailer.prev
      count = self.__size - 1
      while(count != index):
        count -= 1
        cur = cur.prev
      return cur.val




  def rotate_left(self):

    if self.__size == 0 or self.__size == 1:
      return
    current = self.__trailer.prev
    this = self.__header.next
    current.next = self.__header.next
    self.__header.next.prev = current
    self.__header.next = this.next
    self.__header.next.prev = self.__header
    this.next = self.__trailer

    
    
  def __str__(self):

    if self.__size == 0:
      return '[ ]'
    cur = self.__header.next
    list_str = '[ '
    while cur is not self.__trailer:
      list_str = list_str + str(cur.val)
      if cur.next is not self.__trailer:
        list_str = list_str + ', '
      cur = cur.next
    list_str = list_str + ' ]'
    return list_str
    

  def __iter__(self):

    self.__iter_index = 0
    return self

  def __next__(self):

    if self.__iter_index == self.__size:
      raise StopIteration
    to_return = self.get_element_at(self.__iter_index)
    self.__iter_index = self.__iter_index + 1
    return to_return

if __name__ == '__main__':

  my_list = Linked_List()
  print(my_list)  #list should be empty
  print('My list has ' + str(len(my_list)) + ' elements')   #0 elements

  try:
    my_list.append_element(4)
    my_list.append_element(-3)
    my_list.append_element(8)
    my_list.append_element(-1)
  except MemoryError:
    print("append dont work")
  
  print(my_list) #list should be 4, -3, 8, -1
  print('My list has ' + str(len(my_list)) + ' elements')  #should have 4 elements

  try:
    my_list.insert_element_at(14, 2)
  except IndexError:
    print("This message should not pop up, otherwise insert in middle doenst work")
  
  print(my_list) #list should be 4 -3 14 8 -1
  print('My list has ' + str(len(my_list)) + ' elements') #should have 5 elements

  try:
    my_list.insert_element_at(-7,8)
  except IndexError:
    print("Index error caught correctly, index out of bounds")   #index error should occur, index 8 is out of bounds

  print(my_list)

  try:
    my_list.insert_element_at(4, len(my_list))
  except IndexError:
    print("Caught correctly, cannot append with insert element") #error should result
  
  print(my_list)

  try:
    print(my_list.remove_element_at(3))  #removes 8, list becomes 4 -3 14 -1, should also print 8
  except IndexError:
    print("Should not pop up, crash with remove in middle")
  
  print(my_list)
  print('My list has ' + str(len(my_list)) + ' elements') # 4 elements

  try:
    my_list.remove_element_at(6)
  except IndexError:
    print("Working fine, caught index out of bounds for remove")  #error should be caught

  print(my_list)

  try:
    print(my_list.remove_element_at(0)) #removes correctly at beginning, should also print 4, new list is -3 14 -1
  except IndexError:
    print("Something is wrong, check removing at beginning of list")

  print(my_list) #list should be -3 14 -1
  print('My list has ' + str(len(my_list)) + ' elements')

  try:
    print(my_list.remove_element_at(len(my_list)-1)) #removes correctly at end, should also print -1
  except IndexError:
    print("Should not pop up, error with removing at tail")
  
  print(my_list) #list should be -3 14
  print('My list has ' + str(len(my_list)) + ' elements') # 2 elements

  try:
    my_list.append_element(15)
    my_list.insert_element_at(-5,2)
    my_list.append_element(2)
    my_list.insert_element_at(6,3)
  except IndexError:
    print("something is broken with either append or insert")

  print(my_list)  # new list is -3 14 -5 6 15 2
  print('My list has ' + str(len(my_list)) + ' elements')  # 6 elements

  try:
    print(my_list.get_element_at(2))  #get element should be -5
  except IndexError:
    print("Get element is working incorrectly")

  try:
    print(my_list.get_element_at(8))
  except IndexError:
    print('Index error caught correctly for get element') #index out of bounds should be raised

  print(my_list)

  print('Testing rotate left')
  my_list.rotate_left()
  print(my_list)  # list should be 14 -5 6 15 2 -3 

  print('Testing iterator') # prints 14 -5 6 15 2 -3 on a new line every time
  for val in my_list:
    print(val)
  print