# Algorithm

## Array

| Data                    | Heap                        | Stack          |
| ----------------------- | --------------------------- | -------------- |
| Global, Static variable | Dynamic, Reference variable | Local variable |



## Sorting

> Keyword: [Bubble sort](#bubble-sort), [Counting sort](#counting-sort), [Selection sort](#selection-sort), [Quicksort](#quicksort), [Insertion sort](#insertion-sort), [Merge sort](#merge-sort) | [WIKI](https://en.wikipedia.org/wiki/Sorting_algorithm)



### Bubble sort

> Compare and swap

1. Compare two adjacent elements.
2. Swap if left-side element is bigger than right-side one.
3. Repeat until array is sorted.

```python
def bubble_sort(source):
    for i in range(len(source)-1, 0, -1):
        for j in range(0, i):
            if source[j] > source[j+1]:
                source[j], source[j+1] = source[j+1], source[j]
```



### Counting sort

> Non-swap

1. Count each number from source.
2. Accumulate element in count list.
3. Sort result list.

```python
def counting_sort(source, result, max_num):
    counts = [0] * (max_num+1)
    # Counting
    for i in range(len(result)):
        counts[source[i]] += 1
    # Accumulation
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # Sorting
    for i in range(len(source)-1, -1, -1):
        result[counts[source[i]]-1] = source[i]
        counts[source[i]] -= 1
s1 = [0, 4, 1, 3, 1, 2, 4, 1]
r1 = [0] * len(s1)
counting_sort(s1, r1, 4)
print(r1)
```



### Selection sort

> Compare and swap

1. Find a minimum in a given list.
2. Swap the minimum value with a first value of a list.
3. Exclude the minimum value and repeat until last.

```python
def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
arr = [64, 25, 10, 22, 11]
selection_sort(arr)
```



### Quicksort

### Insertion sort

### Merge sort



## Search

> Keyword: Brute-force search, Sequential search, Binary search | [WIKI](https://en.wikipedia.org/wiki/Search_algorithm)

### Brute-force search

### Sequential search

1. Find a value from first index.
2. If a value is same with a key, return the index.

```python
def seq_search(a, n, k):
    i = 0
    while i < n and a[i] != k:
        i+= 1
    if i < n: return i
    else: return -1
def seq_sort_search(a, n, k):
    i = 0
    while i < n and a[i] < k:
        i+= 1
    if i < n and k == a[i]: return i
    else: return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(seq_search(arr, len(arr), key))
print(seq_sort_search(arr, len(arr), key))
```



### Binary search

1. Pick a element which is in middle of a list.
2. Compare the value with a key.
3. If the value is smaller than a key, repeat binary search at left-half of a list.
4. If not, vice versa.
5. repeat until finding.

```python
def binary_search(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False
arr = [2, 4, 7, 9, 11, 19, 23]
for ar in arr:
    print(binary_search(arr, ar))
```



