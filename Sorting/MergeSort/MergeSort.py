def Merge(A,B): # Получает 2 Отсортированных массива, возвращает 1 отсортированный массив
  res = []
  i,j = 0,0
  id1 = len(A)
  id2 = len(B)

  while(i < id1 and j <id2):
    if A[i]<B[j]:
      res.append(A[i])
      i+=1
    else:
      res.append(B[j])
      j+=1
  
  while i<id1:
    res.append(A[i])
    i+=1

  while j <id2:
    res.append(B[j])
    j+=1

  return res


def MergeSort(A):
  if len(A) <= 1:            # массив из 1 элемента
    return A
  mid = len(A)//2            # выделяем середину массива
  left = MergeSort(A[:mid])  # сортируем левую часть [0 ; mid)
  right = MergeSort(A[mid:]) # сортируем правую часть [mid ; конец)
  return Merge(left,right)   # обединяем два отсортированный массива left и right



  ##################################################

  


A = [1,3,2,5,7,5,5,8,9,0]
B = MergeSort(A)
print(B)
