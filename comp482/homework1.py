"""
Problem 4:
Write an Insertion Sort algorithm (Insertion Sort is discussed in Section 7.2)
that uses Binary Search to find the position where the next insertion should
take place.
"""

def maximize(data):
    list1 = [data[0]]
    list2 = [data[1]]

    left_total = data[0]
    right_total = data[1]

    for i in range(2, len(data)-1):
        if left_total >= right_total:
            list2.append(data[i])
        else:
            list1.append(data[i])
    max = abs(sum(list1) - sum(list2))
    return max



def insertion_sort(data, x, start, end):
    mid = (start + end) // 2
    print(start, mid ,end)
    # base case
    if start >= end:
        if x <= data[start]:
            return start
        else:
            return start + 1
    elif data[mid] >= x:
        return insertion_sort(data, x, start, mid - 1)
    elif data[mid] < x:
        return insertion_sort(data, x, mid + 1, end)

data = [2, 6, 9, 18, 22, 33]
x = 19
start = 0
end = len(data) - 1
max = maximize(data)
#d = insertion_sort(data, x, start, end)
print("Answer: ", max)

    

