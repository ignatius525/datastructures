import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  def test_empty_list_string(self):
    self.assertEqual('[ ]', str(self.__deque), "Empty list should print as [ ]")
    self.assertEqual('[ ]', str(self.__stack), "Empty list should print as [ ]")
    self.assertEqual('[ ]', str(self.__queue), "Empty list should print as [ ]")
  
  def test_add_to_empty(self):
    self.__stack.push('Test')
    self.__queue.enqueue('Test')
    self.__deque.push_front('Test')
    self.assertEqual('[ Test ]', str(self.__deque))
    self.assertEqual('[ Test ]', str(self.__stack))
    self.assertEqual('[ Test ]', str(self.__queue))

  def test_push_to_stack_size_one(self):
    self.__stack.push('Royale')
    self.__stack.push('Victory')
    self.assertEqual('[ Victory, Royale ]', str(self.__stack))

  def test_enqueue_size_one(self):
    self.__queue.enqueue('Victory')
    self.__queue.enqueue('Royale')
    self.assertEqual('[ Victory, Royale ]', str(self.__queue))

  def test_push_front_deque_size_one(self):
    self.__deque.push_front('Royale')
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory, Royale ]', str(self.__deque))

  def test_push_back_deque_size_one(self):
    self.__deque.push_front('Victory')
    self.__deque.push_back('Royale')
    self.assertEqual('[ Victory, Royale ]', str(self.__deque))

  def test_push_to_stack_size_two(self):
    self.__stack.push('You')
    self.__stack.push('Love')
    self.__stack.push('I')
    self.assertEqual('[ I, Love, You ]', str(self.__stack))

  def test_push_to_stack_size_three(self):
    self.__stack.push('McKinney')
    self.__stack.push('Alf')
    self.__stack.push('Hope')
    self.__stack.push('Katherine')
    self.assertEqual('[ Katherine, Hope, Alf, McKinney ]', str(self.__stack))

  def test_enqueue_size_two(self):
    self.__queue.enqueue('I')
    self.__queue.enqueue('Love')
    self.__queue.enqueue('You')
    self.assertEqual('[ I, Love, You ]', str(self.__queue))

  def test_enqueue_size_three(self):
    self.__queue.enqueue('Katherine')
    self.__queue.enqueue('Hope')
    self.__queue.enqueue('Alf')
    self.__queue.enqueue('McKinney')
    self.assertEqual('[ Katherine, Hope, Alf, McKinney ]', str(self.__queue))

  def test_push_front_size_two(self):
    self.__deque.push_front('Love')
    self.__deque.push_back('You')
    self.__deque.push_front('I')
    self.assertEqual('[ I, Love, You ]', str(self.__deque))

  def test_push_back_size_two(self):
    self.__deque.push_front('I')
    self.__deque.push_back('Love')
    self.__deque.push_back('You')
    self.assertEqual('[ I, Love, You ]', str(self.__deque))

  def test_push_front_size_three(self):
    self.__deque.push_front('One')
    self.__deque.push_front('Two')
    self.__deque.push_front('Three')
    self.__deque.push_front('Four')
    self.assertEqual('[ Four, Three, Two, One ]', str(self.__deque))

  def test_push_back_size_three(self):
    self.__deque.push_front('One')
    self.__deque.push_front('Two')
    self.__deque.push_front('Three')
    self.__deque.push_back('Four')
    self.assertEqual('[ Three, Two, One, Four ]', str(self.__deque))

  def test_push_front_size_four(self):
    self.__deque.push_front('One')
    self.__deque.push_front('Two')
    self.__deque.push_front('Three')
    self.__deque.push_front('Four')
    self.__deque.push_front('Five')
    self.assertEqual('[ Five, Four, Three, Two, One ]', str(self.__deque))

  def test_push_back_size_four(self):
    self.__deque.push_front('One')
    self.__deque.push_front('Two')
    self.__deque.push_front('Three')
    self.__deque.push_front('Four')
    self.__deque.push_back('Five')
    self.assertEqual('[ Four, Three, Two, One, Five ]', str(self.__deque))

  def test_pop_stack_return(self):
    self.__stack.push('One')
    self.__stack.push('Two')
    self.__stack.push('Three')
    self.__stack.push('Four')
    returned = self.__stack.pop()
    self.assertEqual('Four', returned)
  
  def test_pop_stack_remaining_list(self):
    self.__stack.push('One')
    self.__stack.push('Two')
    self.__stack.push('Three')
    self.__stack.push('Four')
    returned = self.__stack.pop()
    self.assertEqual('[ Three, Two, One ]', str(self.__stack))

  def test_pop_queue_return(self):
    self.__queue.enqueue('One')
    self.__queue.enqueue('Two')
    self.__queue.enqueue('Three')
    self.__queue.enqueue('Four')
    returned = self.__queue.dequeue()
    self.assertEqual('One', returned)

  def test_pop_queue_remaining_list(self):
    self.__queue.enqueue('One')
    self.__queue.enqueue('Two')
    self.__queue.enqueue('Three')
    self.__queue.enqueue('Four')
    returned = self.__queue.dequeue()
    self.assertEqual('[ Two, Three, Four ]', str(self.__queue))

  def test_deque_pop_back_return(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.pop_back()
    self.assertEqual('Boys', returned)

  def test_deque_pop_back_remaining(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.pop_back()
    self.assertEqual('[ For, The, Tali ]', str(self.__deque))

  def test_deque_pop_front_return(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.pop_front()
    self.assertEqual('For', returned)

  def test_deque_pop_front_remaining(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.pop_front()
    self.assertEqual('[ The, Tali, Boys ]', str(self.__deque))

  def test_stack_peek(self):
    self.__stack.push('One')
    self.__stack.push('Two')
    self.__stack.push('Three')
    self.__stack.push('Four')
    peek = self.__stack.peek()
    self.assertEqual('Four', peek)

  def test_stack_peek_remainder(self):
    self.__stack.push('One')
    self.__stack.push('Two')
    self.__stack.push('Three')
    self.__stack.push('Four')
    peek = self.__stack.peek()
    self.assertEqual('[ Four, Three, Two, One ]', str(self.__stack))

  def test_queue_peek(self):
    self.__queue.enqueue('One')
    self.__queue.enqueue('Two')
    self.__queue.enqueue('Three')
    self.__queue.enqueue('Four')
    peek = self.__queue.peek()
    self.assertEqual('One', peek)

  def test_queue_peek_remainder(self):
    self.__queue.enqueue('One')
    self.__queue.enqueue('Two')
    self.__queue.enqueue('Three')
    self.__queue.enqueue('Four')
    peek = self.__queue.peek()
    self.assertEqual('[ One, Two, Three, Four ]', str(self.__queue))
  
  def test_deque_peek_back_return(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.peek_back()
    self.assertEqual('Boys', returned)

  def test_deque_peek_back_remaining(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.peek_back()
    self.assertEqual('[ For, The, Tali, Boys ]', str(self.__deque))

  def test_deque_peek_front_return(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.peek_front()
    self.assertEqual('For', returned)

  def test_deque_peek_front_remaining(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    returned = self.__deque.peek_front()
    self.assertEqual('[ For, The, Tali, Boys ]', str(self.__deque))

  def test_deque_length(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    self.assertEqual(4,len(self.__deque))

  def test_stack_length(self):
    self.__stack.push('For')
    self.__stack.push('The')
    self.__stack.push('Tali')
    self.__stack.push('Boys')
    self.assertEqual(4,len(self.__stack))

  def test_queue_length(self):
    self.__queue.enqueue('For')
    self.__queue.enqueue('The')
    self.__queue.enqueue('Tali')
    self.__queue.enqueue('Boys')
    self.assertEqual(4, len(self.__queue))

  def test_deque_length_after_pop_front(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    self.__deque.pop_front()
    self.assertEqual(3,len(self.__deque))
  
  def test_deque_length_after_pop_back(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    self.__deque.pop_back()
    self.assertEqual(3,len(self.__deque))

  def test_stack_length_after_pop(self):
    self.__stack.push('For')
    self.__stack.push('The')
    self.__stack.push('Tali')
    self.__stack.push('Boys')
    self.__stack.pop()
    self.assertEqual(3,len(self.__stack))

  def test_queue_length_after_dequeue(self):
    self.__queue.enqueue('For')
    self.__queue.enqueue('The')
    self.__queue.enqueue('Tali')
    self.__queue.enqueue('Boys')
    self.__queue.dequeue()
    self.assertEqual(3, len(self.__queue))

  def test_deque_length_after_peek_front(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    self.__deque.peek_front()
    self.assertEqual(4,len(self.__deque))

  def test_deque_length_after_peek_back(self):
    self.__deque.push_back('For')
    self.__deque.push_back('The')
    self.__deque.push_back('Tali')
    self.__deque.push_back('Boys')
    self.__deque.peek_back()
    self.assertEqual(4,len(self.__deque))

  def test_stack_length_after_peek(self):
    self.__stack.push('For')
    self.__stack.push('The')
    self.__stack.push('Tali')
    self.__stack.push('Boys')
    self.__stack.peek()
    self.assertEqual(4,len(self.__stack))

  def test_queue_length_after_peek(self):
    self.__queue.enqueue('For')
    self.__queue.enqueue('The')
    self.__queue.enqueue('Tali')
    self.__queue.enqueue('Boys')
    self.__queue.peek()
    self.assertEqual(4, len(self.__queue))

  def test_empty_stack_peek_return(self):
    to_return = self.__stack.peek()
    self.assertEqual(None, to_return)

  def test_empty_stack_peek_remainder(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_queue_peek_remainder(self):
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_queue_peek_return(self):
    to_return = self.__queue.peek()
    self.assertEqual(None, to_return)

  def test_empty_deque_peek_front_return(self):
    to_return = self.__deque.peek_front()
    self.assertEqual(None, to_return)

  def test_empty_deque_peek_front_remainder(self):
    self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_deque_peek_back_return(self):
    to_return = self.__deque.peek_back()
    self.assertEqual(None, to_return)

  def test_empty_deque_peek_back_remainder(self):
    self.__deque.peek_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_stack_pop_return(self):
    to_return = self.__stack.pop()
    self.assertEqual(None, to_return)

  def test_empty_stack_pop_remainder(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_queue_dequeue_remainder(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_queue_dequeue_return(self):
    to_return = self.__queue.dequeue()
    self.assertEqual(None, to_return)

  def test_empty_deque_pop_front_return(self):
    to_return = self.__deque.pop_front()
    self.assertEqual(None, to_return)

  def test_empty_deque_pop_front_remainder(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_deque_pop_back_return(self):
    to_return = self.__deque.pop_back()
    self.assertEqual(None, to_return)

  def test_empty_deque_pop_back_remainder(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))



  

if __name__ == '__main__':
  unittest.main()

