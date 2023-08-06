text1 = """
## 绘制函数的数据输入类型

所有绘图函数都需要np.array或np.ma.masked_array对象作为输入类型 。 如果是 “类数组（array-like）” 对象（如pandas数据对象和np.matrix）可能会或可能不会按预期工作。最好在绘图之前将它们转换为np.array对象。

例如，要转换pandas.DataFrame

```python
a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values
```

以及转换np.matrix
```python
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)
```

## 常见的图表绘制

进行图表绘制时，我们通常使用pyplot对象，具体教程，请参照Pyplot教程。官方文档写的挺不错，深入浅出，建议要入门的铁子们看看。

### 折线图
绘制单个函数的代码如下所示

```python
import matplotlib.pyplot as plt 
import numpy as np
t = np.arange(0., 5., 0.2)
'''
    arange的作用类似于内置函数range，用于生成
    在范围内的一组数据。此处，生成的是在[0,5)之间的，
    相邻数差是0.2的数据。
     
'''
plt.plot(t, t ** 2, 'r--')
'''
    plot用于绘图， t表示横坐标， t ** 2表示t的二次方，
    表示纵坐标。r--则表示线是红色(red)，以'--'形式表现
'''
plt.show()
```
![avatar](https://imimg.mydw.xyz/2019/10/18/8bd0f675a73370f0.png)

如果要绘制包含多个函数的折线图，只要多调用几次plot()函数，或者在同一个plot()函数中填入多个函数即可。

```python
import numpy as np
 
t = np.arange(0., 5., 0.2)
 
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
'''
   bs表示blue square, 蓝色正方形
   g^表示green 三角形。
'''
plt.show()
```
![avatar](https://imimg.mydw.xyz/2019/10/18/6613b905afbbcf5f.png)
### 柱状图

对于柱状图，我们可以调用plt.bar()。代码示例如下：
```python
names = ['group_a', 'group_b', 'group_c']
values = np.arange(25,100, 25)
plt.bar(names, values)
plt.show()
```

效果如下

![avatar](https://imimg.mydw.xyz/2019/10/18/2956dc17d1fd60f7.png)

现在为止，我们画的都是只有一张图的画板，那有没有那种可以在画板figure上画多个图的实例呢？当然是有的，趁此机会，我们可以学习一下新的功能。

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
 
plt.figure(1, figsize=(9, 3))
# 设置画板大小，总大小为9，分为3块
plt.subplot(1, 3, 1)
'''
    subplot表示的是一张子图，(1, 3)表示的是整张大图的大小为1 x 3，
    大图里面的每个小图，都有自己的索引，索引从左上角向右依次到
    右下角，逐渐增大，这里的子图索引为1。
'''
plt.bar(names, values) # 绘制柱状图
plt.subplot(132)
'''
    当三个参数都小于10的时候，可以将逗号省略。
'''
plt.scatter(names, values) # 绘制散点图
plt.subplot(133)
plt.plot(names, values) # 绘制折线图
plt.suptitle('Categorical Plotting') # 设置父图的标题
plt.show()
```

效果如下

![avator](https://imimg.mydw.xyz/2019/10/18/d000be27a8e8ba8c.png)

### 散点图

绘制散点图时，需要给定两个np.array，在绘图时，plot会将两个array压缩成一对对的坐标，用于在图像中表示，示例代码如下

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# ro 表示红色(red), 以圆圈(o)形式展示
plt.axis([0, 6, 0, 20])
# 规定横坐标和纵坐标的上下限， x ∈ (0, 6), y ∈ (0, 20) 
plt.show()
```
效果如下

![avator](https://imimg.mydw.xyz/2019/10/18/dbafb609cd400ed2.png)

### 饼状图

最后一个饼图， 除了基本饼图外 ，下列案例中，添加了几个可选项：
- 切片标签
- 自动标记百分比 autopct
- 用explode偏移切片
- 投影 shadow
- 自定义初始角度

请注意，自定义起点角度：

默认的起始角度 startangle 为0 ， 这将在正x轴上开始“Frogs”切片。 此示例将 startangle设置为90 ， 以便将所有对象逆时针旋转90度，并且切片从正y轴开始。

示例代码如下：

```python
import matplotlib.pyplot as plt
 
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
# 分离第二块切片
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True)
ax1.axis('equal')  
# 相等的长宽比可确保将饼图绘制为圆形。
plt.show()
```
效果如下：

![avator](https://imimg.mydw.xyz/2019/10/18/df65cedbbc69a26f.png)

## 关于图形的属性和格式

解决图形中文乱码的问题

```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
```

## 设置x轴和y轴的标签

```python
plt.xlabel('name')
plt.ylabel('name')
```

## 给图形添加数据标签

```python
plt.text(x, y, value, ha = "center", va = "bottom", fontsize = 8) 
# x,y表示在坐标(x,y)处添加文字
# ha='center', va= 'bottom'代表horizontalalignment（水平对齐）、verticalalignment（垂直对齐）的方式，fontsize则是文字大小
```

## 显示图例

```python
plt.legend(["","",""])
# 传入n个参数，对应不同的n个图线
```

## 设置数轴的值或改变其偏移量

```python
plt.xticks(rotation=90) # 设置x轴的偏移量
plt.yticks(rotation=90) # 设置y轴的偏移量
```

rotation表示从水平方向开始，顺时针的旋转量

这一类函数还可以用于替换数轴的各个值，官方的示例如下：

```python
xticks( arange(5), ('Tom', 'Dick', 'Harry', 'Sally','Sue'))
# 用['Tom', 'Dick', 'Harry', 'Sally','Sue']替换x数轴上的[0,1,2,3,4]
```

## 设置画板大小

```python
plt.figure(num, figsize= (x,y))
# num表示画板数， figsize表示画板大小为x * y, x为水平长度。
```
"""


text2 = """
import pandas as pd
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 读文件
    df = pd.read_csv("./如意集团2018年6月公司股价变动日收盘价.csv")
    # 设置画板大小
    plt.figure(1, figsize=(9, 6))

    # 获得数据
    date2017 = df['date'].astype(np.str)
    high = df['high']
    close = df['close']
    start = df['open']

    # 设置坐标标签
    plt.xlabel("时间日期")
    plt.ylabel("价格指数")

    # 图1
    plt.plot(date2017, start)

    # 图2
    plt.plot(date2017, close, 'r--')

    # 图3
    plt.plot(date2017, high, 'g--')

    # 图例
    plt.legend(["开盘价", "收盘价", "最高价"])

    # 翻转x轴
    plt.xticks(date2017, date2017, rotation=90)

    plt.savefig("b.png")
    plt.show()

"""

# mt绘图1
text3 = """
import tushare as ts

import matplotlib as mp

import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters

mp.rcParams['font.sans-serif'] = ['SimHei']

mp.rcParams['axes.unicode_minus'] = False
# 抓取数据

ds = ts.get_k_data('000031', start='2019-01-01',
                   end='2019-05-31​', ktype='M', autype='qfq')

ds = ds[['date', 'close']]

ds.to_excel('D:/bigdata/大悦城自2019年1月至2019年5月的前复权月末收盘价.xlsx')

print(ds)


# 为了防止出现中文乱码，在这里进行一下设置

font = mp.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')


# 生成图片

x_date = ds['date']

y_col1 = ds['close']

x2 = range(len(x_date))

width = 0.40

plt.figure(figsize=(10, 8))

plt.bar(x=x2, height=y_col1, width=width,color="r", label="closing data")

# 给图表加上图例

plt.legend()

plt.xticks([index for index in x2], x_date, rotation=40)

plt.xlabel("日期")

plt.ylabel("指数")

plt.style.use('ggplot')

plt.grid(True)

plt.title('大悦城自2019年1月至2019年5月的前复权月末收盘价', fontsize=12)

plt.savefig('D:/bigdata/大悦城自2019年1月至2019年5月的前复权月末收盘价柱状图​.png')

plt.show()

"""

# 绘图2
text4 = """
import tushare as ts

import matplotlib as mp

import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# 抓取数据

ds = ts.get_k_data('000031', start='2019-01-01',
                   end='2019-05-31​', ktype='M', autype='qfq')

ds = ds[['date', 'high', 'low']]

ds.to_excel('D:/bigdata/美利云自2018年08月31日至2018年12月31日前复权周最高价最低价.xlsx')

print(ds)


# 为了防止出现中文乱码，在这里进行一下设置

font = mp.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')


x_cel = ds['date']

y_col1 = ds['high']

y_col2 = ds['low']

plt.figure(figsize=(11, 8))

plt.plot_date(x_cel, y_col1, '-', label='high price')

plt.plot_date(x_cel, y_col2, '-', label='low price')

plt.xlabel('日期', fontproperties=font)

plt.ylabel('指数', fontproperties=font)

# 给图表加上图例

plt.legend()

# X轴文字倾斜

plt.xticks(rotation=45)

plt.style.use('ggplot')

plt.grid(True)

plt.title('美利云自2018年08月至2018年12月前复权周最高价最低价对比图',
          fontproperties=font, fontsize=10)

plt.savefig('D:/bigdata/美利云自2018年08月至2018年12月前复权周最高价最低价折线图.png')

plt.show()
"""

# 绘图5 折线图
text5 = """
import tushare as ts

import matplotlib as mp

import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()



# 抓取数据

ds = ts.get_k_data('002239', start='2018-08-31', end='2018-12-31', ktype='W', autype='qfq')

ds.to_csv('D:/bigdata/奥特佳集团2018年8月31日至2018年12月31日股价变动的周收盘价.csv')



# 清洗数据

df = ds[['date', 'low']]

df.to_csv('D:/bigdata/奥特佳集团2018年8月31日至2018年12月31日股价变动的周最低价（已清洗）.csv')

print(df)



# 为了防止出现中文乱码，在这里进行一下设置

font = mp.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc')



x_cel = ds['date']

y_col1 = ds['high']

y_col2 = ds['open']

y_col3 = ds['close']

plt.figure(figsize=(10, 7))

plt.plot_date(x_cel, y_col1, '-', label='peak price')

plt.plot_date(x_cel, y_col2, '-', label='open price')

plt.plot_date(x_cel, y_col3, '-', label='closing price')

plt.xlabel('日期', fontproperties=font)

plt.ylabel('指数', fontproperties=font)

plt.legend()

plt.xticks(rotation=45)

plt.style.use('ggplot')

plt.grid(True)

plt.title('奥特佳集团2018年8月至12月周开盘价收盘价最高价折线图', fontproperties=font, fontsize=10)

plt.savefig('D:/bigdata/奥特佳集团开盘价收盘价最高价折线图.png')

plt.show()
"""