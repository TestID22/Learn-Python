def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight)
        guess = list[mid]
        if guess == mid:
            return mid
        if guess > mid:
            hight = mid - 1
        else:
            hight = mid + 1
    return None

my_list = [1,4,6,7,8,12,56,3,2,6,1,7]
my_list.sort()

print(binary_search(my_list, 3))
