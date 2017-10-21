**核心任务：对文本语料库统计，将结果保存为特定文件格式，将程序作为共享软件发布**

**10.1 任务描述**

文本语料库一般可视为存放在一个目录下的所有文本文件，该目录可能含有不定层次和数量的子目录与文本文件。真实语料库统计需要统计和展示的内容很多，本任务仅考虑对分词后的文本语料库，主要任务如下：
- 利用分词工具，将文本进行分词及词性标注(忘记写啦！！！！！！)
- 统计其总字节数、文本数、词频以及词的2gram频（连续两个词作为一个整体的频次）；
- 将统计结果保存为.csv格式及xlsx格式以及JSON格式；
- 将写好的代码作为共享软件发布到python第三方库的源仓库中（pypi），任何人均可以搜到并安装使用。

**10.2 得到目录下所有文件及文件大小（os模块使用初步）**

在XXXX下载文件YYY，在d:\下，新建子目录temp，将YYY内所有文件解压至temp目录中。打开temp目录，可以看到其中有很多文本文件，有很多文件夹。假设我们当前的任务是统计temp当前目录下的所有文本文件（不含子目录）。


键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-1

import os

path = r'd:\temp'
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

**10.3 模块导入与使用**

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
# 示例代码 C3-7
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

示例代码C3-7中:
- my_counter.count_words_freq_dict(file)是调用自定义包my_counter中的count_word_freq_dict函数，与以往导入模块并使用其中函数的方法没有不同。
- 注意，my_counter.py应与本示例代码在同一个目录下，否则import时会找不到该文件。

python解释器需要知道被import模块的所在位置，这就提供了两种方式确保python解释器能够找到我们自定义的模块：
- 将模块放到python解释器默认的搜索位置
- 告诉python解释器去哪里找（通过更改环境变量内容实现，方法可自行搜索）

python解释器默认的搜索位置顺序是：1、当前目录；2、path环境变量目录。其中，path环境变量目录的列表可用如下代码列出：

`import sys, pprint`

`pprint.pprint(sys.path)`

- 首先导入sys及pprint模块。
- sys.path可以得到当前环境的目录列表。
- 使用pprint是为了保证输出的易读性，利用pprint下的pprint()方法打印出当前环境的路径目录列表（sys.path），该方法类似print()函数。

因此，将我们自定义的模块/程序放置到当前目录或者上述代码列出的任意一个目录中，均能够被导入。

注意，由于对Counter对象的加法计算耗时较多，因此，可以考虑在示例代码3-7中直接原task9中示例程序9-36中的关键语句。

```python
#coding: utf-8
示例代码3-8
import os
from Collections import Counter

def count_words_dir(path):
    words_freq_dict = Counter()
    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            for line in file:
                words_freq_dict.update([word.split('/')[0] for word in line.split()])
    return words_freq_dict

# 测试
if __name__ == '__main__':
    path = r'd:\temp'
    print(list(count_words_dir(path))[:20])
```

当文件较多时，示例代码3-8的性能，将比示例代码3-7，有几倍的提升。

**10.4 输出结果为csv格式、xlsx格式及JOSN文件格式**

**10.4.1 输出结果到csv格式文件**

CSV是Comma-Separated Values的缩写，其文件以纯文本形式存储的数据，数据间默认为逗号分隔，但也可以用其他符号。存成csv文件格式与存为文本文件类似，只需要构造用逗号或其他符号分隔的形式，再以一般文本形式文件存储即可。

键入如下代码并运行。

```python
# coding:utf-8
# 示例代码 C3-8

'''
此部分与示例代码 C3-7部分相同
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
# 示例代码 C3-9

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

示例代码C3-9中：
- import csv，引入csv包
- reader = csv.reader(f)，建立一个reader对象，可以解析读取f中的行
- for line in reader，可以按行遍历解析的行
- data = list(reader)，可以直接将文件转为list
- print(data[1][1])，可以按照行与列索引获得对应数据

**10.4.2 输出结果到xlsx格式文件**

xlsx是当前excel最常用的文件格式，对此类文件操作一般可用第三方包：openpyxl。该包已随Anaconda一并安装。

键入如下代码并运行。

```python
# coding:utf-8
# 示例代码 C3-10

'''
此部分与示例代码 C3-7部分相同
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

示例代码C3-10中：
- import openpyxl引入openpyxl包
- wb = openpyxl.Workbook()，调用Workbook()函数，建立一个工作簿
- ws = wb.active，选择当前活动的表，用ws指向之。
- ws.cell(row=index, column=1).value = element[0]，首先调用工作表ws的cell()方法，该方法接受两个参数row及column，可得到工作表中相应坐标的格。然后将该格的值value设为element[0]。
- wb.save(filename='d:\code_temp\result.xlsx)，调用wb对象的save方法，将wb这个工作簿存入filename指定的文件。

可以到d:\code_temp中打开result.xlsx文件查看。

**10.4.3 输出结果到JSON格式文件**

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，JSON采用完全独立于语言的文本格式（就是一个字符串），几乎所有编程语言都有解析JSON的库，几乎已经成为互联网时代数据交换的标准格式。

JSON建构于两种结构：
- “名称/值”对的集合（A collection of name/value pairs），在python中可以理解为dict类型。
- “值的有序列表”（An ordered list of values），在python中可以理解为列表（list）。

具体JSON的介绍可参考官网：http://www.json.org/

python将JSON模块置于标准库中，用于处理JSON数据与python中数据或变量之间的转换。一般的，JSON可以用来存储python中的字符串、整型、浮点型、布尔型、列表、字典及NoneType等类型。

键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-11

import json

s = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(type(s))
print(s)
print('-'*30)
print(json.dumps({'c': 0, 'b': 0, 'a': 0}, sort_keys=True))
print('-'*30)
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

```

示例代码C3-11中：
- 首先导入json模块
- json.dumps()函数用于将Python变量（对象）**编码**成JSON字符串，这一过程也称为**序列化**，dumps就是dump string
- sort_keys是json.dumps()函数的一个参数，可以用来对字典进行排序
- indent是json.dumps()函数的一个参数，用于控制每行行首缩进，提升json的可读性
- 注意：输出的字符串中，所有的单引号'都自动变成了双引号"，json格式对字符串是采用双引号进行包裹的


再看下编码/序列化的反向操作，即**解码**，将json字符串解析成python对象的过程。

键入以下代码，并观察执行结果。

```python
# coding:utf-8
# 示例代码 C3-12

import json

foos = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(type(foos))
print(foos)
print('-'*30)
foos = print(json.loads('{"a": 0, "b": 0, "c": 0}'))
print(type(foos))
print(foos)

```

示例代码C3-12中：
- json.loads()函数用于将JSON字符串解码成Python变量（对象），这一过程也可称为**反序列化**，loads即load string


回到我们的任务中，键入以下代码并运行：


```python
# coding:utf-8
# 示例代码 C3-13

'''
此部分与示例代码 C3-7部分相同
后续代码从测试部分开始有所不同
'''

import json

if __name__ == '__main__':
    path = r'd:\temp'
    result = count_words_dir(path)
    with open(r'd:\code_temp\result.json', 'w') as f:
        json.dump(result, f)
        
    with open(r'd:\code_temp\result.json') as f:
        new_result = json.load(f)
    
    type(new_result)

```

示例代码C3-13中：
- json.dump(obj, fp)函数可以将python变量（对象）序列化并保存到文件中，obj参数是指向要序列化的对象，fp指向要存入的文件。
- json.load(fp)函数将json文件对象解析成python变量（对象）。

有关json在python中的更多细节，请参考官方文档：https://docs.python.org/3/library/json.html


**10.5 统计词的2gram频次**

统计词的2gram的频次，思路与统计词频类似。首先初始化一个空的字典，假设列表中存放分词的文本，我们需要从列表索引的第0位置开始，每次取出2个词(假设文本至少含有2个词汇)，依次放入字典并计数。

由于不能直接利用Counter进行计数，因此可仿照task9中示例程序9-25，键入以下代码并运行：

```python

#coding: utf-8
#示例程序 C3-14

from collections import defaultdict

def count_gram_freq_dict(filename):
    gram_freq_dict = defaultdict(int)
    
    with open(filename) as f:
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            for i in range(len(words)-1):
                gram_freq_dict['_'.join(words[i], words[i+1])] += 1
    return gram_freq_dict

```

示例程序C3-14中：
- words = [word.split('/')[0] for word in line.split()]，将文本中带词性的词存入words列表中
- gram_freq_dict['_'.join(words[i], words[i+1])] += 1，将words中连续两个词用_连接，并统计频次

还可以将示例程序C3-14稍加扩展，扩展为可统计词的任意gram频次的函数：

```python
#coding: utf-8
#示例程序 C3-15

from collections import defaultdict

def count_gram_freq_dict(filename, n=2):
    gram_freq_dict = defaultdict(int)
    
    with open(filename) as f:
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            if len(words) >= n:
                for i in range(len(words)-n+1):
                    gram_freq_dict['_'.join(words[i:i+n])] += 1
    return gram_freq_dict

```

示例程序C3-15中：
- def count_gram_freq_dict(filename, n=2)，定义了一个函数，该函数有两个参数，其中参数n是**默认参数**，可为参数提供默认值，调用函数时可传可不传该默认参数的值。因此，如果在调用该函数时，如果只有第一个filename参数，则默认函数参数n的值为2。


**10.6 包/模块的发布**

我们对语料库统计的代码十分满意，想将统计语料库的代码发布，以第三方包的形式共享给大家。届时，人们可以利用pip install安装这个语料库统计的包，并调用函数。这个过程一般称为项目打包与发布（Packaging and Distributing Projects），这个过程可以简单的分为三步。

a. 项目配置(Configuring your Project)

简单的说，就是整理好项目的目录，建立一些必要的安装配置及初始化文件。
- 打开一个powershell
- 键入d:并回车
- 键入md stat_test并回车，建立stat_test目录
- 键入cd stat_test并回车，进入该目录
- 建立stat_test.py文件并保存，内容是本小节完整代码
- 建立README.rst文件，该文件是项目的详细说明文档，文本格式，可参考官方示例文档https://github.com/pypa/sampleproject/blob/master/README.rst修改，存在stat_test目录下
- 建立setup.py文件，该文件基于官方示例文档https://github.com/pypa/sampleproject/blob/master/setup.py，内容大致如下：

```python
#coding: utf-8
#示例程序 C3-16

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='stat_test',
    version='0.1',
    description='stat_test',
    long_description=long_description,
    # The project's main homepage.
    url='https://github.com/liupengyuan/hello-world',
    # Author details
    author='liupengyuan',
    author_email='liupengyuan@pku.edu.cn',
    # Choose your license
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[       
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.      
        'Programming Language :: Python :: 3.6',
    ],
    # What does your project relate to?
    keywords='sample test for dist',
    # py_modules=["my_module"],    
)

```

示例程序C3-16中：
- name='stat_test'，指定项目名称
- url='https://github.com/liupengyuan/stat_test'，一般使url指向该项目在github上的项目地址，将stat_test中的所有文件上传到该项目目录下
- author='liupengyuan'，指明项目作者
- author_email='liupengyuan@pku.edu.cn'，指定项目作者邮件

除了以上修改外，对官方文档示例的setup.py暂先可以不做修改，直接复制即可。


b. 项目打包(Packaging your Project)

- 在d:\stat_test目录下，键入python setup.py sdist并回车，就创建了一个源代码发布包(source distribution)
最好同时建立一个Wheels包，其他用户安装时无需build这一过程，速度会更快。
- pip install wheel，安装wheel模块
- python setup.py bdist_wheel

c. 上传项目到PyPi(Uploading your Project to PyPi)

The Python Package Index(PypI) is a repository of software for the Python programming language. There are currently 116533 packages here.

- 到https://pypi.python.org/pypi注册用户，注意用户名与邮箱要与setup.py中的对应
- pip install twine，安装twine包，用于将项目上传到pypi上
- twine upload dist/*，将项目上传到pypi

访问https://pypi.python.org/pypi，用刚才注册过的账号密码登陆，可以发现新增了一个发布的项目test_test。

OK，现在世界任何python用户均可以利用pip install stat_test安装我们发布的包，并利用里面的函数进行语料库统计。



有关项目打包与发布，详细信息见官方文档：https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi。


**10.7 扩展与总结**

os模块
import 模块路径
import方式与原则
