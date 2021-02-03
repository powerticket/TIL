# 데이터 구조(Data Structure) I

데이터 구조(Data Structure)란 데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법을 말한다.

> **Program = Data Structure + Algorithm**
> - Niklaus Wirth

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조
    - 문자열(String)
    - 리스트(List)
- 데이터 구조에 적용 가능한 Built-in Function
    - `map()`
    - `filter()`

# 문자열(String)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

문자열의 다양한 조작법(method)

## 조회/탐색

### `.find(x)`

x의 **첫 번째 위치**를 반환합니다. 없으면, `-1`을 반환합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
#
'apple'.find('p')
```

```python
#
'apple'.find('f')
```

### `.index(x)`

x의 **첫번째 위치**를 반환합니다. 없으면, 오류가 발생합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
#
'apple'.index('p')
```

```python
#
try:
    'apple'.index('k')
except:
#     print(error)
    print('해당하는 값이 없습니다.')
```

## 값 변경

### `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
#
'yay!'.replace('a', '_')
```

```python
#
'wooooowoo'.replace('o', '', 2)
```

### `.strip([chars])`

특정한 문자들을 지정하면,  양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip).

지정하지 않으면 공백을 제거합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
#
'    oh!\n'.strip()
```

```python
#
'    oh!\n   '.lstrip()
```

```python
#
'hehehihihihihi'.rstrip('hi')
```

### `.split()`

문자열을 특정한 단위로 나누어 리스트로 반환합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
#
'a_b_c'.split('_')
```

```python
#
inputs = input().split()
print(inputs)
```

### `'separator'.join(iterable)`

특정한 문자열로 만들어 반환합니다.

반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) 문자열로 반환합니다.

```python
word = '배고파'
words = ['안녕', 'hello']

# 아래에 코드를 작성하세요.
```

```python
#
'!'.join(word)
```

```python
#
' '.join(words)
```

## 문자 변형

### `.capitalize()`, `.title()`, `.upper()`

* `.capitalize()` : 앞글자를 대문자로 만들어 반환한다.

* `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환한다.

* `.upper()` : 모두 대문자로 만들어 반환한다.

```python
a = 'hI! Everyone, I\'m kim'

# 아래에 코드를 작성하세요.
```

```python
#
a.capitalize()
a.title()
a.upper()

print(a) # 변형을 시켜 반환만 하기때문 a를 출력해보면 그대로
```

### `.lower()`, `.swapcase()`

* `lower()` : 모두 소문자로 만들어 반환한다.

* `swapcase()` : 대 <-> 소문자로 변경하여 반환한다.

```python
a = 'hI! Everyone, I\'m kim'

# 아래에 코드를 작성하세요.
```

```python
#
a.lower()
a.swapcase()
```

### 기타 문자열 관련 검증 메소드 : 참/거짓 반환
```py
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(),
.istitle(), .islower()
```

```python
# 다음 명령어로 문자열 메소드를 확인할 수 있습니다.
# =====
dir('string')
```

---

# 리스트(List)

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

데이터 구조로서의 리스트(list)와 조작법(method)

## 값 추가 및 삭제

### `.append(x)`

리스트에 값을 추가할 수 있습니다.

```python
# 카페 리스트를 만들어봅시다.
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
```

```python
# 값을 추가해봅시다.
```

```python
#
cafe.append('banapresso')
print(cafe)
```

### `.extend(iterable)`

리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있습니다.
```python
[1, 2, 3] + [4, 5, 6]
> [1, 2, 3, 4, 5, 6]
```

```python
# 앞서 만든 리스트에 추가해봅시다.
```

```python
#
cafe.extend(['wcafe', '빽다방'])
print(cafe)
```

```python
# 앞서 배운 list concatenate와 동일합니다.
```

```python
#
cafe += ['mc_cafe', 'droptop']
print(cafe)
```

```python
# append와 비교해봅시다.
```

```python
#
cafe.append(['coffeenie'])
print(cafe)
print('-----')

cafe.extend(['twosome_place'])
print(cafe)
```

```python
# 문자열도 활용해봅시다.
```

```python
print(cafe)
cafe.extend('ediya')
print(cafe)
```

### `.insert(i, x)`

정해진 위치 `i`에 값을 추가합니다.

```python
# 앞서 만든 리스트의 가장 앞에 'hi'를 넣어봅시다.
```

```python
#
cafe.insert(0, 'start')
print(cafe)
```

```python
# 앞서 만든 리스트의 가장 뒤에 'bye'를 넣어봅시다
```

```python
#
cafe.insert(len(cafe), 'end')
print(cafe)
```

```python
# 리스트의 길이를 넘어서는 인덱스는 마지막에 아이템이 추가됩니다.
```

```python
#
cafe.insert(len(cafe)+100, '!')
print(cafe)
```

### `.remove(x)`

리스트에서 값이 x인 것을 삭제합니다.

```python
# remove를 사용해봅시다.
numbers = [1, 2, 3, 1, 2]
```

```python
# 중복된 값 1을 삭제 해봅시다.
```

```python
#
numbers.remove(1)
print(numbers)
```

```python
# 한번 더 삭제해봅시다.
```

```python
#
numbers.remove(1)
print(numbers)
```

```python
# remove는 값이 없으면 오류가 발생합니다. 확인해봅시다.
```

```python
#
numbers.remove(1)
```

### `.pop(i)`

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

```python
# pop을 사용해봅시다.
a = [1, 2, 3, 4, 5, 6]
```

```python
# 가장 앞에 있는 것을 삭제해봅시다. return도 확인해보세요.
```

```python
#
print(a.pop(0))
print(a)
```

```python
# 값이 return이 된다는 것은 별도의 변수에 저장할 수 있다는 것입니다. 
```

```python
#
print(a)
deleted_value = a.pop()
print(f'{deleted_value}가 삭제되어 {a}가 되었습니다.')
```

### `.clear()`

리스트의 모든 항목을 삭제합니다.

```python
# clear를 사용해봅시다.
```

```python
#
numbers = list(range(1, 46))
print(numbers)
numbers.clear()
print(numbers)
```

## 탐색 및 정렬

### `.index(x)`

x 값을 찾아 해당 index 값을 반환합니다.

```python
# index를 사용해봅시다.
a = [1, 2, 3, 4, 5]
```

```python
#
a.index(3)
```

```python
# index는 없을 시 오류가 발생합니다. 확인해봅시다. 
# 앞서 remove 역시도 같은 에러가 발생하였습니다. (ValueError)
# =====
a.index(100)
```

### `.count(x)`

원하는 값의 개수를 확인할 수 있습니다.

```python
# count를 사용해봅시다.
a = [1, 2, 5, 1, 5, 1]
```

```python
#
a.count(1)
```

```python
# 따라서 원하는 값을 모두 삭제하려면 다음과 같이 할 수 있습니다.
```

```python
#
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
```

```python
# 모두 삭제되었는지 검증해봅시다.
```

```python
#
print(a)
```

```python
#
target_value in a
```

### `.sort()`

정렬을 합니다.

내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, **`None`**을 리턴합니다.

```python
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)
```

```python
# sort() 를 사용해봅시다.
# =====
lotto.sort()
print(lotto.sort())
print(lotto)

lotto.sort(reverse=True)
print(lotto)
```

### `.reverse()`

반대로 뒤집습니다. **(정렬 아님)**

```python
classroom = ['Tom', 'David', 'Justin']
print(classroom)
```

```python
#
classroom.reverse()
print(classroom)
```

## 리스트 복사

```python
a = 3
b = a
print(b)
b += 2
print(b)
print(a)
```

```python
# 리스트 복사를 해봅시다.
original_list = [1, 2, 3]
```

```python
#
copy_list = original_list
print(copy_list)
```

```python
# copy_list의 값을 바꾸고 original_list를 출력해봅시다.
```

```python
#
copy_list[0] = 5
print(original_list)
```

```python
# id 값을 확안해봅시다.
```

```python
#
id(copy_list) == id(original_list)
copy_list is original_list
```

## 데이터의 분류 (*복습*)
> `mutable` vs. `immutable`

데이터는 크게 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)으로 나뉘며, python은 각각을 다르게
다룹니다.

### 변경 불가능한(`immutable`) 데이터

단일 데이터들

- **숫자(Number)**
- **글자(String)**
- **참/거짓(Bool)**

그리고

```python
range(), tuple(), frozenset()
```

```python
# immutable 데이터의 복사는 어떻게 이루어질까?
a = 20
b = a
b = 10

print(a)
print(b)
```

```python
%%html
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%2020%0Ab%20%3D%20a%0Ab%20%3D%2010%0A%0Aprint%28a%29%0Aprint%28b%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

### 변경 가능한(`mutable`) 데이터

Container(복합 데이터)들 (~~`tuple`, `range()`, `frozenset`~~)

- `list`
- `dict`
- `set`
- ~~사용자가 만든 데이터 타입~~

```python
# mutable 데이터의 복사는 어떻게 이루어질까?
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)
print(b)
```

```python
%%html
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%20%5B1,%202,%203,%204%5D%0Ab%20%3D%20a%0Ab%5B0%5D%20%3D%20100%0A%0Aprint%28a%29%0Aprint%28b%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```

## 리스트를 복사 방법

### (1) slice 연산자 사용 `[:]`

```python
# 리스트를 복사해봅시다.
```

```python
#
a = [1, 2, 3]
b = a[:]

b[0] = 5
print(a)
```

```python
# 다른 방법으로 복사해봅시다.
```

### (2) `list()` 활용

```python
#
a = [1, 2, 3]
b = list(a)

b[0] = 5
print(a)
```

* 하지만, 이렇게 하는 것도 일부 상황에만 서로 `다른 얕은 복사(shallow copy)`이다.

```python
# 2차원 배열을 복사해봅시다.
```

```python
#
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 3
print(a)
```

* 만일 중첩된 상황에서 복사를 하고 싶다면, `깊은 복사(deep copy)`를 해야한다.

* 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경된다.

```python
# 깊은 복사를 사용해봅시다.
```

```python
#
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a)
```

## List Comprehension

List Comprehension은 표현식과 제어문을 통해 리스트를 생성합니다.

여러 줄의 코드를 한 줄로 줄일 수 있습니다.

---

### 활용법

```python
[식 for 변수 in iterable]

list(식 for 변수 in iterable)
```

### 세제곱 리스트

> 다음의 리스트를 작성하세요.
- 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`

```python
numbers = range(1, 11)
```

```python
# 반복문을 활용하여 작성하세요.
```

```python
#
cubic_list = []
for number in numbers:
    cubic_list.append(number ** 3)
```

```python
print(cubic_list)
```

```python
# List comprehension을 활용하여 작성하세요.
```

```python
#
cubic_list = [number ** 3 for number in numbers]
```

```python
print(cubic_list)
```

## List Comprehension + 조건문

조건문에 참인 식으로 리스트를 생성합니다.

---

### 활용법

```python
[식 for 변수 in iterable if 조건식]

[식 if 조건식 else 식 for 변수 in iterable]

# elif 는 다음과 같이 사용해야 합니다. (if else 열거)
[식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]
```

### [연습] 짝수리스트
> 다음의 리스트를 작성하세요.

- 1~10까지의 숫자중 짝수만 담긴 리스트 `even_list`
- 여러개의 `for` 혹은 `if`문을 중첩적으로 사용 가능합니다.

```python
# 반복문을 활용하여 작성하세요.
```

```python
#
even_list = []
for number in range(1, 11):
    if number % 2 == 0:
        even_list.append(number)
```

```python
print(even_list)
```

```python
# List comprehension을 활용하여 작성하세요.
```

```python
#
even_list = [number for number in range(1, 11) if number % 2 == 0]
```

```python
print(even_list)
```

### [실습] 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 작성하세요.
1. 반복문 활용
2. list comprehension 활용

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
```

---

```
예시 출력)
[('justin', 'jane'), ('justin', 'ashley'), ('justin', 'mary'), ('eric', 'jane'),
('eric', 'ashley'), ('eric', 'mary'), ('david', 'jane'), ('david', 'ashley'),
('david', 'mary')]
```


```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
```

```python
# 반복문을 활용하여 작성하세요.
```

```python
#
pair = []
```

```python
print(pair)
```

```python
# List comprehension을 활용하여 작성하세요.
```

```python
#
pair = []
```

```python
print(pair)
```

### [응용] 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾으세요.
1. 반복문 활용
2. list comprehension 활용

---

```
예시 출력)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9,
40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39),
(16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36,
45)]
```

```python
# 반복문을 활용하여 작성하세요.
```

```python
#
result = []
```

```python
print(result)
```

```python
# List comprehension을 활용하여 작성하세요.
```

```python
#
result = []
```

```python
print(result)
```

### [응용] 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하세요.

```python
words = 'Life is too short, you need python!'
```

---

```
예시 출력)
Lf s t shrt, y nd pythn!
```

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'
```

```python
# 반복문을 활용하여 작성하세요.
```

```python
#
result = []
```

```python
print(''.join(result))
```

```python
# List comprehension을 활용하여 작성하세요.
```

```python
#
result = []
```

```python
print(''.join(result))
```

# 데이터 구조에 적용가능한 Built-in Function

순회가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

- `map()`
- `filter()`
- `zip()`
- ~~`reduce()`~~
([참고](https://docs.python.org/ko/3/library/functools.html#functools.reduce))

### `map(function, iterable)`

* 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다.


* return은 `map_object` 형태이다.

```python
numbers = [1, 2, 3]

# 위의 코드를 문자열 '123'으로 만드세요
new_numbers = []
for number in numbers:
    new_numbers.append(str(number))
print(new_numbers)
```

```python
# List comprehension 활용
```

```python
#
new_numbers = list(map(str, numbers))
```

```python
print(new_numbers)
```

```python
# map() 활용
```

```python
#
```

```python
print(new_numbers)
```

`map()` 함수는 입력값을 처리할 때 자주 활용됩니다.

```python
numbers = ['1', '2', '3']

# 위의 코드를 숫자 '123'으로 만드세요
```

```python
# List comprehension 활용
```

```python
#

```

```python
print(new_numbers)
```

```python
# map() 활용
```

```python
#

```

```python
print(new_numbers)
```

첫번째 인자 function은 사용자 정의 함수도 가능합니다.

```python
# 세제곱의 결과를 나타내는 함수가 있습니다.
def cube(n):
    return n ** 3
```

```python
# 세제곱 함수를 각각의 요소에 적용한 결과값을 구해봅시다.
numbers = [1, 2, 3]
```

```python
#
```

```python
print(new_numbers)
```

### `filter(function, iterable)`

* iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환한다.


* `filter object` 를 반환한다.

```python
# 특정 list에서 홀수만을 걸러내는 코드를 작성해봅시다.
```

```python
# 홀수를 판별하는 함수가 있습니다.
def odd(n):
    return n % 2
```

```python
# 홀수인 요소만 뽑아 new_numbers에 저장합니다.
numbers = [1, 2, 3]
```

```python
#
```

```python
print(new_numbers)
```

```python
# 다음의 list comprehension과 동일합니다.
```

```python
#
```

### `zip(*iterables)`

* 복수의 iterable 객체를 모아(`zip()`)준다.


* 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
```

```python
# zip() 활용하여 짝을 맞추어 본다.
```

```python
#
```

```python
print(pair)
```
