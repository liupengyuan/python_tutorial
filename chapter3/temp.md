-  operator模块，含有各种操作符的函数如add等：https://docs.python.org/3.6/library/operator.html
-  高阶函数：map,filter,funtools.reduce
```python
from operator import add
from functools import reduce

numbers = map(abs, range(-10,10))
print(list(numbers))

numbers = filter(lambda x:x>2, range(-10,10))
print(list(numbers))

sum_num = reduce(add, range(10)) 
#按照给定的方法把输入参数中序列缩减为单个的值
print(sum_num)
```
-  用列表推导，生成器推导等替代
```python
numbers = [abs(i) for i in range(-10,10)]
print(list(numbers))

numbers = numbers = [i in range(-10,10) if i>2]
print(list(numbers))

sum_num = sum(range(10)) 
#按照给定的方法把输入参数中序列缩减为单个的值
print(sum_num)
```
-  itertools包含各种Combinatoric generators：https://docs.python.org/3.6/library/itertools.html
