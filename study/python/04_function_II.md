# 함수(function) II
- 함수와 스코프
- 재귀 함수

# 함수와 스코프(scope)

함수는 코드 내부에 공간(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인
`전역 스코프(global scope)`와 구분됩니다.

* **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
* **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간


* **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
* **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

```python
# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    a = 30
    print(a)
    print(b)


# 변수 c는 접근 불가합니다.
func(5)
print(a)
```

```python
# 50을 인자로 전달하여 출력할 수 있습니다.
func(50)
```

> `func()` 함수에 a 변수를 추가하면 어떻게 될까요?

## 이름 검색(resolution) 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

이것을, `LEGB Rule` 이라고 부르며, 아래와 같은 순서로 이름을 찾아나갑니다.

* `L`ocal scope: 정의된 함수


* `E`nclosed scope: 상위 함수


* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈


* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
# 이것을 통해 첫시간에 내장함수의 식별자를 사용할 수 없었던 예제에서 오류가 생기는 이유를 확인할 수 있습니다.
```

```python
#
print = 'ssafy'
print(3)
```

```python
#
del print
```

1. `print()` 코드가 실행되면


2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,


3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고,


4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.


5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.

```python
a = 10  # 전역 변수
b = 20  # 전역 변수

def enclosed():
    a = 30  # enclosed함수의 지역 변수
    
    def local():
        c = 40 # local함수의 지역 변수
        print(a, b, c)
    
    local()
    
    a = 50  # enclosed함수의 지역 변수이며, local함수에서는 Enclosed Scope
```

```python
enclosed()
```

```python
# 전역에서 local() 함수의 호출이 가능할까요?
```

```python
local()
```

```python
# 전역 변수를 바꿀 수 있을까요?
```

```python
#
global_num = 3
def local_scope():
    global_num = 5
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
```

```python
# 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다.
```

```python
#
global_num = 3
def local_scope():
    global global_num
    global_num = 5    
    return f'global_num이 {global_num}으로 설정되었습니다.'

print(local_scope())
print('global_num:', global_num)
```

### 변수의 수명주기(lifecycle)

변수의 이름은 각자의 `수명주기(lifecycle)`가 있습니다.

* **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지


* **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지


* **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 가 종료될 때까지 유지 (함수 내에서 처리되지
않는 예외를 일으킬 때 삭제됨)

# 재귀 함수(recursive function)

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻합니다.

알고리즘을 설계 및 구현에서 유용하게 활용됩니다.

## 팩토리얼 계산
> 팩토리얼은 1부터 n 까지 양의 정수를 차례대로 곱한 값이며 `!` 기호로 표기합니다. 예를 들어 3!은 3 * 2 * 1이며 결과는 6
입니다.
>
> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성하세요.
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

---
```
예시 출력)
120
```

### 반복문을 이용한 팩토리얼 계산

```python
# 아래에 코드를 작성해주세요.
```

```python
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

fact(5)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
def fact(n):
    n = int(n)
    if n == 1:
        return 1
    return n * fact(n-1)

fact(5)
```

### 재귀를 이용한 팩토리얼 계산

재귀를 이용하여 팩토리얼을 계산하여 return하는 `factorial()` 함수를 작성하세요.

```
1! = 1
2! = 1 * 2 = 1! * 2
3! = 1 * 2 * 3 = 2! * 3
```

```python
# 아래에 코드를 작성해주세요.
```

```python

# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
def factorial(n):
    n = int(n)
    if n == 1:
        return 1
    return n * fact(n-1)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
factorial(5)
```

## 반복문과 재귀함수
```python
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

* 두 코드 모두 원리는 같다!


1. 반복문 코드
    - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소한다.
    - 마지막에 n이 1이면 더 이상 반복문을 돌지 않는다.


2. 재귀 함수 코드
    - 재귀 함수를 호출하며, n은 1씩 감소한다.
    - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않는다.

* 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 된다.

* 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 한다.

* `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳이다.

* 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1일때, 함수가 아닌 정수 반환하는 것**이다.

* 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
* 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
* 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에
쌓이는 것을 볼 수 있다.
* 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
* 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다. (최대 재귀 깊이)

### 최대 재귀 깊이

```python
def ssafy():
    print('Hello, ssafy!')
    ssafy()

ssafy()
```
---

`ssafy()`를 호출하면 아래와 같이 문자열이 계속 출력되다가 RecursionError가 발생합니다.

파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있기 때문입니다.

---

```bash
Hello, world!
Hello, world!
...
Hello, world!
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)

...

<ipython-input-11-2bbb40950c86> in hello()
      1 def hello():
      2     print('Hello, world!')
----> 3     hello()
      4
      5 hello()

RecursionError: maximum recursion depth exceeded while calling a Python object
```

```python
# 직접 오류를 확인하세요.
```

```python
def ssafy():
    print('Hello, ssafy!', end=" ")
    ssafy()

ssafy()
```

## 피보나치 수열

첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열입니다.

(0), 1, 1, 2, 3, 5, 8

> 피보나치 수열은 다음과 같은 점화식이 있습니다.
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해주세요.
>

$$
\displaystyle F_0 = F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

---
```
예시 입력)
fib(10)

예시 호출)
55
```

```python
# 재귀를 이용한 코드 fib() 를 작성하세요.
```

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
fib(10)
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
fib(10)
```

```python
# 반복문을 이용한 코드 fib_loop() 를 작성하세요.
```

```python

```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
fib_loop(10)
```

## 반복문과 재귀 함수의 차이

* 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용한다.
* 재귀 호출은 `변수 사용` 을 줄여줄 수 있다.

```python
# 큰 숫자를 재귀로 짜여진 fib() 함수의 인자로 넘겨보세요.
```

```python

```

```python
# 100배 되는 숫자를 반복문으로 짜여진 fib_loop() 인자로 넘겨보세요.
```

```python

```

## 다른 재귀 함수 사용

```python
def sum_recur(n):
    if n == 0:
        return 0
    return n + sum_recur(n-1)

sum_recur(10)
```
