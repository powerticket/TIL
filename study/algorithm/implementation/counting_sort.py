def counting_sort(source, result, max_num):
    count = [0] * (max_num+1)
    for s in source:
        count[s] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in range(len(source)):
        result[count[source[i]]-1] = source[i]
        count[source[i]] -= 1
    return result

s1 = [0, 4, 1, 3, 1, 2, 4, 1]
r1 = [0] * len(s1)
counting_sort(s1, r1, 4)
print(r1)