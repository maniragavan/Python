list = [2, 13, 24, 36, 45, 65, 89,98]

# search item by using position  lower  , mid , upper position...
pos = 0
def bSearch(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2  # find mid position of the list

        if list[mid] == n:
            globals()['pos'] = mid
            print('found at', mid)
            return True
        elif list[mid] < n:
            l = mid+1     # move lower to mid position in  search value higher than mid
        else:
            u = mid -1

    return False

bSearch(list,89)