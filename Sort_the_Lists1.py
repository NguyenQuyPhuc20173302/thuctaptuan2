list1 = [1, 4, 7]
list2 = [1, 3, 4]
list3 = [2, 6]
count1 = 0
count2 = 0
count3 = 0
total_len = len(list1) + len(list2) + len(list3)
ls = []


# hàm này từ 2 dành sách rồi chuyển thành 1 danh sách đã được sắp xếp
def Sort_two_list(a1, a2):
    a = []
    dem1 = 0
    dem2 = 0
    while 1:
        if dem1 == len(a1):
            a.extend(a2[dem2:])
            return a
        if dem2 == len(a2):
            a.extend(a1[dem1:])
            return a

        if a1[dem1] < a2[dem2]:
            a.append(a1[dem1])
            dem1 += 1
        else:
            a.append(a2[dem2])
            dem2 += 1


list1 = Sort_two_list(list1, list2)
list1 = Sort_two_list(list1, list3)
print(list1)
