# 任务：搭建可视化网站：xxx.xxxx.xxx

**xx.1 Echarts入门**

**1. Echarts介绍**  
ECharts，一个纯 Javascript 的图表库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖轻量级的 Canvas 类库 ZRender，提供直观，生动，可交互，可高度个性化定制的数据可视化图表。
ECharts 3 中加入了更多丰富的交互功能以及更多的可视化效果，并且对移动端做了深度的优化。

Echarts官网所列重点特点基本如下：
- 丰富的图表类型
- 支持多个坐标系
- 针对移动端优化
- 深度交互式数据探索
- 可实现大数据量展现
- 支持多维数据、动态数据、特效、视觉编码手段丰富

但，其实以上都不是重点，`bokeh`也能在网页内展示类似效果，真正重点如下：
- 国货且开源
- 中文文档且文档丰富
- 国人使用较多，这样容易解决使用中出现的各类问题
- 百度开发，因而echarts开发技术有较高保障，项目也会有较强的延续性


**2. 迅速上手使用**

**2.1 建立工作目录**

windows下，在`D:`下建立目录`my_app`，其他环境请类似相应建立目录。
- 下载echarts至工作目录  
浏览器中，打开：http://echarts.baidu.com/download.html
这里先下载完整版`http://echarts.baidu.com/dist/echarts.min.js`，下载到工作目录`D:\my_app`。以后可以视需要选择版本下载。

**2.2 建立最基本的`html`文件**

利用记事本或其他文本编辑器，在工作目录`D:\my_app`下，建立文件`first.html`，注意，将文件扩展名`txt`更改为`html`。文件内容如下：

```html
<!--示例代码xx-1-->

<html>
  <head>
    <title>first_html网页文件</title>
  </head>
  <body>
    Hello, world!
  </body>
</html>
```
双击这个`first.html`文件，观察运行结果。

这个`first.html`是我们实现的第一个网页，该网页是用`html`语言写成的，`html`称为超文本标记语言 (Hyper Text Markup Language)。它是一种标记语言，确切的说，是一套标签集，用以描述网页。标签是由尖括号包围关键词，一般是成对出现的，一对标签间的内容是该对标签的描述对象。

示例代码xx-1中：
- `<html>`与`</html>`标签描述两者之间的内容是网页
- `<head>`与`</head>`标签描述两者之间的内容是网页头部（注意，很多头部内的信息将来不显示在网页上）
- `<title>`与`<title>`标签描述两者之间是抬头信息（显示在网页抬头中）
- `<body>`与`</body>`标签描述两者之间的内容是网页内容（显示在网页页面中）
- `<!--`为`html`语言的注释开始，中间的字符为注释，最终以` -->`作为注释结尾。

有关`html`的更多内容，可参考：http://www.w3school.com.cn/html/index.asp

**2.3 在网页中引入echarts**

在工作目录`D:\my_app`下，建立文件`index.html`。文件内容如下：

```html
<!--示例代码xx-2-->

<html>
<head>
<title>未来图表页面标题</title>
    <!-- 引入 ECharts 文件 -->
    <script src="echarts.min.js"></script>
</head>
<body>
未来图表页面内容
</body>
</html>
```

将这个文件用`utf-8`编码保存（本章如无特殊说明，文件一律用`utf-8`编码保存，否则可能会出现意想不到的错误）。然后双击该文件观察结果。

示例代码xx-2中：

- `<script src="echarts.min.js"></script>`，这行中的`<script>`标签标示两者之间是脚本语言代码，`src="echarts.min.js"`表示引入`echarts`模块文件。有了它，后面的可视化展示图表才能被调用。比较类似于`python`的`import`模块或包的功能。有关`javascript`的内容，请参考：http://www.w3school.com.cn/javascript/index.asp


**2.4 图表布置**

我们来看下图表布置，也就是对将在`<body>......</body>`中显示的图表进行布置。  
用文本编辑器打开方才的`index.html`文件，将`body`部分用如下示例代码xx-3替换。

```html
<!--示例代码xx-3-->

<body>
    <!--准备一块画布-->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 初始化这块画布
        var myChart = echarts.init(document.getElementById('main'));

        // 显示准备好的图表（各项参数对应的值暂时为空）
        myChart.setOption( {xAxis: {}, yAxis: {}, series: [] , title: {}, tooltip: {}, legend:{} });

    </script>
</body>
```

将`index.html`文件保存后运行，浏览器中将会显示两条直线，分别代表x与y轴（其他因为值为空，所以不显示）。

示例代码xx-3中：
- `<div id="main" style="width: 600px;height:400px;"></div>`：
    - `<div>......</div>`，这里可暂视为将网页切出一部分，在其中将对这部分进行风格样式等的定义。
    - `id="main" `，将这部分起个名字/给个标签为：`main`，后续可以根据这个`id`找到这部分。
    - `style="width: 600px;height:400px;">`，定义了一个宽600，高400的区域（画布，也就是后续图表整体大小）。
- `<script type="text/javascript">......</script>`，表示之间是脚本代码区域，且是`javascript`脚本代码。
- `var myChart = echarts.init(document.getElementById('main'))`：
    - `var myChart`，定义变量`mychart`。
    - `document.getElementById('main')`，调用`document`文档对象的`getElementById()`方法，参数为`main`。即获取指定id为`main`的对象，也就是上述`div`对象。`document`文档对象在`echarts.min.js`中定义。
    - `var myChart = echarts.init(document.getElementById('main'))`，将网页这部分初始化为`echarts`对象，并赋值给`myChart`。此时我们可以认为，`myChart`就是一个高400宽600的一个区域，后面将对这个变量进行操作，在这个区域上画图。
- `myChart.setOption( {xAxis: {}, yAxis: {}, series: [] , title: {}, tooltip: {}, legend:{} });`
    - 调用`myChart`的`setOption()`方法，参数为一个词典/dict，里面是图表的各项设置与数据。
    - 在词典中，多个设置参数用`,`分隔，每个设置都是一个键值对。`xAxis: {}`是对x轴的设置，`yAxis: {}`是对y轴的设置，当前x及y轴对应的值为`{}`，即空；`series: []`是系列数据，值为空；`title: {}`是图表标题，值为空；`tooltip: {}`是浮动提示，值为空；`legend:{}`是图例，值为空。

在决定以何种图表类型进行显示后，图表的布局一般就可以被预先确定好。

用文本编辑器打开方才的`index.html`文件，将` myChart.setOption( {xAxis: {}, yAxis: {}, series: [] , title: {}, tooltip: {}, legend:{} });`这一行代码用如下示例代码xx-4替换。

```javascript
//示例代码xx-4

        // 显示准备好的图表布置
        myChart.setOption({
			xAxis: {
				data: []
			},
			yAxis: {},
			series: [{
				name: 'area',
				type: 'bar',
				data: []
			}],
			title: {
				text: 'example'
			},
			tooltip: {},
			legend: {
				data:['area']
			},
		});

```

保存`index.html`后运行，观察其在浏览器中的执行结果。

示例代码xx-4其实就只有一行代码，为了便于阅读分成了多行，这是一种良好的编程风格，其中：
- `xAxis`键的值为一个词典，其中`data`键的值是一个空列表
- `series`键的值为一个列表，列表内是一个词典dict：
    - `name`键的值为字符串，该值一般要与`legend`中`data`列表中的值对应，表示系列数据的名称
    - `type`键的值为字符串，表示图表类型，`bar`就是柱状图
    - `data`键的值为列表，即柱状图要显示的数据
- `title`键的值为一个词典，其中的键为`text`，其值是一个字符串，显示在图表左上方
- `legend`键的值为一个词典，其中的键为`data`，其值是一个列表，显示在图表正上方

图表布置好以后，下面将对最重要的部分---数据进行填充展示。

**2.5 数据填充展示**
 
用文本编辑器打开方才的`index.html`文件，在示例代码xx-4下一行添加如下示例代码xx-5。

```javascript
//示例代码xx-5

 myChart.setOption({
    xAxis: {
        data: ["北语","北大","清华","北航","北邮","北外"]
    },
    series: [{
        data: [100, 500, 1000, 400, 400, 250]
    }]
});
```


保存`index.html`后运行。

从示例代码xx-5可以看到，只是对`xAxis`键的`data`的值，`series`键的`data`的值进行了覆盖。  
在示例代码xx1-4的图表布置下，未来如果我们换一组数据，填充不同的`data`，则可以显示不同的柱状图。

完整示例如下：

```html
<!--示例代码xx-6-->

<html>
<head>
    <!-- 引入 ECharts 文件 -->
    <script src="echarts.min.js"></script>
</head>
<body>
    <!--准备一块画布-->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 初始化这块画布
        var myChart = echarts.init(document.getElementById('main'));

        // 显示准备好的图表布置
		myChart.setOption({
			title: {
				text: '完整示例'
			},
			tooltip: {},
			legend: {
				data:['area']
			},
			xAxis: {
				data: []
			},
			yAxis: {},
			series: [{
				name: 'area',
				type: 'bar',
				data: []
			}]
		});
		
		// 显示图表数据
		 myChart.setOption({
			xAxis: {
				data: ["北语","北大","清华","北航","北邮","北外"]
			},
			series: [{
				data: [100, 500, 1000, 400, 400, 250]
			}]
        });
    </script>
</body>
</html>
```

示例代码xx-6中两个`myChart.setOption`部分的内容可以合并，效果相同，请读者自行完成。

恭喜，至此我们已经利用echarts完成了一个虽小，但是还算是完整的可视化网页实例，虽然只有一个`html`网页的柱状图内容。 

更多时候，我们想把这个网页也展示给别人而不仅仅是自己自娱自乐，我们期望未来会有用户以浏览器链接（URL）的方式来远程访问这个网页，然后看到我们想展示的内容。这种需求，比较快捷的方式是利用开源的web后端框架来满足。


**xx.2 Flask入门**

**1. Flask介绍**  
Flask是使用Python编写一个微型/轻量级Web开发框架，微型/轻量级意为使用简单的核心，用extension 进行功能扩展，实际应用中Flask搭建的网站也可以处理大规模百万级别的用户。  
Web开发框架是将Web开发中比较复杂的过程集成封装起来，在Web开发框架上开发Web应用，更有效率。  
python下Web开发框架最常用的即Flask与Django。这里介绍Flask的原因除了个人偏好外，还在于：

-  简单易上手
-  文档齐全
-  代码简洁且易于扩展


**2. 迅速上手使用**

**2.1 下载安装Flask**

由于Anaconda中自带Flask，因此本步骤可以省略。否则可以进入到`powershell`，在其中运行：`pip install Flask`。这样就装好了Flask。

**2.2 第一个Flask应用：Hello, world**

```python
#示例代码xx-7

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

- 利用文本编辑器等将以上代码键入文件并起名为`hello_world.py`存放到`D:\my_aap`下。
- 进入`powershell`，键入`cd D:\my_app`可转到`D:\my_aap`目录。
- 在`powershell`中键入`python hello_world.py`，运行这个文件。
- 在浏览器中访问`127.0.0.1:5000`并回车，观察执行结果。

示例代码xx-7中：
- `from flask import Flask`，从`flask`中引入`Flask`对象。
- `app = Flask(__name__)`，声明了一个Flask实例，也就是Web应用对象。如果你使用的是单一的模块（就如本例），第一个参数应该使用` __name__`，也就是本应用的名称变量，这样 Flask才会知道去哪里寻找模板、静态文件等等。
- `@app.route('/')`，装饰器，定义一个路由，告诉Flask哪个URL能触发并执行哪个函数。或者说，`route()` 装饰器是用于把一个函数绑定到一个URL 上。如对当前地址如`127.0.0.1:5000`，访问时会触发并执行紧随的`hello_world()`函数(因为一般当前地址默认为访问其根目录`\`)。也即是说URL：`127.0.0.1:5000`绑定了函数`hello_world()`。
- `hello_world()`，就是一个普通函数，只不过返回的字符串`Hello, World!`是到浏览器。
- ` app.run()`，`app`对象的执行函数。

回到`powershell`，并请按control-C来停止Flask服务。

**2.3 扩展**

```python
#示例代码xx-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index!'
    
@app.route('/hello/')
def hello_world():
    return 'Hello World!'
    
@app.route('/welcome/')
def welcome():
    return 'You are welcome!'

if __name__ == '__main__':
    app.run()
```

将以上代码存入文件起名为`hello_world.py`。然后运行这个文件。

在浏览器中访问`127.0.0.1:5000`，`127.0.0.1:5000/hello`，`127.0.0.1:5000/welcome`，观察执行结果。

示例代码xx-8中：
- URL：`127.0.0.1:5000/hello`绑定了函数`hello_world()`。
- URL：`127.0.0.1:5000/welcome`绑定了函数`welcome()`。

因为返回的字符串是返回到网页中，所以可以直接用`html`标记。另外还可以通过在路由中设置特殊变量参数，从URL中取得变量值。

将以下示例代码xx-9存入文件起名为`hello_world.py`。

```python
#encoding: utf-8
#示例代码xx-9

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'common string<h1>string between html tag</h1>'
    
@app.route('/user/<username>')
def say_hello_to(username):
    return 'Hello,{}!'.format(username)

@app.route('/post/<int:post_code>')
def show_postcode(post_code):
    return '邮编是：{}。'.format(post_code)


if __name__ == '__main__':
    app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000/user/liupengyuan`，`127.0.0.1:5000/post/100083`，`127.0.0.1:5000`，观察执行结果。

示例代码xx-9中：
- `@app.route('/user/<username>')`，其中由`<>`包含的`username`是变量名称，其值由URL中相应部分字符串得到。
- `@app.route('/post/<int:post_code>')`，其中`<int:post_code>`表示，将要接受一个`int`型变量`post_code`，其值由URL中相应部分字符串得到。
- `<h1>string between html tag</h1>`，其中`<h1>......</h1>`是`ntml`语言的标记，期间的字符将作为一级标题显示，可将其视为最简单的带标记`html`页面。

由于一个`html`文件就可以视为一个字符串，故可将每个函数的返回做成比较复杂的包含`html`语法的字符串返回到浏览器上，来进行显示网页，但更习惯的作法是先预先写好一个`html`文件来返回。

同时，我们希望能将返回响应部分与路由处理事务的逻辑分开，各个部分专注于自己的部分，这样的程序设计更清晰，耦合度更低。

最后，还希望在返回响应中，能将数据等根据需要‘嵌入’到预先写好的`html`文件中。
以上这些的实现，就需要借助Flask中的模板（Templates）。


（以后放图说明）

**2.4 模板**

模板是一个包含响应的文本文件（很多时候就是一个`html`文件），包含用变量表示的动态部分（对应未来预期的数据）。使用数据来替换变量,再返回最终得到的响应文件（很多时候就是嵌入数据的`html`文件），这一过程称为渲染。Flask直接利用强大的模板引擎Jinja2。


首先在`my_app`目录下建立目录`templates`，进入该目录，该目录即为默认的模板文件目录。

在`templates`目录下，建立文件`hello.html`及`show.html`，这两个文件将作为模板文件。

`hello.html`文件内容：

```html
<!--hello.html-->
<html>
<body>
<h1>Hello world!</h1>
</body>
</html>
```

`show.html`文件内容：

```html
<!--show.html-->
<html>
<body>
<h1>Hello {{name}}!</h1>
</body>
</html>
```

转到`my_app`目录，将以下示例代码xx-10存入文件起名为`hello_world.py`。

```python
#encoding: utf-8
#示例代码xx-10

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, world!'

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/user/<username>')
def user(username):
    in_str = '姓名：' + username
    return render_template('show.html', name=in_str)

if __name__ == '__main__':
    app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000`，`127.0.0.1:5000/hello`，`127.0.0.1:5000/user/liupengyuan`，观察执行结果。

示例xx-10中：

- `from flask import Flask, render_template`，从`flask`中引入`Flask`及`render_template`函数。
- `return render_template('hello.html')`，返回渲染模板函数的值，其实也就是`hello.html`页面。
- `return render_template('show.html', name=in_str)`，用`show.html`以及一个参数用于`render_template`模板函数，在这个渲染过程中，`show.html`中的`{{name}}`中位于双大括号的`name`是变量，其值由同名变量`name`指向的`in_str`的值替换。

**xx.3 Flask+Echarts结合**

现在D:\my_app下已经有好几种文件，我们将目录整理下。
- 建立`static`目录，将`echarts.min.js`移入该目录，以后将存放各种`js`库。
- 建立`data`目录，该目录暂时为空，以后将存放数据。
- `templates`目录，该目录存放`html`文件，作为渲染模板。
- `\`目录，即`D:\my_app`目录，存放`.py`文件。


**1. 基本结合**

将示例代码xx-6中的`<script src="echarts.min.js"></script>`改为：` <script src="../static/echarts.min.js"></script>`（其中`..`表示当前目录的上一层目录），然后保存成的`index.html`移入`templates`目录中。

转入`D:\my_app`目录，将以下示例代码xx-11存入文件，文件名为：`first_fe.py`。
```python
#coding: utf-8
#示例代码xx-11

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000`，观察执行结果。

我们已经可以利用Flask进行Echarts的可视化展示了，但是别人还是看不到，好，将示例代码xx-11中的`app.run()`改为：`app.run(host = '0.0.0.0')`，然后重新运行`first_fe.py`。

假设你的机器ip是公网固定ip为`xxx.xxx.xxx.xxx`，则此时别人就可以通过浏览器访问`xxx.xxx.xxx.xxx:5000`看到示例代码xx-6给出的可视化展示了。

否则，如果是局域网ip，假设你机器的ip为`196.168.1.5`，则同一个局域网的机器上，用浏览器来访问`196.168.1.5:5000`，也可以看到同样效果。

**2. 动态加载数据**

假设示例代码xx-11所要可视化的数据市场更新，更新的数据是自动统计生成的，格式为互联网使用最广泛的`JSON`数据交换格式，我们要对新的数据进行可视化。

但如果每次更新数据，可视化的展示都要去手动编写`html`文档，这就太枯燥，太不自动化了。  

我们不希望每次更新都要修改代码，希望程序能够根据数据自动形成`html`文档。

由于能够先确定图表布置（含图表类型），因此只需要使`JSON`格式的数据能够被`echarts`动态加载显示即可。

在`data`目录下，建立一个数据文件，文件名为：`bar_data.json`，内容如下：

```python
{"school":["北语","北大","清华","北航","北邮","北外"],
"area":[100, 500, 1000, 400, 400, 250]}`
```

在`templates`目录内，将示例代码xx-6略加修改依旧保存为`index.html`，内容如下：

```html
<!--示例代码xx-12-->
<html>
<head>
    <!-- 引入 ECharts 文件 -->
     <script src="../static/echarts.min.js"></script>
</head>
<body>
    <!--准备一块画布-->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 初始化这块画布
        var myChart = echarts.init(document.getElementById('main'));

        // 显示准备好的图表布置
		myChart.setOption({
			title: {
				text: '完整示例'
			},
			tooltip: {},
			legend: {
				data:['area']
			},
			xAxis: {
				data: {{school|tojson}}
			},
			yAxis: {},
			series: [{
				name: 'area',
				type: 'bar',
				data: {{area|tojson}}
			}]
		});
		
		
    </script>
</body>
</html>
```

示例代码xx-12中：
- `data: {{school|tojson}}`中，`school`是一个变量，其值预期将由在后续利用`render_template`渲染过程传入。`|tojson`是`flask`的标准过滤器，可以把对象转换为 JSON 格式。
- `data: {{area|tojson}}`的情况与上类似。
 
在`D:\my_app`目录下，建立一个python文件，命名为`second_re.py`，内容如下：

```python
#coding: utf-8
#示例代码xx-13

from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def root():
    with open(os.path.join(os.getcwd(), 'data', 'bar_data.json'), encoding='utf-8') as json_file:
	    data = json.load(json_file)
    school_data = data['school']
    area_data = data['area']
    
    return render_template('index.html', school = school_data, area = area_data)

if __name__ == '__main__':
    app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000`，观察执行结果。

示例代码xx-13中：
- ` school_data = data['school']`与`area_data = data['area']`将获取到的数据分别保存到两个变量。
- `return render_template('index.html', school = school_data, area = area_data)`将两个变量的数据内容传入到示例代码xx-12中的`{{school|tojson}}`及`{{area|tojson}}`对应变量中。
 
**3. 用户交互可视化**

这次我们想要在web页面中，根据用户的输入，能够有所反应，显示相应可视化效果。这就需要程序能够接受到用户输入的信息，根据该信息，路由到对应的可视化页面，同时利用对应的数据或者计算生成数据对web页面进行渲染。

**3.1 第一次用户交互**

在`templates`目录下，建立`index.html`文件，内容如下：

```html
<!--示例代码xx-14-->
<html>
	<head>
		<title>交互示例</title>
		<meta charset="UTF-8">
	</head>
	<!--文本框及提交按钮-->
	<form name="input" action="http://www.baidu.com" method="POST">
		Username: <input type="text" name="user"> <input type="submit" value="提交">
	</form>
</html>
```

双击该文件，在文本框中输入字符串，点击`提交`按钮，观察结果。

示例代码xx-14中：
- `<form>`与`</form>`是一对表单标签，其`name`属性的值为`input`，`action`属性的值为`http://www.baidu.com`，`method`属性的值为`POST`。这个表单的名字为`input`，表单完成（执行/提交）后要执行的动作是`http://www.baidu.com`，这个动作是执行同名路由绑定的函数，表单提交数据的方法是`POST`，表单数据会被发送到到`action`动作中规定的页面（函数）中。对本例，由于向百度首页发送一个字符串并不会直接被其接受，因此百度会给出一个错误页面信息。
- `<input type="text" name="user">`中，`<input>`标签规定了用户可以在其中输入的字段，字段`type`属性值为`text`（即文本），`name`属性值为`user`，后续可以根据`user`这个值来获取输入的文本。
- `<input type="submit" value="提交">`中，字段`type`属性值为`submit`（即提交动作），`value`属性值为`提交`，该值将显示在按钮上。

在`D:\my_app`目录下，新建文件，命名为`first_interact.py`，内容如下：

```python
#coding: utf-8
#示例代码xx-15

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_get.html')

@app.route('/result', methods = ['POST'])
def show():
    data = request.form['user']
    return data

if __name__ == "__main__":
	app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000`，观察执行结果。

示例代码xx-15中：
- `@app.route('/result', methods = ['POST'])`中，`/result`绑定了函数`show()`，但是必须加上额外的参数`methods`，且其值与示例代码xx-14中`<form name="input" action="/result" method="POST">`中`method`的值对应一致，才能在` <input type="submit" value="提交">`中点击提交后执行`show()`函数。
- `request.form['user']`中，`request`对象在程序前部`import`，对于 Web 应用，与客户端发送给服务器的数据交互至关重要。在Flask中由request对象来提供这些信息。其`form`属性将返回一个从POST（和PUT）请求得到的词典（dict）。本例中返回词典的键为`user`，则`request.form['user']`的值即为`user`对应的用户在文本框中输入的文本。

**3.2 用户交互可视化实例**

假设有历时十年的词频统计结果，我们想根据用户输入的词汇，给出该词汇在十年间的折线图。这需要将以上知识整合起来。

数据文件依旧是JSON格式文件在`data`目录下，文件名为line_data.json，内容如下：

```python
{
    "年":[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017], 
    "中国":[100, 500, 1000, 400, 400, 250,2000,400,500,340],
    "人民":[1300, 500, 300, 200, 500, 500,1200,200,300,430],
    "德国":[1200, 500, 100, 400, 40, 250,1000,400,50,30],
    "美国":[100, 300, 300, 400, 400, 250,500,400,200,40]
}
```

在`templates`目录下，建立`index.html`文件，内容如下：

```html
<!--示例代码xx-16-->
<html>
	<head>
		<title>交互示例</title>
		<meta charset="UTF-8">
		 <!-- 引入 ECharts 文件 -->
        <script src="../static/echarts.min.js"></script>
	</head>
	<!--文本框及提交按钮-->
	<form name="input" action="/" method="POST">
		输入词汇: <input type="text" name="word"> <input type="submit" value="提交">
	</form>
	
	<body>
    <!--准备一块画布-->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 初始化这块画布
        var myChart = echarts.init(document.getElementById('main'));

        // 显示准备好的图表布置
		myChart.setOption({
			title: {
				text: '词频历时折线图'
			},
			tooltip: {},
			legend: {
				data:[]
			},
			xAxis: {
				data:[]
			},
			yAxis: {},
			series: [{
				name: [],
				type: 'line',
				data: []
			}],
		});
		
    </script>
</body>
</html>
```

在`templates`目录下，建立`show.html`文件，内容如下：

```html
<!--示例代码xx-17-->
<html>
	<head>
		<title>词频历时曲线</title>
		<meta charset="UTF-8">
		 <!-- 引入 ECharts 文件 -->
        <script src="../static/echarts.min.js"></script>
	</head>
	<!--文本框及提交按钮-->
	<form name="input" action="/" method="POST">
		输入词汇: <input type="text" name="word"> <input type="submit" value="提交">
	</form>
	
	<body>
    <!--准备一块画布-->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 初始化这块画布
        var myChart = echarts.init(document.getElementById('main'));

        // 显示准备好的图表布置
		myChart.setOption({
			title: {
				text: '词频历时折线图'
			},
			tooltip: {},
			legend: {
				data:[{{word|tojson}}]
			},
			xAxis: {
				data: {{year|tojson}}
			},
			yAxis: {},
			series: [{
				name: {{word|tojson}},
				type: 'line',
				data: {{freq|tojson}}
			}],
		});
		
    </script>
</body>
</html>
```

在`D:\my_app`目录下，新建文件，命名为`word_freq_vis.py`，内容如下：

```python
#coding: utf-8
#示例代码xx-18

from flask import Flask, render_template, request, url_for
import os, json

app = Flask(__name__)

@app.route('/')
def select_word():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def show():
    selected_word = request.form['word']
    with open(os.path.join(os.getcwd(), 'data', 'line_data.json'), encoding='utf-8') as json_file:
	    data = json.load(json_file)
    year_data = data['年']
    freq_data = data[selected_word]

    return render_template('show.html', word = selected_word, year = year_data, freq = freq_data)

if __name__ == "__main__":
	app.run()
```

运行这个文件。在浏览器中访问`127.0.0.1:5000`，观察执行结果。

恭喜，一个能够与用户进行交互、数据动态加载并进行可视化展示demo已经完成了。

在此基础上，如果想做出更炫酷的可视化展示平台，可以进一步参考学习如下工具或者语言：

- html
- css
- javascript及jquery
- echarts工具包
- flask框架
- bootstrap框架

我们搭建可视化平台后，理想的情况是发现访问用户逐步增加，这时候，仅利用flask自身的web服务可能就满足不了要求了，一般来说，需要一台Web服务器，目前理想的情况，是租用。  

windows下可以完全搭建Web服务器，但考虑到目前更多的Web等服务均搭建在linux平台，因此这里将介绍在linux下搭建Web平台，当然首先需要一台linux系统的本地计算机或一个具有`sudo`权限的远程服务器账号。

**xx.4 linux最基本操作**

**4.1 进入linux系统**

- 如果已有`linux`远程服务器，则用`putty`或`Xshell`等工具登陆一个具有sudo权限的账号，方法可自行百度。
- 如果没有远程服务器，且本地计算机不是`linux`系统，可安装其任意一个流行的发行版本，这里介绍flask在`ubuntu`下的web服务器安装使用，`ubuntu`请读者自行搜索安装，关键字可为"ubuntu U盘安装"。安装时注意记住用户密码，这个密码也就是日后管理员密码，具有`sudo`权限，你懂的。

**4.2 ubuntu等桌面环境**

Linux下的桌面环境与windows桌面类似，自带浏览器，文件管理器等，操作也与windows平台类似。

**4.3 命令行终端**

快捷键`Ctrl+Alt+t`可打开一个**终端**。终端就是一个`linux`系统用户界面，用户在其中与`linux`系统交互，一般也称为**shell**。在实际使用中，可视实际需要同时打开多个终端进行操作。  
在`shell`下是用命令行操作的，`shell`的提示符为`$`。  
本章在介绍`ubuntu`下的一些操作中，如以`$`开头，则表示是在`shell`下操作。注意，`$`只是提示符，操作指令中不要包含`$`。

**4.4 最常用命令**

- `ls` 列出当前目录下的文件
- `cp filename1 filename2` 拷贝`filename1`文件，且命名为`filename2` 
- `cd /var/www` 进入根目录下的`var`目录下的`www`目录

**4.5 vim最简使用命令**

vim是linux下最常用的文本编辑器之一。与windows下word等软件最大的不同是，有**命令模式**与**编辑模式**之分，需要提醒的是，并非只有在编辑模式才能对文件进行修改。
- `vim filename.py` 用`vim`打开（并编辑）`filename.py`文件，如果文件不存在，则自动创建一个空文件。
- `vim`编辑器存在两种模式：命令模式与编辑模式。按`esc`键，可切换至命令模式，输入`i`，可切换至编辑模式。
- 打开文件后，默认为命令模式，键入`:q`后，回车，可直接退出文件。
- 命令行模式下：
    - `:q!`后，回车，可放弃保存，退出编辑
    - `:w`后，回车，可保存文件
    - `:wq`后，回车，可保存文件并退出
    - `yy`可复制当前行
    - `p`可将剪贴板内容粘贴到当前行位置
    - `dd`可删除当前行
    - `:!某命令`，`:!`后跟着某个`shell`下的命令（部分命令），可以在不退出编辑文件的情况下直接执行该命令。比如`:!ls`可查看目录，`:!python filename.py`可以运行`filename.py`这个文件。
- 编辑模式下对内容进行修改可先用与平时windows中类似的方法，但注意不要用windows中常用的`Ctrl+c`等系列操作。

这里仅介绍本章用到的最基本的`linux`使用，进一步的`linux`使用基础，请参阅附录X，或者自行搜索。


**xx.5 Linux下搭建python及相关web服务环境**

**5.1 Anaconda及python开发包的安装**

1. 登陆linux服务器

2. $ `wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-4.3.1-Linux-x86_64.sh`

下载anaconda 3.4版本，这是一个软件镜像站点，国内下载速度较快。如果失败则改用软件原地址下载：  
$ `wget -c https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh`

3. $ `bash Anaconda3-4.3.1-Linux-x86_64.sh`

安装Anaconda，注意文件名要对应自己下载的文件名。

---
**5.2 python多版本环境conda**

完全可以直接在当前Anaconda版本下安装各类软件包，但是，最好需要所安装的库与包的版本与当前Anaconda对应的python版本一致，当版本不一致时，就很可能导致安装失败或者运行出错。  
当然，卸载当前的Anaconda或者python，重新一个与要安装的包/库相同版本的Anaconda或python，然后再安装这个包/库也无不可。但是Anaconda内置的`conda`提供了更好的解决办法，可创建多个Anaconda版本的python环境，并可以根据需要随意切换，互不干扰。

1. $ `conda create -n env34 python=3.4 anaconda`  
创建一个python 3.4版本的anaconda，并将其命名为：env34。具体版本读者可以根据需要创建。

2. $ `source activate env34`  
激活刚才创建的`env34`环境。此时，会发现提示符行最前面有`(env34)`。如果确定要在`python3.4`版本下进行各类软件包的安装以及使用，则可在该环境下进行。

3. (env34)$ `source deactivate env34`
退出env34环境（注意，以后利用`source activate env34`即可再次进入该环境，且保留所有安装包等各项设置）

**5.3搭建gunicorn并提供服务**

- 搭建
1. 登陆linux服务器

2. $ `sudo apt-get update`

这个步骤是为了更新软件包源（地址列表），以便后续可以正确下载各类软件包。
注意在本节的安装设置中多需要`sudo`权限，如需要输入密码，则自行输入。

3. $ `sudo apt-get install python-dev`

linux环境下编译python扩展应用时一般均需要安装`python-dev`包，主要包含编译时需要的头文件。

4. `source activate env34`

5. (env34)$ `sudo apt-get install python-pip`

安装`python-pip`模块，该模块安装以后，可以使用`pip install 软件包`这样的`pip`命令方便安装python各类软件库/包。

6. (env34)$ `pip install gunicorn`

至此，gunicorn安装完毕。

- 提供服务

1. 可在指定目录如在`/var/www/`下，建立`my_app`目录，然后请自行建立类似**3.2**小节中的目录结构、同名文件以及相同的文件内容。

2. 转到my_app目录。

3. (env34)$ `gunicorn -w 4 -b 0.0.0.0:8000 word_freq_vis:app`

启动gunicorn服务，其中：`-w`参数是`worker`数量，为4，`-b`参数是绑定地址及端口，为`0.0.0.0:8000`，最后是程序名称以及函数名称，在本例中分别是`word_freq_div`及`app`。

4. 在服务器浏览器中输入：`127.0.0.1:8000`，观看执行结果。假设服务器ip为`xxx.xxx.xxx.xxx`，也可在同局域网内终端的浏览器访问：`xxx.xxx.xxx.xxx:8000`，观察执行结果。

5. 回到命令行，按`Ctrl+c`，停止gunicorn服务。

6. (env34)$ `source deactivate env34`。

退出env34虚拟环境。

至此，基于`gunicorn`的动态可视化web服务已经搭建。

但如果你的网站不仅仅是提供了动态可视化网页，还有一些静态网页如纯`html`页面等，且访问用户较多，则可安装配置`nginx`来进行静态动态网页分别解析代理以提高网站性能。

**5.4 安装配置nginx**

Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行。由俄罗斯的程序设计师Igor Sysoev所开发，供俄国大型的入口网站及搜索引擎Rambler（俄文：Рамблер）使用。其特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。(引自百度百科)

1. 登陆linux服务器

2. $ `sudo apt-get update`

3. $ `sudo apt-get install python-dev`

4. $ `source activate env34`

5. (env34)$ `sudo apt-get install nginx`

安装nginx包。

6. (env34)$ `sudo service nginx start`

启动`nginx`服务。

7. 打开浏览器并输入`127.0.0.1`(如果是登陆服务器进行开发，则需要打开浏览器，输入服务器的ip地址) 

浏览器将会显示nginx的欢迎页面，至此，已经成功的运行了nginx的web服务。




**5.4 flask+nginx+gunicorn联合进行web服务示例**


1. 登陆linux服务器

2. $ `source activate env34`

3. 在指定目录如在`/var/www/`下，建立`my_app`目录，然后请自行建立类似**3.2**小节中的目录结构、同名文件以及相同的文件内容（如已经建立，则忽略）。在`my_app`目录下建立文件test_static.html。内容为：

```html
<html>
<body> Test for nginx. This is a test page for static web page.</body>
</html>
```

4. 转到my_app目录。

5. (env34)$ `gunicorn -w 4 -b 0.0.0.0:8000 word_freq_vis:app`

启动`word_freq_vis程序`对应的函数`app`的gunicorn服务。

6.  (env34)$ `sudo cp /etc/nginx/sites-available/default   /etc/nginx/sites-available/default.bak`

备份nginx的默认配置文件`default`，必要时可以恢复最原始的缺省配置。

7.  (env34)$ `sudo vim /etc/nginx/sites-available/default`

利用`vim`文本文件编辑器修改nginx的默认配置文件`default`。对本例使用ip进行访问的情况，可简单配置如下：

```python
server{
        listen 80;

        root /var/www/my_app;
        index index.html;
        location / {
                try_files $uri $uri/ = 404;
                proxy_pass http://127.0.0.1:8000;   # 须与gunicorn的端口设定对应一致。
       }

```
其中：
- `listen 80;`，将监听端口设为：`80`，也就是一般web浏览默认端口。
- `root /var/www/my_app;`，将URL访问的根目录设定为：`/var/www/my_app`。
- `index index.html;`，将访问的默认页面设为：`index.html`。
- ` try_files $uri $uri/ = 404;`，表示如果找不到页面则返回404错误页面。
- `proxy_pass http://127.0.0.1:8000;`，设定动态页面访问的服务器地址以及端口，这里面设为当前服务器地址，端口号与`gunicorn`服务的端口一致。

8.  (env34)$ `sudo service nginx restart`

重启`nginx`服务。如果没有错误提示信息，则表示服务已经成功重启，否则说明上述`default`文件输入有误，需要重新修改并再次重启。

9. 假设租用的远程web服务器ip地址为：`xxx.xxx.xxx.xxx`：
- 可在本地浏览器输入`xxx.xxx.xxx.xxx/test_static.html`并回车，因为是静态页面，所以直接被`nginx`解析访问。
- 在本地浏览器输入`xxx.xxx.xxx.xxx`并回车，则动态可视化页面将被加载执行，这是通过nginx代理到gunicorn提供的web服务。

至此，一个简单的flask+nginx+gunicorn联合进行web服务示例已经完成。

这样的web服务，对访问量日均ip在1000左右的可视化网站，已经足够，对其进一步提高性能与优化，则留待读者慢慢探索。
