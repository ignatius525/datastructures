from Linked_List import Linked_List


def Josephus(ll): 
  while len(ll) != 1:
    ll.rotate_left()
    ll.remove_element_at(0)
    print(ll)
  print('The survivor is ' + str(ll.get_element_at(0)))


if __name__ == '__main__':
  n = int(input("Input the total number of people: "))
  ll = Linked_List()
  for k in range(1, n+1):
    ll.append_element(k)  
  print("Initial order:", ll)
  Josephus(ll)
