def quick_sort(x):
    """This is quick sort function

    Args:
        x (list): unsorted list

    Returns:
        [list]: sorted list
    """
    if len(x) <= 1:
        return x
    mid = x[len(x)//2]
    less = []
    equal = []
    more = []
    for a in x:
        if a < mid:
            less.append(a)
        elif a > mid:
            more.append(a)
        else:
            equal.append(a)
    return quick_sort(less) + equal + quick_sort(more)


print(quick_sort([1, 5, 3, 2, 7, 2, 3, 4, 2, 45, 4, 1, 2, 43, 1, 1]))