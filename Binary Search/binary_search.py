

# Binary Search function definition (it returns the list index of the selected item or None in it's absence)
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Sorted Array Generator Function
def generate_sorted_array(size):
    arr_size = size
    element = 0
    sorted_array = []
    while arr_size > 0:
        sorted_array.append(element)
        element += 1
        arr_size -= 1
    return sorted_array


# Test case 1
sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(sortedList, 4))

# Test case 2
sortedList = generate_sorted_array(1024)
print(binary_search(sortedList, 4))
