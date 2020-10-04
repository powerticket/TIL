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

##### Bar

```python
import matplotlib.pyplot as plt
import random


random_list = []
for _ in range(20):
    random_list.append(random.randint(1, 50))
print(random_list)
plt.bar(range(1, 21), random_list)
plt.show()
plt.barh(range(1, 21), random_list)
plt.show()
```

##### Pie

```python
import matplotlib.pyplot as plt


plt.axis('equal')
data = [10, 20, 15, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.pie(data, labels=labels, autopct='%.1f%%', colors=colors, explode=(0, 0, 0.1, 0), startangle=90)
plt.legend()
plt.show()
```



#### Reference

- [Color](https://matplotlib.org/examples/color/named_colors.html)



### [NumPy](https://numpy.org/)

#### Installation

```bash
$ pip install numpy
```



#### Quickstart

```python
import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
```



### [pandas](https://pandas.pydata.org/)

#### Installation

```bash
$ pip install pandas
```



#### Quickstart

```python
import pandas as pd


df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
summer = df[1].iloc[:,:5]
summer.columns = ['경기수', '금', '은', '동', '계']
print(summer.sort_values('금', ascending=False))
summer.to_excel('하계올림픽메달.xlsx')
```





## 참고

[공공데이터포털](https://www.data.go.kr/)

