# 에러 & 예외 처리
- 에러(Error)
- 예외 처리(Exception Handling)

# 에러(Error)
발생할 수 있는 에러의 종류를 확인해봅시다.

## 문법 에러(Syntax Error)

> 문법 에러가 있는 프로그램은 실행되지 않습니다.

* 에러 발생 시 `SyntaxError`라는 키워드와 함께, 에러의 상세 내용을 보여줍니다.


* `파일이름`과 `줄번호`, `^` 문자를 통해 파이썬이 코드를 읽어 들일 때(`parser`) 문제가 발생한 위치를 표현합니다.


* `parser` 는 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 작은 '화살표(`^`)'를 표시합니다.

```python
# 조건문을 통해 발생시켜봅시다.
```

```python
#
if True:
    print('참')
else
    print('거짓')
```

```python
# print문을 통해 다른 오류를 발생시켜봅시다.
# EOL 오류(따옴표 오류)를 확인해봅시다.
```

```python
#
print('hi)
```

```python
# EOF 에러(괄호 닫기 오류)도 보게됩니다.
```

```python
#
print('hi')
```

```python
# 정확한 위치를 지정하지 않을 수도 있으므로 지정된 위치 전후를 모두 확인해야합니다.
```

```python
#
if True print('참')
```

## 예외(Exception)

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춥니다.

* 문법적으로는 옳지만, 실행시 발생하는 에러입니다.


* *아래 제시된 모든 에러는 `Exception`을 상속받아 이뤄진다.*

```python
# ZeroDivisionError를 확인해봅시다.
```

```python
# 0으로 나눌수는 없습니다.
# =====
10 * (1/0)
```

```python
# NameError를 확인해봅시다. 
```

```python
# 지역 혹은 전역 이름 공간내에서 유효하지 않는 이름
# 즉 정의되지 않은 변수를 호출 하였을 경우
# =====
print(abc)
```

```python
# TypeError를 확인해봅시다.
```

```python
# 자료형에 대한 타입 자체가 잘못 되었을 경우
# =====
1 + '1'
```

```python
# 함수 호출과정에서 TypeError도 발생하게 됩니다. 확인해봅시다.
```

```python
#
round('3.5')
```

```python
# 함수호출 과정에서 다양한 오류를 확인할 수 있습니다. (1) 필수 argument 누락
```

```python
#
import random
random.sample([1, 2, 3])
```

```python
# 함수호출 과정에서 다양한 오류를 확인할 수 있습니다. (2) argument 개수 초과
```

```python
#
random.choice([1, 2, 3], 6)
```

```python
# ValueError를 확인해봅시다.
```

```python
# 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
# =====
int('3.5')
```

```python
# ValueError를 확인해봅시다.
```

```python
# 존재하지 않는 값을 찾고자 할 경우
numbers = [1, 2]
numbers.index(3)
```

```python
# IndexError를 확인해봅시다.
```

```python
# 존재하지 않는 index로 조회할 경우
empty_list = []
empty_list[-1]
```

```python
# KeyError를 확인해봅시다. 
```

```python
# 딕셔너리에서 Key가 없는 경우 
# =====
songs = {'sia': 'candy cane lane'}
songs['queen']
```

```python
# ModuleNotFoundError를 확인해봅시다.
```

```python
# 모듈을 찾을 수 없는 경우 
# =====
import reque
```

```python
# ImportError를 확인해봅시다.
```

```python
# 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
# =====
from random import sampl
```

```python
# KeyboardInterrupt를 확인해봅시다.
```

```python
# 주피터 노트북에서는 정지 버튼이지만, 실제로 우리가 돌릴 때는 ctrl+c를 통해 종료하였을 때 발생한다.
# =====
while True:
    continue
```

# 예외 처리(Exception Handling)

###  `try` & `except`
`try` 문을 이용하여 예외 처리를 할 수 있습니다.

---

#### 활용법

```python
try:
    <코드 블럭 1>
except (예외):
    <코드 블럭 2>
```

* `try` 아래의 코드블락(code block)이 실행된다.

* 예외가 발생되지 않으면, **`except`없이 실행이 종료 된다.**

* 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.

```python
# 사용자로부터 값을 받아 정수로 변환하여 출력해봅시다.
```

```python
#
num = input('값을 입력하시오 : ')
print(int(num))
```

```python
# 사용자가 문자열을 넣어 해당 오류(ValueError)가 발생하면, 숫자를 입력하라고 출력해봅시다.
```

```python
#
num = input('값을 입력하시오 : ')
print(int(num))
```

### 에러 메시지 처리  `as`

`as` 키워드를 활용하여 에러 메시지를 보여줄 수도 있습니다.

---

#### 활용법

```python
try:
    <코드 블럭 1>
except 예외 as err:
    <코드 블럭 2>
```

```python
# 에러 메세지를 넘겨줄 수도 있습니다.
```

```python
#
empty_list = []
print(empty_list[-1])
```

## 복수의 예외 처리

하나 이상의 예외를 모두 처리할 수 있습니다.

괄호가 있는 튜플로 여러 개의 예외를 지정할 수 있습니다.

---

#### 활용법

```python
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>


try:
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```

```python
# 100을 사용자가 입력한 값으로 나눈 후 출력하는 코드를 작성해봅시다.
```

```python
#
num = input('100으로 나눌 값을 입력하시오: ')
print(100/int(num))
```

```python
# 문자열일때와 0일때 모두 처리를 해봅시다.
```

```python
#
num = input('100으로 나눌 값을 입력하시오: ')
100/int(num)
```

```python
# 각각 다른 오류를 출력할 수 있습니다.
```

```python
#
num = input('100으로 나눌 값을 입력하시오: ')
100/int(num)
```

- 여기서 중요한 내용은 **에러가 순차적으로 수행됨**으로, 가장 작은 범주부터 시작해야 합니다.

```python
#
num = input('100으로 나눌 값을 입력하시오: ')
100/int(num)
```

### `else`

* 에러가 발생하지 않는 경우 실행 시킬 문장은 `else`를 활용한다.
* `else`는 `except` 코드 뒤에 와야 한다.
* `try` 코드 블럭이 예외를 일으키지 않았을 때, 실행되어야 하는 코드에 사용된다.

---

#### 활용법

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```

```python
# else를 사용해봅시다.
```

```python
#
try:
    numbers = [1, 2, 3]
    number = numbers[2]
except IndexError:
    print('오류 발생')
```

### `finally`

* 어떤 경우에든 반드시 실행해야하는 코드에는 `finally`를 활용한다.
* 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
* 예외의 발생 여부과 관계없이 항상 실행된다.

---

#### 활용법

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```

```python
# finally를 사용해봅시다.
```

```python
#
try:
    languages = {'python': 'good'}
    languages['java']
except KeyError as err:
    print(f'{err}는 딕셔너리에 없는 키입니다.')
```

## 예외 발생 시키기(Exception Raising)


### `raise`
`raise`를 통해 예외를 강제로 발생시킬 수 있습니다.

---

#### 활용법

```python
raise <에러>('메시지')
```

```python
# raise를 사용해봅시다.
```

```python
#

```

```python
#

```

### [연습] `raise`를 활용하여 예외 발생시키기

>양의 정수 두개를 받아 몫을 출력하는 함수 `def my_div(num1, num2)`를 작성하세요.

---

- num2 가 0 이여서 발생하는 오류인 경우 **에러메시지**를 출력합니다.
    - *예) division by zero 오류가 발생하였습니다.*


- 인자가 string 이여서 발생하는 경우는 **ValueError와 함께 '숫자를 넣어주세요'를 출력**합니다.
    - (실제로 이 경우에 발생하는 것은 `TypeError`입니다.)


- 정상적인 경우에는 결과를 return합니다.

```python
# 아래에 코드를 작성하세요.
```

```python
def my_div(num1, num2):
    pass
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
```

```python
my_div(1, 0)
```

```python
my_div('1', '5')
```

### `assert`

`assert` 문은 예외를 발생시키는 다른 방법입니다.

보통 **상태를 검증하는데 사용**되며 무조건 `AssertionError`가 발생합니다.

---

**활용법**

```python
assert Boolean expression, error message

assert type(1) == int, '문자열을 입력하였습니다.'
```

---

위의 검증식이 거짓일 경우를 발생합니다.

`raise`는 항상 예외를 발생시키고, 지정한 예외가 발생한다는 점에서 다릅니다.

### [연습] `assert`를 활용하여 예외 발생시키기

> 양의 정수 두개를 받아 몫과 나머지로 출력하는 함수 `def my_div(num1, num2)`를 작성하세요.
- assert를 활용하여, int가 아닌 경우 AssertionError를 발생시켜주세요.

```python
# 아래에 코드를 작성하세요.
```

```python
def my_div(num1, num2):
    pass
```

```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
```

```python
my_div(1, 2)
```

```python
my_div('1', '2')
```

```python
my_div(1, 0)
```
