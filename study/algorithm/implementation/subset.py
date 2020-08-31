arr = [1, 2, 3]
N = len(arr)
A = [0] * N

def powerset(n, k, cursum):
    if cursum > 10:
        return
    if n == k:
        print(A)
        for i in range(N):
            if A[i]:
                print(arr[i], end=' ')
        print()
    else:
        A[k] = 1
        powerset(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset(n, k+1, cursum)


powerset(N, 0, 0)