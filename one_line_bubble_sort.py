nums = [2,2,45,65,562,453,45,21,12,231]

def setitem(a, b, c):
    a[b] = c

bubbleSort = lambda numList: [[((lambda i=i, temp=[0]: [(setitem(temp, 0, numList[i]), setitem(numList, i, numList[i+1]) if numList[i+1] < numList[i] else None, setitem(numList, i+1, temp[0]) if numList[i+1] < temp[0] else None)])()) for i in range(len(numList) - 1)] for i in range(len(numList) - 1)]

print(nums)

bubbleSort(nums)

print(nums)
