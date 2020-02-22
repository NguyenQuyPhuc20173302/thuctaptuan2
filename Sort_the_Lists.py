# cho vào toàn bộ vào một danh sách và dùng thuật toán sắp xếp nhanh để xắp xếp
list1 = [1, 4, 7]
list2 = [1, 3, 4]
list3 = [2, 6]
list1.extend(list2)
list1.extend(list3)
list1.sort()
print(list1)
'''
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


quick_sort(list1, 0, len(list1) - 1)
print(list1)
'''
# độ phức tạp của thuật toán là 8*log(8)
