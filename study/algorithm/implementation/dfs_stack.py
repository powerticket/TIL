def dfs(n):
    stack = [0] * V
    visited = [0] * (V+1)
    top = -1

    top += 1
    stack[top] = n
    visited[n] = 1
    print(n, end=' ')
    while top >= 0:
        n = stack[top]
        top -= 1
        for i in range(1, V+1):
            if adj[n][i] and not visited[i]:
                top += 1
                stack[top] = i
                visited[i] = 1
                print(i, end=' ')


V, E = 7, 8 # map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # list(map(int, input().split()))
for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

dfs(1)