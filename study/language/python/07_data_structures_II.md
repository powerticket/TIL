# 데이터 구조(Data Structure) II

- 알고리즘에 빈번히 활용되는 순서가 없는(unordered) 데이터 구조
    - 세트(Set)
    - 딕셔너리(Dictionary)

# 세트(Set)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

데이터 구조로서의 세트(set)와 조작법(method)

## 추가 및 삭제

### `.add(elem)`
elem을 세트에 추가합니다.

```python
# add를 사용해봅시다.
a = {'사과', '바나나', '수박'}
```

```python
#
a.add('포도')
a.add('포도')
print(a)
```

### `.update(*others)`

여러가지의 값을 추가합니다.

인자로는 반드시 iterable 데이터 구조를 전달해야합니다.

```python
# update를 사용해봅시다.
a = {'사과', '바나나', '수박'}
```

```python
#
a.update({'토마토', '토마토', '딸기'}, {'포도', '레몬'})
print(a)
```

### `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생합니다.

```python
# remove를 사용해봅시다.
a = {'사과', '바나나', '수박'}
```

```python
#
a.remove('애플')
a.remove('사과')
print(a)
```

### `.discard(elem)`
elem을 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

```python
# discard를 사용해봅시다.
a = {'사과', '바나나', '수박'}
```

```python
#
a.discard('포도')
a.discard('수박')
print(a)
```

### `.pop()`

**임의의 원소**를 제거해 반환합니다.

```python
# pop을 사용해봅시다.
a = {'사과', '바나나', '수박', '아보카도'}
```

```python
#
print(a.pop())
print(a)
```

# 딕셔너리(Dictionary)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
>
> `Key: Value` 페어(pair)의 자료구조

데이터 구조로서의 딕셔너리(dictionary)와 조작법(method)

## 조회

### `.get(key[, default])`

key를 통해 value를 가져옵니다.

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다.

```python
# get을 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict['pineapple']
```

```python
#
print(my_dict.get('pineapple'))
print(my_dict.get('apple'))
print(my_dict.get('pineapple', 0))
```

## 추가 및 삭제

### `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

```python
# pop을 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나'}
```

```python
#
my_dict.pop('apple')
print(my_dict)
```

```python
# 딕셔너리에 없으면 에러가 발생합니다.
```

```python
#
my_dict.pop('melon')
```

```python
# 두번째 인자로 default를 설정할 수 있습니다.
```

```python
#
my_dict.pop('melon', 0)
```

### `.update()`

값을 제공하는 key, value로 덮어씁니다.

```python
# update를 사용해봅시다.
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
```

```python
#
my_dict.update(apple='애플')
print(my_dict)
```

## 딕셔너리 순회(반복문 활용)

딕셔너리에 `for` 문을 실행하면 기본적으로 다음과 같이 동작합니다.

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)
```

딕셔너리의 **key**를 접근할 수 있으면 **value**에도 접근할 수 있기 때문입니다.

따라서 딕셔너리의 value를 출력하기 위해서는 아래와 같이 작성합니다.

```python
# 학생 이름(key)을 활용하여 점수(value)를 출력해봅시다.
```

```python
#
for student in grades:
    print(grades[student])
```

* dictionary에서 `for`를 활용하는 4가지 방법

```python
# 0. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])


# 2. `.values()` 활용
for val in dict.values():
    print(val)


# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)

```

### [연습] 딕셔너리 순회

> 혈액형 검사한 결과가 담긴 `blood_types`이 주어졌을때, 해당 딕셔너리를 순회하며, `key`와 `value`를 출력해보세요.

---

**[출력 예시]**
```
A형은 40명입니다.
B형은 11명입니다.
AB형은 4명입니다.
O형은 45명입니다.
```

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
```

```python
# 아래에 코드를 작성하세요.
```

```python
# key로 반복하는 코드를 작성해봅시다.
```

```python
#

```

```python
# .keys()를 활용하여 반복하는 코드를 작성해봅시다.
```

```python
#

```

```python
# .items()를 활용하여 반복하는 코드를 작성해봅시다.
```

```python
#

```

### [실습] 딕셔너리 순회

> 혈액형 검사한 결과가 담긴 `blood_types`이 주어졌을때, 해당 검사에 참가한 사람들의 총합을 구해보세요.

---

**[출력 예시]**
```
검사에 참가한 사람은 총 100명입니다.
```

```python
# key로 반복하는 코드를 작성해봅시다.
```

```python
total = 0

```

```python
# .values()를 활용하여 작성해봅시다.
```

```python
total = 0

```

```python
# 더 간단하게 구할 수도 있습니다.
```

```python

```

### [응용] 딕셔너리 구축하기(counter)
> 리스트가 주어질 때, 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드세요.

---

**[출력 예시]**

{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock':
1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

# 아래에 코드를 작성하세요.
```

```python
#

```

> `get(key[, default])`
* key 가 딕셔너리에 있는 경우 key 에 대응하는 값을 돌려주고, 그렇지 않으면 default 를 돌려준다.

## Dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

---

### 활용법
`iterable`에서 `dict`를 생성할 수 있습니다.

```python
{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})
```

```python
# iterable(range) -> dict
```

```python
#
cubic = {}
print(cubic)
```

```python
# iterable(dict) -> dict
```

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
negative_blood_types = {}
print(negative_blood_types)
```

## Dictionary comprehension + 조건

List comprehension과 유사하게, 조건문에 참인 식으로 딕셔너리를 생성합니다.


### 활용법

```py
{키: 값 for 요소 in iterable if 조건식}

{키: 값 if 조건식 else 값 for 요소 in iterable}

# elif 는 다음과 같이 사용해야 합니다. (if else 열거)
{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable}
```

### Dictionary comprehension 사용해보기

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
```

```python
# 미세먼지 농도가 80 초과 지역만 뽑아주세요.
# 예) {'대전': 82, '중국': 200}
```

```python
#
result = {}
```

```python
print(result)
```

```python
# 미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꾸세요.
```

```python
#
result = {}
```

```python
print(result)
```

```python
# elif 도 사용할 수 있습니다. (if else 열거)
```

```python
#
result = {}
```

```python
print(result)
```
