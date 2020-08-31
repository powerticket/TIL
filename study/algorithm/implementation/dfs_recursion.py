def dfs(v):
    print(v, end=' ')
    visited[v] = 1

    for w in range(1, V+1):
        if adj[v][w] and not visited[w]:
            dfs(w)


V, E = 7, 8 # map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # list(map(int, input().split()))
visited = [0] * (V+1)
for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

dfs(1)