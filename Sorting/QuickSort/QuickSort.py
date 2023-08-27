def QuickSort(A,l,r):             
  if l>=r: return                 # если элементов 1 или меньше, выходим

  i,j = l,r
  x = A[(l+r)//2]

  while i<=j:
    while A[i] < x: i+=1          # увеличиваем правый индекс
    while A[j] > x: j-=1          # уменьшаем левый индекс

    if i<=j:                      # если индексы не пересеклись, то меняем элементы местами
      A[i], A[j] = A[j], A[i]
      i+=1
      j-=1

  QuickSort(A,l,j)               # сортируем левую часть 
  QuickSort(A,i,r)               # сортируем правую часть




T = [3,5,1,4,6,8,4,2,1,7,9,2,3,3,3]
print(T)
QuickSort(T,0,len(T)-1)
print(T)
