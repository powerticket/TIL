# Python Basic

## Documents

[Python 3.7.8 documentation](https://docs.python.org/3.7/index.html)

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

[List of Unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters#Latin_script)

[점프 투 파이썬](https://wikidocs.net/book/1)

[Can Integer Operations Overflow in Python?](https://mortada.net/can-integer-
operations-overflow-in-python.html)



## Syntax

### Comment

- `#` at one line comment

  ```python
  # comment
  ```

- `'''` or `"""` at multi-line comments

  ```python
  '''
  multi
  line
  comments
  '''
  ```



### Code

- Statement is a minimum code which is executable. One statement at one line is a basic rule in making python code.

  ```python
  print('Hello, World!')
  ```

- Can use `;` when you want to code statements in one line.

  ```python
  print('Hello,'); print('World!')
  ```

* Can use `\` or `'''` when you want to code statements in multi-line.

  ```python
  print('Hello, \
  World!')
  ```

  ```python
  print('''Hello,
  World!''')
  ```

- Can code multi-line without `\` or `'''` when defines`()`, `{}`, `[]`

  ```python
  list_l = [
      'l1',
      'l2',
      'l3'
  ]
  ```

  

## Variable

### Assignment Operator: `=`

- In python, `=` means assignment, not equality.

  ```python
  x = 'value'
  ```

* Use `type()` when you want to identify the type of value.

  ```python
  type(x)
  ```

* Use `id()` when you want to identify the address of value.

  ```python
  id(x)
  ```

- Can assign same value at once

  ```python
  x = y = 'same value'
  print(x); print(y)
  ```

* Can assign different value at once

  ```python
  x, y = 'differnt', 'value'
  print(x); print(y)
  ```

- It is possible to swap each value.

  ```python
  x, y = 'differnt', 'value'
  print(x); print(y)
  x, y = y, x
  print(x); print(y)
  ```



### Identifier

Identifier is a name of variable, function, module or class.

* Identifier is composed of alphabet, underscore(`_`), digits.

* It is not allowed to use digit as a first letter.

* Length is unlimited.

* Upper and lower-case alphabet is distinguished.

* Reserved words below are not allowed to use as a identifier.

  ```python
  False, None, True, and, as, assert, break, class, continue, def, del, elif,
  else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal,
  not, or, pass, raise, return, try, while, with, yield
  ```

- Can check reserved words by importing keyword.

  ```python
  import keyword
  print(keyword.kwlist)
  ```

* Have to avoid using a name of built-in function as a identifier.

  ```python
  print = 'hi'
  del print
  print(print)
  ```

  

## Data Type

- **Number**
- **String**
- **Boolean**

### Number
#### Integer: `int`

- No `long` type in python 3.x

- No overflow at `int` type unlike C language.

- Binary: `0b`, octal: `0o`, hexadecimal: `0x` number expressions

  ```python
  binary_number = 0b10
  print(binary_number)
  octal_number = 0o10
  print(octal_number)
  hexadecimal_number = 0x10
  print(hexadecimal_number)
  ```

  ```python
  import sys
  print(sys.maxsize * sys.maxsize)
  ```



#### Floating point number: `float`

- Not always same value because of floating point rounding error.

  ```python
  print(bool(3.5 - 3.2 == 0.3))
  ```

  ```python
  a = 3.5 - 3.2
  b = 0.3
  round(a, 2) == b
  ```

  ```python
  import sys
  print(sys.float_info.epsilon)
  abs(a - b) <= sys.float_info.epsilon
  ```

  ```python
  import math
  math.isclose(a, b)
  ```

- Can use `E`(or `e`)-expression.

  ```python
  b = 314e-2
  type(b)
  ```



#### Complex number: `complex`

- Can be expressed by `j` and each complex numbers have both real and imagine part.

  ```python
  x = 3 + 4j
  print(x.real); print(x.imag)
  ```

- Complex number expressed as string with no spaces also can be converted to `float` type

  ```python
  b = complex('3+4j')
  type(b)
  ```

  

### String

* Can express using single quotes(`'`), double quotes(`"`).

  ```python
  print('Hello, World!')
  ```

* Triple single or double quotes are expression of multi-line.

  ```python
  """multi
  lines
  """
  '''multi
  lines
  '''
  ```



### Escape sequence

- Use escape sequence(`\`) to disguish special character.

|Reserved word|Meaning|
|:--------:|:--------:|
|\n|Line change|
|\t|Tap|
|\r|Carriage return|
|\0|Null|
|\\\\ |`\`|
|\\'|Single quotes(`'`)|
|\\"|Double quotes(`"`)|

```python
print('''Hello,
this is
python\n''')
print('Hello,\nthis is\npython\t')
```

```python
print('\\ - $ USD')
print('\ - $ USD')
print("This is \"python\".")
```

```python
print('hello', end=",\t2020")
print('ssafy')
```



### String interpolation

* `%-formatting`

* [`str.format()` ](https://pyformat.info/)

* [`f-strings`](https://www.python.org/dev/peps/pep-0498/) :  Support above python version 3.6

```python
name = 'ashley'
```

```python
print('My name is %s.' % name)
```

```python
print('My name is {}.'.format(name))
```

```python
print(f"My name is {name}.")
```

```python
print(f'''My name
is
{name}.''')
```

```python
import datetime
now = datetime.datetime.now()
print(now)
```

```python
print(f'This year is {now:%Y}, this month is {now:%m}, today is {now:%d}.')
```

```python
pi = 3.141592
r = 10
print(f'{pi:.3}, area is {pi * r * r:.3}')
```



## Boolean type

There is a type `bool` composed with `True` and `False` values.

Belows are transformed as `False`.
```
0, 0.0, (), [], {}, '', None
```

```python
type(True)
type(False)
```

```python
print(bool(0))
print(bool(.0))
print(bool(0.))
print(bool(0.00000000))
print(bool(False))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(''))
print(bool(""))
print(bool(None))
```



### None type

There is a type `none` in python for presenting there is no value.

```python
type(None)
```

```python
a = None
print(type(a))
print(a)
type(a)
```



## Type conversion & Typecasting

### Implicit type conversion

* bool
* Numbers (int, float, complex)

```python
print(True + 3)
print(False + 3.14)
print(True + 1 + 2j)
```

```python
int_number = 2020
float_number = 3.14
complex_number = 2 + 3j
```

```python
print(int_number + float_number)
print(type(int_number + float_number))
```



### Explicit type conversion

`int()`, `float()`, `complex()`, `string()`, `tuple()`, `list()`, `dict()`, `set()`

* Proper form of string can be transformed to integer.
* Every integer can be transformed to string.
* Other various type can be transformed to another if it has proper form.



# Operator

- 산술 연산자
- 비교 연산자
- 논리 연산자
- 복합 연산자
- 기타 연산자

## 산술 연산자
Python에서는 기본적인 사칙연산이 가능합니다.

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

- 나눗셈 (`/`) 은 항상 float를 돌려준다.
- 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 `//` 연산자를 사용한다.

```python
# 2의 1000승을 확인해봅시다.
```

```python
2 ** 1000
```

```python
# 나눗셈과 관련된 산술연산자를 활용해봅시다.
```

```python
print(type(5 / 2))
print(5 / 2)
print(type(5 // 2))
print(5 // 2)
print(type(5 % 2))
print(5 % 2)
```

```python
# divmod는 나눗셈과 관련된 함수입니다.
```

```python
divmod(5, 2)
```

```python
# 음수 양수 표현도 해봅시다.
```

```python
num = 2020
-num
```

## 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|

```python
# 숫자의 대소관계를 비교해봅시다.
```

```python
print(5 >= 1)
print(3 > 6)
```

```python
# 다른 숫자인지 확인해봅시다.
```

```python
3 != 3.0
```

```python
# 같은 숫자인지 확인해봅시다.
```

```python
3.0000000000000000000000000 == 3.0
```

```python
# 문자열도 같은지 확인해봅시다.
```

```python
print('hello' == 'hello')
print('hello' == 'Hello')
```

## 논리 연산자

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자입니다.

```python
# and과 관련해서 모든 case를 출력해봅시다.
```

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

```python
# or과 관련해서 모든 case를 출력해봅시다.
```

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

```python
# not을 활용해봅시다.
```

```python
print(not True)
print(not False)
```

* 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
* 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.

### 단축평가
* 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음
* 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

```python
vowels = ['a', 'e', 'i', 'o', 'u']
```

```python
print('b' and 'a' in vowels)
print('a' and 'b' in vowels)
print('b' or 'a' in vowels)
print('a' or 'b' in vowels)
```

```python
print('a' and 'b') # 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
print('a' or 'b')  # 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.
print(False and 'b')
print(False or 'b')
```

```python

```

```python

```

- `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.
- `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.

```python
# and의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
```

```python

```

```python
# or의 단축평가(short-circuit evaluation)에 대해서 알아봅시다.
```

```python

```

## 복합 연산자

복합 연산자는 연산과 대입이 함께 이뤄집니다.

가장 많이 활용되는 경우는 반복문을 통해서 개수를 카운트하거나 할 때 활용됩니다.

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

```python
# 복합연산자는 이럴 때 사용됩니다.
```

```python
cnt = 0
while cnt < 5:
  print(cnt)
  cnt = cnt + 1
print()
cnt = 0
while cnt < 5:
  print(cnt)
  cnt += 1
```

## 기타 주요 연산자

### Concatenation

숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있습니다.

```python
# 문자열을 더해봅시다.(합쳐봅시다.)
```

```python
'pp' + 'ap'
```

```python
# list를 더해봅시다.(합쳐봅시다.)
```

```python
[1, 2, 3] + [4, 5, 6] + [1, 2, 3]
```

### Containment Test

`in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있습니다.

```python
# 문자열안에 특정한 문자가 있는지 확인해봅시다.
```

```python
print('a' in 'hello')
print('e' in 'hello')
```

```python
# list안에 특정한 원소가 있는지 확인해봅시다.
```

```python
print(0 in [1, 2, 3, 5, 7])
print(5 in [1, 2, 3, 5, 7])
```

```python
# range안에 특정한 원소가 있는지 확인해봅시다.
```

```python
print(45 in range(45))
print(45 in range(46))
```

### Identity

`is` 연산자를 통해 동일한 object인지 확인할 수 있습니다. (OOP 파트에서 다시 학습하게 됩니다.)

```python
# 파이썬에서 -5 부터 256 까지의 id는 동일합니다.
```

```python
print(id(5))
print(id(6))
print(id(7))
```

```python
# 257 이루의 id 는 다릅니다.
```

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))
print(a is b) # print(id(a) == id(b))
```

### Indexing/Slicing
`[]`를 통한 값을 접근하고, `[:]`을 통해 리스트를 슬라이싱할 수 있습니다. (Container 파트에서 자세하게 학습합니다.)

```python
# 문자열을 인덱싱을 통해 값에 접근해봅시다.
```

```python
print([1, 2, 3, 4, 5][3])
print([1, 2, 3, 4, 5][1:3])
print([1, 2, 3, 4, 5][1:3][0:])
print([1, 2, 3, 4, 5][1:3][0:][0])
```

## 연산자 우선순위

0. `()`을 통한 grouping

1. Slicing

2. Indexing

3. 제곱연산자
    `**`

4. 단항연산자
    `+`, `-` (음수/양수 부호)

5. 산술연산자
    `*`, `/`, `%`

6. 산술연산자
    `+`, `-`

7. 비교연산자, `in`, `is`

8. `not`

9. `and`

10. `or`

```python
# 우선순위를 확인해봅시다.
```

```python
print(-3 ** 6)
print((-3) ** 6)
```

### [참고] 표현식(Expression) & 문장(Statement)

### 표현식(Expression)

> 표현식 => `evaluate` => 값

* 하나의 값(value)으로 환원(reduce)될 수 있는 문장
* `식별자`, `값`(리터럴), `연산자`로 구성됩니다.
* 표현식을 만드는 문법(syntax)은 일반적인 (중위표기) 수식의 규칙과 유사합니다.
* [참고] [표현식(Expression) 문법 관련
공식문서](https://docs.python.org/3/reference/expressions.html)

```python
# 하나의 값(value)도 표현식(expression)이 될 수 있습니다.
```

```python
35 + 35
```

```python
# 표현식은 하나의 값으로 평가(evaluate)될 수 있어야 합니다. 그러면 할당문(assignment statement)은 표현식일까요?
```

```python
a = 5 # 할당문은 표현식이 아니다.
a
```

```python
# 식별자가 값이 할당되어 있는 경우 수식의 일부가 될 수 있습니다.
```

```python
3 + a
```

```python
# 표현식을 만드는 문법(syntax)은 일반적인 (중위표기) 수식의 규칙과 유사합니다. 아래와 같은 문장은 표현식이 될 수 없습니다.
```

```python
3 ** 4 + 4 ** 2
```

### 문장(Statement)

* 파이썬이 실행 가능한 최소한의 코드 단위 (a syntatic unit of programming)

```python
# 하나의 값(value)도 문장이 될 수 있습니다.
```

```python
'hello'
```

```python
# 표현식(expression)도 문장이 될 수 있습니다.
```

```python
3 + 5
```

```python
# 실행 가능(executable)해야 하기 때문에 아래의 코드는 문장이 될 수 없습니다.
```

```python
print(
```

### 문장과 표현식의 관계

<center><img width="600" height="300" src="https://user-
images.githubusercontent.com/9452521/87619771-f41f5e00-c757-11ea-9e4b-1f76e4ca0981.png",
alt="variable"/></center>

# 정리

## 변수(Variable)와 자료형(Data Type)

<center><img width=800 height=400 src="https://user-
images.githubusercontent.com/9452521/87640197-55a7f280-c781-11ea-9cff-19c022ce704a.png",
alt="variable"/></center>
