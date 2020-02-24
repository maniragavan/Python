def SelectionSort(list):

       for i in  range(len(list)-1):
           minpos = i
           for j in range(i,len(list)):
               if list[j] < list[minpos]:
                   minpos = j

           temp = list[i]
           list[i] = list[minpos]
           list[minpos] =temp

       print(list)




# from Git
list = [2, 13, 24, 5, 36, 45, 9, 65, 89,98]

SelectionSort(list)
