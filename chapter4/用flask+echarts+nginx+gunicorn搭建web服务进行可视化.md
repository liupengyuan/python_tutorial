任务：搭建可视化网站：xxx.xxxx.xxx

xx.1 Echarts入门
1. Echarts介绍  
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

2. 迅速上手使用
- 建立工作目录  
windows下，在```D:```下建立目录```my_app```，其他环境请类似相应建立目录。
- 下载echarts至工作目录  
浏览器中，打开：http://echarts.baidu.com/download.html
这里先下载完整版```http://echarts.baidu.com/dist/echarts.min.js```，下载到工作目录```D:\my_app```。以后可以视需要选择版本下载。

- 建立最基本的```html```文件并引入echarts

利用记事本或其他文本编辑器，在工作目录```D:\my_app```下，建立文件```index.html```，注意，将文件扩展名```txt```更改为```html```。文件内容如下：

```html
<!--示例代码xx-1-->

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <!-- 引入 ECharts 文件 -->
    <script src="echarts.min.js"></script>
</head>
<body>
页面内容这里显示（用后续示例中body中的内容替换）
</body>
</html>
```

将这个文件用```utf-8```格式保存。然后双击该文件，浏览器中应该能够显示```页面内容这里显示（用后续示例中body中的内容替换）```。

示例代码xx-1中：
- ```<script src="echarts.min.js"></script>```这行代码引入```echarts```文件，有了它，后面的可视化展示图表才能被调用。
- ```<body>......</body>```，可视化内容将放置在其中，相关```html```语言的基本使用，请自行搜索查阅相关文档。
- ```<!--```为```html```语言的注释开始，中间的字符为注释，最终以``` -->```作为注释结尾。


- 图表布置

我们来看下图表布置，也就是将在```<body>......</body>```中的内容。  
用文本编辑器打开方才的`index.html`文件，将`body`部分用如下示例代码xx-2替换。

```html
<!--示例代码xx-2-->

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

示例代码xx-1中：
- ```<div id="main" style="width: 600px;height:400px;"></div>```：
    - ```<div>......</div>```，这里可暂视为将网页切出一层，在其中将对这层进行风格样式等的定义。
    - ```id="main" ```，将这层起个名字/给个标签为：```name```，后续可以根据这个```id```找到这层。
    - ```style="width: 600px;height:400px;">```，定义了一个宽600，高400的区域（画布，也就是后续图表整体大小）。
- ```<script type="text/javascript">......</script>```，表示之间是脚本代码区域，且是```javascript```脚本代码。
- ```var myChart = echarts.init(document.getElementById('main'))```：
    - ```var myChart```，定义变量```mychart```。
    - ```document.getElementById('main')```，调用```document```文档对象的```getElementById()```方法，参数为`main`。即获取指定id为```main```的对象，也就是上述````div```对象。
    - ```echarts.init(document.getElementById('main'))```，将```div```对象初始化为```echarts```对象。
- `myChart.setOption( {xAxis: {}, yAxis: {}, series: [] , title: {}, tooltip: {}, legend:{} });`
    - 调用`myChart`的`setOption()`方法，参数为一个词典/dict，里面是图表的各项设置与数据。
    - 在集合/set中，多个设置参数用`,`分隔，每个设置都是一个键值对。`xAxis: {}`是对x轴的设置，`yAxis: {}`是对y轴的设置，当前x及y轴对应的值为`{}`，即空；`series: []`是系列数据，值为空；`title: {}`是图表标题，值为空；`tooltip: {}`是浮动提示，值为空；`legend:{}`是图例，值为空。

下面将可视化图表布置中除了系列数据部分以外的相关信息填入，这些信息基本上是在决定采用什么图表类型来展示什么内容后就能够预先确定好的。数据部分可以在这个图表布置下，后续显示。  
用文本编辑器打开方才的`index.html`文件，将` myChart.setOption( {xAxis: {}, yAxis: {}, series: [] , title: {}, tooltip: {}, legend:{} });`这一行代码用如下示例代码xx-3替换。

```javascript
//示例代码xx-3

        // 显示准备好的图表布置
        myChart.setOption({
			xAxis: {
				data: []
			},
			yAxis: {},
			series: [{
				name: '面积',
				type: 'bar',
				data: []
			}]
			title: {
				text: '图表布置示例'
			},
			tooltip: {},
			legend: {
				data:['面积']
			},
		});

```

保存`index.html`后运行，观察其在浏览器中的执行结果。

示例代码xx-3其实就只有一行代码，为了便于阅读分成了多行，这是一种良好的编程风格，其中：
- `series`的值为一个列表，列表内是一个词典dict：
    - `name`的值为字符串，该值一般要与`legend`中`data`列表中的值对应，表示系列数据的名称
    - `type`的值为字符串，表示图表类型，`bar`就是柱状图
    - `data`的值为列表，即柱状图要显示的数据
- `title`的值为一个词典，其中的键为`text`，其值是一个字符串，显示在图表左上方
- `legend`的值为一个词典，其中的键为`data`，其值是一个列表，显示在图表正上方

图表布置好以后，将对最重要的部分---数据进行填充展示。

- 数据填充展示
 
用文本编辑器打开方才的`index.html`文件，在示例代码xx-3下一行添加如下示例代码xx-4。

```javascript
//示例代码xx-4

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

从示例代码xx-4可以看到，只是对`xAxis`的`data`的值，`series`的`data`的值进行了补充。  
在示例代码xx1-3的图表布置下，未来如果我们换一组数据，填充不同的`data`，则可以显示不同的图表。

完整示例如下：

```html
<!--示例代码xx-5-->

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
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
				data:['面积']
			},
			xAxis: {
				data: []
			},
			yAxis: {},
			series: [{
				name: '面积',
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

恭喜，至此我们已经利用echarts完成了一个虽小，但是还算是完整的可视化网页实例，虽然只有一个`html`网页。  
我们知道双击该网页即可显示该网页内容，
但我们更想把这个网页也展示给别人而不仅仅是自己自娱自乐，我们期望未来会有用户以浏览器链接（URL）的方式来远程访问这个网页，然后看到我们想展示的内容。于是，我们需要一台Web服务器，目前理想的情况，是租用。  
windows下可以完全搭建Web服务器，但考虑到目前更多的Web等服务均搭建在linux平台，因此本章将在linux下搭建Web平台，首先需要一台linux系统的本地计算机或一个具有`sudo`权限的远程服务器账号。

xx.2 linux最基本操作

0. 进入linux系统
- 如果已有`linux`远程服务器，则用`putty`或`Xshell`等工具登陆一个具有sudo权限的账号。
- 如果没有远程服务器，且本地计算机不是`linux`系统，可安装其任意一个流行的发行版本，本章使用`ubuntu`，请读者自行搜索安装，关键字可为"ubuntu U盘安装"。安装时注意记住用户密码，这个密码也就是日后管理员密码，具有`sudo`权限，你懂的。

1. ubuntu等桌面环境
Linux下的桌面环境与windows桌面类似，自带浏览器，文件管理器等，操作也与windows平台类似。

2. 命令行终端
快捷键`Ctrl+Alt+t`可打开一个**终端**。终端就是一个`linux`系统用户界面，用户在其中与`linux`系统交互，一般也称为**shell**。在实际使用中，可视实际需要同时打开多个终端进行操作。  
在`shell`下是用命令行操作的，`shell`的提示符为`$`。  
本章在介绍`ubuntu`下的一些操作中，如以`$`开头，则表示是在`shell`下操作。注意，`$`只是提示符，操作指令中不要包含`$`。

3. 最常用命令
- `ls` 列出当前目录下的文件
- `cp filename1 filename2` 拷贝`filename1`文件，且命名为`filename2` 
- `cd /var/www` 进入根目录下的`var`目录下的`www`目录

4. vim最简使用命令
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

xx.3 linux系统下搭建python及web服务器nginx

- Anaconda及python开发包的安装
1. 登陆linux服务器
2. $ ```sudo apt-get update```  
这个步骤是为了更新软件包源（地址列表），以便后续可以正确下载各类软件包。
注意在本节的安装设置中多需要```sudo```权限，如需要输入密码，则自行输入。
3. $ ```wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-4.3.1-Linux-x86_64.sh```  
下载anaconda 3.4版本，这是一个软件镜像站点，国内下载速度较快。如果失败则改用软件原地址下载：  
$ ```wget -c https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh```  
4. $ ```bash Anaconda3-4.3.1-Linux-x86_64.sh```  
安装Anaconda，注意文件名要对应自己下载的文件名。
5. $ ```sudo apt-get install python-dev```   
linux环境下编译python扩展应用时一般均需要安装```python-dev```包，主要包含编译时需要的头文件。

- 安装配置nginx

Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行。由俄罗斯的程序设计师Igor Sysoev所开发，供俄国大型的入口网站及搜索引擎Rambler（俄文：Рамблер）使用。其特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。(引自百度百科)

1. 登陆linux服务器
2. $ ```sudo apt-get install nginx```   
安装nginx包。
3.  $ ```sudo service nginx start```  
启动```nginx```服务。
4. 打开浏览器并输入```127.0.0.1```  
浏览器将会显示nginx的欢迎页面，至此，已经成功的运行了nginx的web服务。
5. $ ```sudo cp /etc/nginx/sites-available/default   /etc/nginx/sites-available/default.bak```  
备份nginx的默认配置文件```default```，必要时可以恢复最原始的缺省配置。
6. $ ```sudo vim /etc/nginx/sites-available/default```  
利用```vim```文本文件编辑器修改nginx的默认配置文件```default```。可简单配置如下：


7. $ ```sudo service nginx restart```  
重启```nginx```服务。如果没有错误提示信息，则表示服务已经成功重启，否则说明上述```default```文件输入有误，需要重新修改并再次重启。


xx.3 实现可远程访问的可视化web应用

1. 登陆linux服务器。
2. $ ```sudo service nginx start```  
如未启动`nginx则`启动```nginx```服务。
3. $ `cd /var/www`
转到 `/var/www`目录。
4. $ `mkdir myapp`
在当前目录(`/var/www`)下，建立工作目录，名为`myapp`。
5. $ `cd myapp`
进入`myapp`工作目录
6. $ `vim index.html`
建立并编辑`index.html`文件，内容为中将本章第一节中的示例代码5。或直接示例代码5的`index.html`文件拷贝到这个目录下。
7. 打开浏览器并输入```127.0.0.1```  
浏览器将会显示预期中的可视化图表。

xx.4 (异步)数据加载与更新

但如果每次一个可视化的展示都要去手动编写`html`文档，这就太枯燥，太不自动化了。  
可以先确定图表布置（含图表类型），然后预先将数据计算/准备好，一般存成`JSON`格式的数据文件中，读入该数据文件，一般可利用非常流行的`javascript`框架`jQuery`中的方法来读取，填入数据显示即可。  
我们利用现成的数据，即`xAxis`及`series`的`data`，保存到一个JSON文件，然后读取并可视化展示。

- `jQuery`准备
1. 下载`jQuery`最新版本。
2. 拷贝其一个副本到`/var/www/myapp`目录下，重新命名文件为：`jquery.js`。
- 编辑并保存`JSON`文件
1. 文件名为：`data.json`。
2. 文件内容如下：
```python
{
	"categories": ["北语","北大","清华","北航","北邮","北外"], 
	"data": [100, 500, 1000, 400, 400, 250]
}
```
- 修改`index.html`文件为如下：

```html
<!--示例代码xx-6-->

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <!-- 引入 ECharts 文件 -->
    <script src="echarts.min.js"></script>
    <script src="jquery.js"></script>           <!-- 引入 jQuery 文件 -->
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
				text: '异步加载JSON示例'
			},
			tooltip: {},
			legend: {
				data:['面积']
			},
			xAxis: {
				data: []
			},
			yAxis: {},
			series: [{
				name: '面积',
				type: 'bar',
				data: []
			}]
		});
		
		// 异步加载数据
		$.get('data.json').done(function (my_data) {
			// 填入数据
			myChart.setOption({
				xAxis: {
					data: my_data.categories
				},
				series: [{
					// 根据名字对应到相应的系列
					name: '面积',
					data: my_data.data
				}]
			});
		});
    </script>
</body>
</html>
```

示例代码xx-6中：
- `<script src="jquery.js"></script>`，是引入`jquery`文件，其中有读取`JSON`数据文件函数。
- `$.get('data.json').done(function (my_data) {......})`，其中``$.get('data.json')`是调用`jquery`中的`get`函数，读取文件`data.json`。`。done()`是当`get()`函数成功读取时，执行`function()`方法。
- `function()`方法中有一个参数`mydata`，是一个`json`对象，内容即为被成功读取的文件`data.json`内容。
- `function()`方法内部是我们熟悉的`myChart.setOption()`，这个方法与前面类似，只是将`data`部分换成文件中的相应部分替代。`my_data.categories`的值即为`data.json`中`categories`键的值，`my_data.data`的值即为`data.json`中`data`键的值。

让我们再次打开浏览器并输入`127.0.0.1`，浏览器将会显示预期中的可视化图表。
