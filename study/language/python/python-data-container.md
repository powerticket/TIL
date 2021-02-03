# 컨테이너(Container)
여러 개의 값을 저장할 수 있는 것(~~객체~~)

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터

## 시퀀스(sequence)형 컨테이너

`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다.

* **주의! 순서대로 나열된 것이 `정렬되었다(sorted)`라는 뜻은 아니다.**

### 특징
1. 순서를 가질 수 있다.

2. **특정 위치의 데이터를 가리킬 수 있다.**

### 종류
파이썬에서 기본적인 시퀀스 타입은 다음과 같습니다.

* 리스트(list)

* 튜플(tuple)

* 레인지(range)

* *문자형(string)*

* *바이너리(binary)* : 따로 다루지는 않습니다.


## 리스트(`list`)

<center><img src="https://user-
images.githubusercontent.com/18046097/61180421-fe90ae80-a650-11e9-8211-d06f87756d05.png",
alt="list figure"/></center>

**활용법**
```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.

```python
# 빈 리스트를 만들어봅시다.
```

```python
l = []
ll = list()
print(type(l))
print(type(ll))
```

```python
# 원소를 포함한 리스트를 만들어봅시다.
```

```python
numbers = [1, 3, 5, 7, 9]
print(type(numbers))
print(numbers)
```

```python
# 첫번째 값에 접근해봅시다.
```

```python
numbers[2:4]
```

## 튜플(`tuple`)

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없습니다.

직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.

## 레인지(`range()`)

`range` 는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)`


> 0부터 n-1까지 값을 가짐


범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다




## 시퀀스에서 활용할 수 있는 연산자/함수

|operation|설명|
|---------|---|
|x `in` s	|containment test|
|x `not in` s|containment test|
|s1 `+` s2|concatenation|
|s `*` n|n번만큼 반복하여 더하기
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|



# 비 시퀀스형(Non-sequence) 컨테이너

- 셋(set)

- 딕셔너리(dictionary)

## `set`

`set`은 순서가 없는 자료구조입니다.

* `set`은 수학에서의 집합과 동일하게 처리된다.

* `set`은 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.

* 빈 집합을 만들려면 `set()`을 사용해야 합니다. (`{}`로 사용 불가능.)

* `set`을 활용하면 `list`의 중복된 값을 손쉽게 제거할 수 있습니다.



## `dictionary`

`dictionary`는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다.


<center><img src="https://user-
images.githubusercontent.com/18046097/61180427-1405d880-a651-11e9-94e1-1cc5c2a2ff34.png"></center>

### 활용법

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

* `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
* `key`는 **변경 불가능(immutable)한 데이터**만 가능하다. (immutable : string, integer, float,
boolean, tuple, range)
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.



## 컨테이너형 형변환

파이썬에서 컨테이너는 서로 변환할 수 있습니다.

except other container to range and dictionary value

## 데이터의 분류 (*중요*!)
> `mutable` vs. `immutable`

### 변경 불가능한(`immutable`) 데이터

단일 데이터들

- **숫자(Number)**
- **글자(String)**
- **참/거짓(Bool)**

```python
range(), tuple(), frozenset()
```



### 변경 가능한(`mutable`) 데이터

컨테이너 (~~`tuple`, `range()`, `frozenset`~~)

- `list`
- `dict`
- `set`
- 사용자가 만든 데이터 타입



## 컨테이너(Container)
<center><img src="https://user-
images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png",
alt="container"/></center>
