
t = [1, 3, 4, 6, 8, 10]


def binarySearch(list, num):
    index = _binarySearch(list, 0, len(list) - 1, num)
    return index

def _binarySearch(list, left, right, num):
   mid = int((left + right) / 2)
   if left > right:
       return -1
   else:
       if num > list[mid]:
           return _binarySearch(list, mid + 1, right, num)
       elif num < list[mid]:
           return _binarySearch(list, left, mid - 1, num)
       else:
           return mid


def binarySearch2(list, num):

    l = 0
    r = len(list)
    index = -1
    while l <= r:
        mid = int(l*0.5 + r*0.5)
        if num < list[mid]:
            r = mid - 1
        elif num > list[mid]:
            l = mid + 1
        else:
            l += 1
            index = mid

    return index



if __name__ == '__main__':
    print('serching...')
    print(binarySearch2(t, 8))