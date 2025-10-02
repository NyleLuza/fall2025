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
"""
