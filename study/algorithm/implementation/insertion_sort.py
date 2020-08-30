def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and x[j] > key:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
    return x


print(insertion_sort([5, 2, 3, 1, 1, 2]))
