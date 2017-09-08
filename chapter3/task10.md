核心任务：对文本语料库统计，将结果保存为特定文件格式，将程序作为共享软件发布

10.1 任务描述 文本语料库一般可视为存放在一个目录下的所有文本文件，该目录可能含有不定层次和数量的子目录与文本文件。真实语料库统计需要统计和展示的内容很多，本任务仅考虑对分词后的文本语料库，主要任务如下：
- 统计其总字节数、文本数、词频以及词的2gram频（连续两个词作为一个整体的频次）；
- 将统计结果保存为.csv格式及xlsx格式以及JSON格式；
- 将写好的代码作为共享软件发布到python第三方库的源仓库中（pypi），任何人均可以搜到并安装使用。

10.2 得到目录下所有文件及文件大小（os模块使用初步）

在XXXX下载文件YYY，在d:\下，新建子目录temp，将YYY内所有文件解压至temp目录中。打开temp目录，可以看到其中有很多文本文件，有很多文件夹。假设我们当前的任务是统计temp当前目录下的所有文本文件（不含子目录）。


键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-1

import os

files = os.listdir(path)
for file in files:
    print(file)
```
示例代码C3-1中：

- import os引入了os模块，该模块主要包含操作系统相关的各种函数，如各类对目录及文件操作的函数。
- os.listdir(path)函数可以返回给定参数path内的所有条目的列表。可在文件管理其中打开D:\temp目录进行对比，会发现其中包含所有的文件名与子目录名，但是不包含.与..这两个特殊条目（一个代表本层目录，一个代表上层目录）。

键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-2
# 统计一个目录下所有文件的个数及字节数（不含子目录）
import os

def count_path(path):
    number = 0
    size = 0
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(file):
            number += 1
            file_size = os.path.getsize(file)
            size += file_size
    return number, size

# 测试
if __name__ == '__main__':
    path = r'd:\temp'
    number, size = count_path(path)
    print('File number is {}, file size is {}.\n'.format(number, size))

```
示例代码C3-2中：

- os.path.isfile(name)函数可以判断参数name是否是文件，如果是就返回True，否则就返回False。这里的目的是仅需要文件名，过滤掉文件夹名。
- os.path.getsize(file)函数可以得到参数file文件的大小（字节数）。

统计temp目录下所有文本文件（不含子目录）的词频也可以类似处理如下。

```python
# coding:utf-8
# 示例代码 C3-3
# 统计一个目录下所有文件的词频（不含子目录）

import os
from collections import Counter

def count_words_path(path):
    words_freq_dict = Counter()
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(file):
            words_freq_dict += count_words_freq_dict(file)
    return words_freq_dict

```

示例代码C3-3中：
- count_words_freq_dict(file)是task9中示例程序9-36中的函数。

下面考虑要统计一个目录下所有文件以及子目录的情况。

键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-4

import os

for root, dirs, files in os.walk(path):
    print('当前目录:', root)
    print('当前目录下的目录:', dirs)
    print('当前目录下的文件:', files)
    print('-'*30)
```

示例代码C3-4中：

- os.walk(path)函数接受一个字符串参数（文件目录名），可以获得该目录下所有目录名（含自身）及文件名。执行时会产生一个3元组 (dirpath, dirnames, filenames)，其中dirpath是一个字符串，也就是当前遍历到的目录路径名，dirnames是当前dirpath目录下所有子目录的列表，filenames是当前dirpath目录下所有文件的列表。
- 注意，dirnames及filenames并不包含完整路径，只保存在当前路径dirpath下的相对路径。


键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-5

import os

def count_dir(path):
    number = 0
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            number += 1
            file = os.path.join(root, file)
            file_size = os.path.getsize(file)
            size += file_size
    return number, size
 
# 测试
if __name__ == '__main__':
    path = r'd:\temp'
    number, size = count_dir(path)
    print('File number is {}, file size is {}.\n'.format(number, size))

```

示例代码C3-5中：

- join(root, file)是os.path模块下的一个函数，接受两个字符串参数，可返回root路径名与file文件名连接起来组成的完整文件名。该函数连接文件名的特点是不受操作系统的影响（windows上用\分隔目录及文件名，而Linux及OS X用/）。
- os.path.getsize(file)是os.path模块下的一个函数，接受一个字符串参数（文件全名），可返回该文件的大小，以字节数返回。


统计temp目录下所有文本文件（含子目录）的词频可类似处理如下。

```python
# coding:utf-8
# 示例代码 C3-6
# 统计一个目录下所有文件的词频（含子目录）

import os
from Collections import Counter

def count_words_dir(path):
    words_freq_dict = Counter()
    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            words_freq_dict += count_words_freq_dict(file)
    return words_freq_dict

```
示例代码C3-6中：
- count_words_freq_dict(file)是task9中示例程序9-36中的函数。

确实可以将task9中示例程序9-36中的函数count_words_freq_dict(file)直接copy过来，但我们更希望能不复制代码，直接调用该函数---人类讨厌重复。

10.3 模块导入与使用

在以往的示例程序中，很多都进行了模块导入（import），如内置的标准库中的math，Collection的Counter及os等，非标注库（也称第三方库）bokeh等。这些模块是什么样子？放在哪里了呢？

假设Anaconda存放在D:\下。

- 打开一个powershell
- 键入d:并回车（转到d盘）
- cd anaconda\lib并回车（转到anaconda\lib目录）
- dir os.py并回车（列出当前目录下的os.py文件）

这个位于Anaconda\lib目录下的os.py文件，就是我们import os时候所导入的模块。标准库的模块，均在Anaconda\lib目录下。而类似于bokeh等第三方模块，则位于Anaconda\lib\site-packages下。

利用import将模块导入时，模块随即被执行。于是，模块内的各种函数，可以被调用。

此外，模块是单个python源文件，而由多个python源文件组成的目录，则被称之为包（package），比如bokeh。但并不是随便在Anaconda\lib下或Anaconda\lib\site-packages下建立一个目录，并放入几个python源程序就可以称为包并可被导入。

在Anaconda\lib目录下，我们查看各个目录（除了__pycache__目录，这个是缓存文件目录）里面的文件，会发现每一个目录内均有__init__.py文件。只有含有__init__.py文件的目录，python才会认为该目录是一个包，虽然该文件内容很多时候可以是空。

（包目录结构图）


下面将自己写的python源程序作为模块导入。

- 关闭浏览器及当前powershell
- 重新打开一个powershell
- 键入d:并回车，转到d盘
- 键入md code_temp并回车（建立了code_temp目录）
- 键入cd code_temp（进入code_temp目录）
- 利用记事本建立新文件my_counter.py，将task9中示例程序9-36拷贝，保存文件（utf-8格式）并退出。
- 在当前目录下，进入jupyter notebook编程环境
- 键入import my_counter并执行该单元格，观察执行结果
- 将my_counter.py文件的最后两行代码替换为main()（注意前面没有空格），保存文件
- 键入import my_counter并执行该单元格，观察执行结果

第一次import my_counter后，程序与以往import其他模块时候，没有什么不同（都没什么动静，笑）。

第二次import my_counter后，程序会直接执行my_counter.py中的main()函数。

这是由于，每一个python程序在运行时，都会自动定义一个变量__name__。如果是直接运行程序，则__name__的值为字符串'__main__'，如果是因为import导入而导致程序被运行，则__name__的值为该程序名。

因此，第一次import my_counter，运行my_counter.py时，__name__的值为'my_counter'，所以main()不会被执行（这也是我们一般希望的结果）。

而第二次import my_counter，运行改过的my_counter.py时，由于去掉了if __name__ == '__main__'这个判断，因此main()函数会被执行。

统计temp目录下所有文本文件（含子目录）的词频可通过导入my_counter模块如下：

```python
# coding:utf-8
# 示例代码 C3-6
# 统计一个目录下所有文件的词频（含子目录）

import os
from Collections import Counter
import my_counter

def count_words_dir(path):
    words_freq_dict = Counter()
    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            words_freq_dict += my_counter.count_words_freq_dict(file)
    return words_freq_dict

# 测试
if __name__ == '__main__':
    path = r'd:\temp'
    print(list(count_words_dir(path))[:20])

```

示例代码C3-6中:
- my_counter.count_words_freq_dict(file)是调用自定义包my_counter中的count_word_freq_dict函数，与以往导入模块并使用其中函数的方法没有不同。

10.4 输出结果为csv格式、xlsx格式及JOSN文件格式

CSV是Comma-Separated Values的缩写，其文件以纯文本形式存储的数据，数据间默认为逗号分隔，但也可以用其他符号。存成csv文件格式与存为文本文件类似，只需要构造用逗号或其他符号分隔的形式，再以一般文本形式文件存储即可。

键入如下代码并运行。

```python
# coding:utf-8
# 示例代码 C3-7

'''
此部分与示例代码 C3-6部分相同
后续代码从测试部分开始有所不同
'''

if __name__ == '__main__':
    path = r'd:\temp'
    result = count_words_dir(path)
    with open(r'd:\code_temp\result.csv', 'w') as f:
        for word, freq in result.items():
            f.writeline(','.join(word, freq))        
```

可以用excel打开位于d:\code_temp下的result.csv文件，也可以直接用记事本等文本编辑器打开。

对于csv格式文件，python内置了专门用来处理csv格式文件的模块：csv。更多时候，由于csv格式文件的分隔符不一定是逗号，允许转义字符，允许逗号成为值的一部分，因而用split()方法不易处理，而csv模块可以直接解析，因此其用于文件读入比较方便：

```python
# coding:utf-8
# 示例代码 C3-8

import csv

with open(r'd:\code_temp\result.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
        print(line)
        print('-'*30)
        break
    
    data = list(reader)
    print(data[1][1])
```

示例代码C3-8中：
- import csv，引入csv包
- reader = csv.reader(f)，建立一个reader对象，可以解析读取f中的行
- for line in reader，可以按行遍历解析的行
- data = list(reader)，可以直接将文件转为list
- print(data[1][1])，可以按照行与列索引获得对应数据


xlsx是当前excel最常用的文件格式，对此类文件操作一般可用第三方包：openpyxl。该包已随Anaconda一并安装。

键入如下代码并运行。

```python
# coding:utf-8
# 示例代码 C3-9

'''
此部分与示例代码 C3-6部分相同
后续代码从测试部分开始有所不同
'''

import openpyxl

if __name__ == '__main__':
    path = r'd:\temp'
    result = count_words_dir(path)
    wb = openpyxl.Workbook()
    ws = wb.active
    for index, element in enumerate(list(result)):
        ws.cell(row=index, column=1).value = element[0]
        ws.cell(row=index, column=2).value = element[1]
    wb.save(filename=r'd:\code_temp\result.xlsx')
        
```

示例代码C3-9中：
- import openpyxl引入openpyxl包
- wb = openpyxl.Workbook()，调用Workbook()函数，建立一个工作簿
- ws = wb.active，选择当前活动的表，用ws指向之。
- ws.cell(row=index, column=1).value = element[0]，首先调用工作表ws的cell()方法，该方法接受两个参数row及column，可得到工作表中相应坐标的格。然后将该格的值value设为element[0]。
- wb.save(filename='d:\code_temp\result.xlsx)，调用wb对象的save方法，将wb这个工作簿存入filename指定的文件。

可以到d:\code_temp中打开result.xlsx文件查看。









10.x 扩展与总结：

os模块
import方式与原则
