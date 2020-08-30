def bubble_sort(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


print(bubble_sort([5, 2, 3, 1, 1, 2]))