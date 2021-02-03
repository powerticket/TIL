# 제어문(Control Statement)

지금까지 우리는 위에서부터 아래로 순차적으로 명령을 수행하는 프로그램을 작성하였습니다.

특정 상황에 따라 코드를 선택적으로 실행(분기)하거나 동일한 코드를 계속해서 실행해야하려면 어떻게 해야할까요?

이 경우, **코드 실행의 순차적인 흐름을 제어**(Control Flow)할 필요가 있습니다.

이러한 순차적인 코드의 흐름을 제어하는 것을 제어문이라고 하고, 제어문은 크게 **조건문**과 **반복문**으로 나눌 수 있습니다.

제어문을 통해 다음과 순서도(Flow Chart)를 코드로 표현할 수 있습니다.

```python
a = 5
if a > 5:
    print("5 초과")
else:
    print("5 이하")
```

# 조건문(Conditional Statement)

`if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용이 되어야한다.



## `if` 조건문의 구성

### 활용법

- **문법**

```python
if <참/거짓 조건>:
    <코드 블럭>
else:
    <코드 블럭>
```

- **예시**

```python
if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```

* **조건**이 **참**인 경우 `:` 이후의 문장을 수행한다.

* **조건**이 **거짓**인 경우 `else:` 이후의 문장을 수행한다.

* 여러 개의 `elif` 부가 있을 수 있고(없거나), `else`는 선택적이다.

### 주의사항
* 이때 반드시 **들여쓰기**를 유의해야한다.
    - 파이썬에서는 코드 블록을 자바나 C언어의 `{}`와 달리 **들여쓰기**로 판단하기 때문이다.
* 앞으로 우리는 [PEP 8](https://www.python.org/dev/peps/pep-0008/#indentation)에서 권장하는
**4spaces**를 사용할 것이다.



## `elif` 복수 조건

2개 이상의 조건을 활용할 경우 `elif <조건>:`을 활용합니다.



## 중첩 조건문(Nested Conditional Statement)

조건문은 다른 조건문에 중첩될 수도 있다.



## 조건 표현식(Conditional Expression)

* 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다.

* **삼항 연산자(Ternary Operator)**라고 부르기도 한다.

```python
true_value if <조건식> else false_value
```



---

# 반복문(Loop Statement)

- while
- for

## `while` 반복문

`while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.


### `while` 반복문의 구성
- **문법**

```python
while <조건식>:
    <코드 블럭>
```

- 예시

### 주의사항
* `while` 문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요하며, 이후 실행될 코드 블럭은 **4spaces**로 **들여쓰기**를
한다.
* **반드시 종료조건을 설정해야 한다.**



## `for` 문

`for` 문은 시퀀스(String, Tuple, List, Range)나 다른 순회가능한 객체(iterable)의 요소들을 순회한다.

---

### 활용법
- **문법**

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

- **예시**

```python
for menu in ['김밥', '햄버거', '피자', '라면']:
    print(menu)
```

`for` 문에서 요소 값에 다른 값을 할당해도 다음 반복구문에 영향을 주지 않는다.

다음 요소 값에 의해 덮어 씌워지기 때문이다.



### [연습] for 문 작성하기
> `for` 문을 활용하여 사용자가 입력한 문자를 한글자씩 출력해보세요.


### 리스트(list) 순회에서 index의 활용하기

#### `range()`
순회할 list의 길이를 활용하여 index를 조작할 수 있습니다.

```python

```

#### `enumerate()`
인덱스(index)와 값(value)을 함께 활용 가능

> `enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있습니다.
- `enumerate()`는 [내장 함수](https://docs.python.org/ko/3.6/library/functions.html)
중 하나이며, 다음과 같이 구성되어 있습니다.
>
> <center>
    <img src="https://user-
images.githubusercontent.com/18046097/61180561-3993e180-a653-11e9-9558-085c9a0ad65d.png",
alt="enumerate">
</center>

```python
# enumerate()를 활용해서 출력해봅시다.
lunch = ['짜장면', '초밥', '피자', '햄버거']
```

```python
# enumerate()를 사용하였을 때 어떻게 표현이 되는지 확인해봅시다.
```

## 반복제어(`break`, `continue`, `for-else`)

### `break`

반복문을 종료한다.

* `for` 나 `while` 문에서 빠져나간다.



### `continue`

`continue`문은 continue 이후의 코드를 수행하지 않고 *다음 요소부터 계속(continue)하여* 반복을 수행한다.



### `for-else`

끝까지 반복문을 시행한 이후에 실행된다.
- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행된다.
- 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않는다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)



### `pass`
아무것도 하지 않는다.
* 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용할 수 있다.

**`pass` 와 `continue` 차이**

```python
# pass

```

```python
# continue

```
