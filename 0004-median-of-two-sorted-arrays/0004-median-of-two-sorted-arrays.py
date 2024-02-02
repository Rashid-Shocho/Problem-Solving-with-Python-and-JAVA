class Solution:
    def findMedianSortedArrays(self, array1: List[int], array2: List[int]) -> float:
      #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 4, 4, 4]
      merged_arr=[]
      # [1, 1, 2, 3, 5, 7, 8, 40, 90, 98, 100]
      i = 0
      j = 0
      for k in range(len(array1) + len(array2)):
        try:
          if array1[i]==array2[j]:
            merged_arr.append(array1[i])
            merged_arr.append(array2[j])
            array1[i] = float('inf')
            array2[j] = float('inf')
            i+=1
            j+=1

          elif(array1[i]>array2[j]):
            merged_arr.append(array2[j])
            array2[j] = float('inf')
            j+=1
          elif(array1[i]<array2[j]):
            merged_arr.append(array1[i])
            array1[i] = float('inf')
            i+=1
        except:

          for m in array1:
            if m!= float('inf'):
              merged_arr.append(m)
          for n in array2:
            if n!= float('inf'):
              merged_arr.append(n)
          break


      if len(merged_arr)%2 == 0:
        return ((merged_arr[len(merged_arr)//2]+merged_arr[(len(merged_arr)//2)-1])/2)
      else:
        return (merged_arr[len(merged_arr)//2])