class LinkedListNode: # звено
  def __init__ (self,value):
    self.value = value
    self.next = None

class LinkedList: # связный список
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self,value):
    newNode = LinkedListNode(value) # создаем звено

    if self.head: # список непустой 
      self.tail.next = newNode
      self.tail = newNode

    else: # список пустой
      self.head = newNode
      self.tail = newNode
  
  def print(self):
    currentNode = self.head
    while(currentNode):
      print(currentNode.value)
      currentNode = currentNode.next


  def reverse(self):
    prevhead = self.head
    r = None

    while(self.head):
      tmp = self.head.next
      self.head.next = r
      r = self.head
      self.head = tmp
    
    self.head = r
    self.tail = prevhead

lll = LinkedList()

lll.append(1)
lll.append(2)
lll.append(3)
lll.append(4)
lll.append(5)
lll.append(6)

lll.reverse()

lll.print()

        



        
