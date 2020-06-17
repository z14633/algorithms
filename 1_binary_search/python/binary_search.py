# 第一个算法——二分查找法：思想：在一个有序的数组中，先找中间的

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    #内建函数这里记不清了，一时想不起来python要如何才能计算出数组的长度
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid - 1
        if list[mid] < item:
            low = mid + 1


arr = [1, 2, 4, 6, 9]

print(binary_search(arr, 6))

print(binary_search(arr, -1))
