# Algorithm Problem Solving

## Stack

Abstract data type of stacked data

LIFO: Last-In, First-Out



### Main operation

push - insert data to the top of data

pop - delete data from the top of data

isEmpty - check the stack is empty or not

peek - return the item of the top



### Implementation

![File:Lifo stack.png](https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png)



```python
# C Language Style

def push(item):
    global top
    if top > 99:
        print("Stack is full!")
        return
    else:
        top += 1
        stack[top] = item


def pop():
    global top
    if top < 0:
        print("Stack is empty!")
        return
    else:
        result = stack[top]
        top -= 1
    return result


stack = [0] * 100
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())
```

```python
# Python Style

stack = list()

stack.append(1)
stack.append(2)
stack.append(3)
if stack:
    print(stack.pop())
if stack:
    print(stack.pop())
if stack:
    print(stack.pop())
if stack:
    print(stack.pop())
```



## Recursive function

basis

inductive

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
```

```python
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
```



## Memoization

```python
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]


memo = [0, 1]
fibo1(30)
```



## Dynamic Programming

```python
def fibo3(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
```



## DFS

Depth First Search



### Implementation

```python
# recursive method

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


N, E = 7, 8
# N, E = map(int, input().split())
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# temp = list(map(int, input().split()))
G = [[0] * (N+1) for _ in range(N+1)]
arr = [[0] * N for _ in range(N)]
visited = [0] * (N+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e], G[e][s] = 1, 1

dfs(1)
```

```python
def dfs(n):
    visited = [False] * (V + 1)
    stack = [0] * V
    top = -1

    top += 1
    stack[top] = n
    visited[n] = True

    while top > -1:
        n = stack[top]
        top -= 1
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and not visited[i]:
                top += 1
                stack[top] = i
                visited[i] = True


V, E = 7, 8 # map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # list(map(int, input().split()))

for i in range(E):
    n1, n2 = edges[i*2], edges[i*2+1]
    adj[n1][n2], adj[n2][n1] = 1, 1

dfs(1)
```



## Postfix calculator

```python
TOKEN = ['(', '+', '-', '*', '/', ')']
ISP = [0, 1, 1, 2, 2]
ICP = [3, 1, 1, 2, 2]
def postfix_converter(tokens):
    stack = []
    result = []
    for token in tokens:
        if token in TOKEN:
            if stack:
                if token == ')':
                    while stack[-1] != '(':
                        result.append(stack.pop())
                    stack.pop()
                elif ISP[TOKEN.index(stack[-1])] < ICP[TOKEN.index(token)]:
                    stack.append(token)
                else:
                    while ISP[TOKEN.index(stack[-1])] >= ICP[TOKEN.index(token)]:
                        result.append(stack.pop())
                    stack.append(token)
            else:
                stack.append(token)
        else:
            result.append(token)
    while stack:
        result.append(stack.pop())
    return result


def postfix_calculator(tokens):
    stack = []
    for token in tokens:
        if token not in TOKEN:
            stack.append(int(token))
        else:
            b = stack.pop()
            f = stack.pop()
            if token == '+':
                stack.append(f+b)
            elif token == '-':
                stack.append(f-b)
            elif token == '*':
                stack.append(f*b)
            elif token == '/':
                stack.append(f/b)
    return stack.pop()


print(postfix_calculator(postfix_converter('(6+5*(2-8)/2)')))
print(eval('6+5*(2-8)/2'))
```



## Backtracking

```python

```

