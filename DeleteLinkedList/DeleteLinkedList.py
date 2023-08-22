######### удаление элемента из списка 

class LinkedListNode:
  def __init__ (self,value):
    self.value = value
    self.next = None

class LinkedList:
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

####################################################################################################
  def delete(self,value):
    while(self.head and self.head.value == value):
      self.head = self.nead.next
    
    curNode = self.head 

    if curNode:
      while curNode.next:
        if curNode.next.value == value:
          curNode.next = curNode.next.next
        else:
          curNode = curNode.next
    if self.tail:
      if self.tail.value == value:
        self.tail = curNode

####################################################################################################





dll = LinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(2)
dll.append(4)
dll.append(2)
dll.append(4)

dll.delete(2)
dll.print()
