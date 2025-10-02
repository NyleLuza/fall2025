"""
Problem 2:
The maximum number of comparisons that the algorithm must perform before finding
a given item or concluding it isn't in the list is logn since we are splitting the
the problem size in half for each comparison

Problem 7:
Find the largest item in a list of n items

Analysis:
reccurence relation -> T(n) = 2*T(n/2) + O(1)
This is our recurrence relation since we our breaking the problem size in half for each
recursive call and so we need to solve two problems of size n/2 and everything outside of
this recursive call takes constant time. Only thing we are doing is setting our mid point and
returning the single element at our base case. So according to master theorem case 1, our alg
runs in linear time T(n) = O(n).

def largest_item(start, end, items):
    mid = start + (end - start) // 2
    if start == end:
        return items[start]
    largest_val = max(largest_item(start, mid, items), largest_item(mid+1, end, items))
    return largest_val

x = largest_item(0, 4, [12, 3, 4, 20, 8])
print(x)

Problem 8: 
Use Mergesort (Algorithms 2.2 and 2.4) to sort the following list. Show the
actions step by step.

def merge(arr1, arr2):
    merged_arr = []
    i = 0 # pointer for arr1
    j = 0 # pointer for arr2
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<= arr2[j]):          # since arr1 element is less, then we append to merged arr
            merged_arr.append(arr1[i])
            i+=1                        # move to next element in arr1
        else:
            merged_arr.append(arr2[j])  # arr2 elem is less so we merge that and incr j
            j+=1
    merged_arr.extend(arr1[i:])  # adds leftovers of arr1
    merged_arr.extend(arr2[j:])  # adds leftovers of arr2
    return merged_arr
def divide(start, end, items):
    mid = start + (end - start) // 2
    if start == end:
        return [items[start]]
    else:
        left = divide(start, mid, items)
        right = divide(mid+1, end, items)
        combine = merge(left, right)
    return combine
items = [123, 34, 189, 56, 150, 12, 9, 240]
print(divide(0, len(items)-1, items))

Problem 9:
On Document

Problem 15:
a) T(n) = 5*T(n/3) + g(n)
b) T(n) = 5*T(n/3) + O(n) = O(n) => O(n^1.46497) according to case 3 of master theorem
   T(n) belong to O(n^(logbaseb(a))) if a > b^k. a = 5; b = 3; k = 1 (since the outer work is linear)
c) T(n) = 5*T(n/3) + O(n^2) => O(n^2) because according to case 1 of master theorem, a < b^k, since
   a = 5, b = 3, and k = 2, so this satisifies case 1. T(n) belongs to O(n^k) which is O(n^2)
d) T(3^m) = O(3^, * (5/3)^m) = O(n^1.46497)

Problem 17:
Towers of Hanoi alg
def move_stack(n, src, aux, dst):
    if n == 0: 
        return
    move_stack(n-1, src, dst, aux)
    dst.append(src.pop())      # move top disk
    move_stack(n-1, aux, src, dst)

# Example:
A = [4,3,2,1]  # bottom->top
B = []
C = []
move_stack(4, A, B, C)
print(C)

a) Recurrence Relation: S(n) = 2S(n-1) + 1, S(1) = 1
Base Case: n=1; 2^1 - 1 = 1
Step: We assume S(n-1) = 2^(n-1)-1
    Then S(n) = 2(2^(n-1)-1) + 1 = 2^n - 2 + 1 = 2^n -1
S(n) = 2^n - 1 for all n>=1

Problem 19:
On Document

Problem 20:
On Document

Problem 34:
def exchange_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]   # swap
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]                      # first element is pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# call on both functions
print(quicksort([64, 25, 12, 22, 11]))
print(exchange_sort([64, 25, 12, 22, 11]))

a) Find the lower bound for n that justifies
application of the Quicksort algorithm with its overhead.
    - For really small arrays the exchange sort is faster then quicksort, however when n grows
      the quicksort algorithm becomes the better option.

Problem 40:
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return None  # empty matrix
    
    n, m = len(matrix), len(matrix[0])
    
    # start from top-right corner
    row, col = 0, m - 1
    
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row, col)   # found at (row, col)
        elif matrix[row][col] > target:
            col -= 1           # move left
        else:
            row += 1           # move down
    
    return None  # not found
"""
