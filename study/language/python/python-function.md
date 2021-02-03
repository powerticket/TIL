함수(function) I

- 함수(function)?
- 함수의 Output
- 함수의 Input



# 함수(function)
특정한 기능(function)을 하는 코드의 묶음

<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181746-2a1d9400-a665-11e9-804e-e92940d4fc82.png",
alt="func.png">
</center>

## 함수를 쓰는 이유
- 가독성
- 재사용성
- 유지보수




## 함수의 선언과 호출

* 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만든다.


* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.


* 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. (`return` 값이 없으면, `None`을 반환한다.)


* 함수는 호출을 `func()` / `func(val1, val2)`와 같이 한다.

---

#### 활용법

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```



<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png",
alt="function descrpition">
</center>

<center>
    <img src="https://dl.dropbox.com/s/o6v9c0vxpdww1lm/function-argument.png",
alt="function_example">
</center>


<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png",
alt="built_in">
</center>

[출처: python 공식문서](https://docs.python.org/ko/3/library/functions.html)

```python
# 내장함수 목록을 직접 볼 수도 있습니다.
print(__builtins__)
dir(__builtins__)
```



# 함수의 Output

## 함수의 `return`

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류(~~의 객체~~)라도 상관없습니다.

단, **오직 한 개의 객체**만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.



## 함수의 입력(Input)

## 매개변수(parameter) & 인자(argument)

### (1) 매개변수(parameter)

```python
def func(x):
      return x + 2
```

* `x` 는 매개변수(parameter)
* 입력을 받아 함수 내부에서 활용할 `변수`라고 생각하면 된다.
* 함수의 정의 부분에서 볼 수 있다.


### (2) 전달인자(argument)

```python
func(2)
```

* `2` 는 (전달)인자(argument)
* 실제로 전달되는 `입력값`이라고 생각하면 된다.
* 함수를 호출하는 부분에서 볼 수 있다.

> 주로 혼용해서 사용하지만 엄밀하게 따지면 둘은 다르게 구분되어 사용됩니다. 개념적 구분보다 함수가 작동하는 원리를 이해하는게 더 중요합니다.

## 함수의 인자

함수는 입력값(input)으로 `인자(argument)`를 넘겨줄 수 있습니다.

### 위치 인자 (Positional Arguments)

함수는 기본적으로 인자를 위치로 판단합니다.



<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181743-2a1d9400-a665-11e9-8df2-e4856caf16e4.png",
alt="function example 02">
</center>

### 기본 인자 값 (Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

---

**활용법**
```python
def func(p1=v1):
    return p1
```



* 기본 인자 값이 설정되어 있더라도 기존의 함수와 동일하게 호출 가능하다.


<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181744-2a1d9400-a665-11e9-9095-6924ca11122e.png">
</center>

* 호출시 인자가 없으면 기본 인자 값이 활용된다.


<center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181745-2a1d9400-a665-11e9-95ef-e50e463e1583.png",
alt="function example 03">
</center>

**\*주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는
없습니다.**



### 키워드 인자 (Keyword Arguments)

키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.

* **단 아래와 같이 `키워드 인자`를 활용한 다음에 `위치 인자`를 활용할 수는 없습니다.**

```python
greeting(name='홍길동', age=20)
```

## 정해지지 않은 여러 개의 인자 처리

우리가 주로 활용하는 `print()` 함수는 [파이썬 표준 라이브러리의
내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이
구성되어있습니다.
> <center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181751-2b4ec100-a665-11e9-9a7c-a19a8c445cfa.png",
alt="print">
</center>

```python
print('첫번째인자', '두번째인자', '세번째인자', sep='&', end='!')
print(1,2,3,4,5,6,7,8,9)
```

### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트`*args`를 활용합니다.

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.

---

#### 활용법

```python
def func(a, b, *args):
```
> `*args` : 임의의 개수의 위치인자를 받음을 의미
>
> 보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 옵니다.

```python
# 가변 인자 예시
# print문은 *obejcts를 통해 임의의 숫자의 인자를 모두 처리합니다.
```

```python
print(1,2,3,4,5,6,7,8,9)
```

```python
# args는 tuple입니다.
```

```python
def func(*args):
    for i in args:
        if i % 2 == 0:
            print(i)
func(1, 2, 3, 4, 5, 6)
```

### [연습] 가변 인자 리스트를 사용해봅시다.

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 함수 `my_max()`를 작성하세요.

```python
my_max(10, 20, 30, 50)
```
---
```
예시출력)
50
```

```python
max(1, 2, 3, 4)

# 아래에 코드를 작성하세요.
```

```python
def my_max(*args):
    result = args[0]
    for arg in args:
        if arg > result:
            result = arg
    return result
my_max(1, 2, 3, 4)
```

```python
def my_max(*args):
    result = args[-1]
    for i in range(len(args)-1, -1, -1):
        if args[i] > result:
            result = args[i]
    return result
my_max(1, 2, 3, 4)
```

```python
def my_max(*args):
    
my_max(1, 2, 3, 4)
```

```python
import sys
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
def my_max(*args):
    result = sys.maxsize
    for i in args:
        if i > result:
            result = i
    return result
my_max(-1, -2, -3, -4)
```

### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 **`dict`** 형태로 처리가 되며, `**`로 표현합니다.

보통 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

---

#### 활용법

```python
def func(**kwargs):
```
> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미

우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의
내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어
있습니다.
> <center>
    <img src="https://user-
images.githubusercontent.com/18046097/61181740-2984fd80-a665-11e9-94cf-7f5ab41873b1.png",
alt="dictionary">
</center>

```python
# 딕셔너리 생성 함수 예시(키워드 인자)
```

```python
#
hi = dict(한국어='안녕',영어='hi', 독일어='guten tag', 프랑스어='bon jour')
print(hi)
```
