def sort(list):

    for i in range(len(list)-1, 0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)

list = [2, 13, 24, 5, 36, 45, 9, 65, 89,98]

sort(list)