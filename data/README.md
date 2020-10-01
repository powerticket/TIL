# Data

## Library

### csv

#### Quickstart

```python
import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    if row[4]:
        print(row[2], float(row[4]))
    else:
        print(row[2], -999)
f.close()
```



### [Matplotlib](https://matplotlib.org/).pyplot

#### Installation

```bash
$ python -m pip install -U matplotlib
```

```python
import matplotlib.pyplot as plt
```



#### Quickstart

##### Plot

```python
import matplotlib.pyplot as plt


plt.title('plot_marker')
plt.plot([1, 2, 3, 4], [12, 42, 25, 15], 'r.--', label='red circle')
plt.plot(list(reversed([1, 2, 3, 4])), [12, 42, 25, 15], 'g^:', label='green triangle')
plt.legend()
plt.show()
```

##### Histogram

```python
import matplotlib.pyplot as plt
import random

random_list = []
for _ in range(500):
    random_list.append(random.randint(1, 6))
plt.hist(random_list, bins=6)
plt.show()
```

##### Boxplot

```python
import matplotlib.pyplot as plt
import random

random_list = []
for _ in range(13):
    random_list.append(random.randint(1, 1000))
print(sorted(random_list))
plt.boxplot(random_list)
plt.show()
```



## 참고

[공공데이터포털](https://www.data.go.kr/)

