
import random

def selectSort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]
                print("", list[i], " ", list[j])
    return list

def insertSort(list):
    for i in range(1, len(list)):
        for j in range(i - 1, -1, -1):
            if list[j + 1] < list[j]:
                list[j+1], list[j] = list[j], list[j+1]
            print(list)
    return list

def quickSort(list):






if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(10 - i)
    print(arr)
    # selectSort(arr)
    insertSort(arr)
    print(arr)

