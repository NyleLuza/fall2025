"""
Problem 4:
Write an Insertion Sort algorithm (Insertion Sort is discussed in Section 7.2)
that uses Binary Search to find the position where the next insertion should
take place.
"""


def insertion_sort(data, x, start, end):
    mid = (start + end) // 2
    length = end - start
    print(start, mid ,end)
    # base case
    if length == 1:
        if x > data[start] and x > data[end]:
            print("1")
            return end + 1
        if x < data[start]:
            print("2")
            return start
        if x > data[start] and x < data[end]:
            print("3", start)
            return start + 1
        
    elif data[mid] > x:
        insertion_sort(data, x, start, mid - 1)
    elif data[mid] < x:
        insertion_sort(data, x, mid + 1, end)

data = [2, 6, 9, 18, 22]
x = 3
start = 0
end = len(data) - 1
d = insertion_sort(data, x, start, end)
print(d)

    

