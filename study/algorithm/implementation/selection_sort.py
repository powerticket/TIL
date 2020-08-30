def selection_sort(x):
    for i in range(len(x)-1):
        min_idx = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    return x


print(selection_sort([0, 4, 1, 3, 1, 2, 4, 1]))