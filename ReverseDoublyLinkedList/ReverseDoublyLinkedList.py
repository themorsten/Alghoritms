class DoublyLinkedListNode:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    newNode = DoublyLinkedListNode(value)

    if self.head: # списко непустой
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
    
    else:  # списко пустой
      self.head = newNode
      self.tail = newNode

  
  def print(self):
    curNode = self.head
    while(curNode):
      print(curNode.value)
      curNode = curNode.next

#################################################################################
  def reverse(self):
    headNode = self.head
    while(self.head):
      prevNode = self.head.prev
      nextNode = self.head.next
      self.head.prev = nextNode
      self.head.next = prevNode
      self.head = nextNode

    self.head = self.tail 
    self.tail = headNode

    
#################################################################################



dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.reverse()
dll.print()
