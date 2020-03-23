import time
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  # TODO replace pass with your base and recursive cases.
  pass
  print(n, s, a, d)
  print()

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == '__main__':
  start = time.clock()
  n = 3
  Hanoi(n)
  end = time.clock()
  print('computed Hanoi(' + str(n) + ') in ' + str(end - start) + ' seconds.')
