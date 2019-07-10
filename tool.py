import pandas as pd
myfile = pd.read_csv(‘myfile.txt’)
#里面有些参数，如header是设置表头，index是是否有索引，sep是分割符号等
#加载进来的myfile是一个pandas的Dataframe格式的数据。

# 保存文件
header=True表示保存表头
myfile.to_csv(‘myfile.txt’, header=True)

#若原始数据没有列名（表头），加载的数据添加列名即可。
import pandas as pd
myfile = pd.read_csv(‘myfile.txt’,header=None)
myfile.columns = [‘id’,’name’,’sex’]

#Datframe修改列名
myfile.rename(columns={‘id’:’change_id’},inplace=True)

#Datafrme删除一整列
#方法一：
Del myfile[‘sex’]
#方法二：
DF= DF.drop('column_name', 1)；
DF.drop('column_name',axis=1, inplace=True)
DF.drop([DF.columns[[0,1, 3]]], axis=1,inplace=True)   # Note: zero indexed

#Dataframe截取一部分数据
Newfile = myfile[myfile.id>’100’]

#Dataframe填充Nan空值
Myfile.fiina(0) #表示用0填充Nan

# 其他功能
df.head() #显示前五行
df.tail()#显示后五行
# 统计函数：
df.count() #非空元素计算 ，即计数
df.min() #最小值
df.max() #最大值
df.idxmin() #最小值的位置，类似于R中的which.min函数
df.idxmax() #最大值的位置，类似于R中的which.max函数
df.quantile(0.1) #10%分位数
df.sum() #求和
df.mean() #均值
df.median() #中位数
df.mode() #众数
df.var() #方差
df.std() #标准差
df.mad() #平均绝对偏差
df.skew() #偏度
df.kurt() #峰度
df.describe() #一次性输出多个描述性统计指标 ```

# Apply、map函数

为了对每一行进行处理，可以直接用apply或者map
例如df中有列名time，形如2017-02-03，我们计算每行数据属于星期几

from datetime import date
df['weekday']=df.time.apply(lambda x:date(int(x.split('-')[0]),int(x.split('-')[1]),int(x.split('-')[2])).weekday()+1)
#这样df中增加了一列weekday。
#Split()函数是用于分割字符串的，上面的x.split(‘-’)[0]表示将x根据‘-’分割，取出分割后的第一份数据。


# 有时候对每行数据要进行复杂的操作，可能用简单的一行写不下，那么可以单独写一个函数，来处理，再将函数传给apply函数即可，如：
def computeweek(x)
    Do it
    Return num

#定义函数
df['weekday']=df.time.apply(computeweek)
#这里可以不用传参数x，apply函数可以自动传入参数。


同样，map函数也对每一行进行处理，如
df[‘year’]=df.time.map(x:x.split('-')[0])
#表示将time列只保留年份
1
2
apply和map的作用很强大，可以简化很多步骤，之前很多实现代码都是用numpy写的，各种for循环，直接写哭，用了apply和map后真的感觉是：life is short， use python!
11、get_dummies()函数实现onehot编码
这个函数是用来将列中的值转化为列名，简单点说就是可以做onehot编码。

week =pd.get_dummies(train_x['weekday']).add_prefix('weekday_')
#这样就将上面weekday中1~7的值变成了7列，列名分别为weekday_1~weekday_7
1
2
12、groupby（）函数
和SQL中的一样，用来对数据进行分组，其实可以发现，pandas很多操作模仿了SQL来对数据进行处理，熟悉数据库的可以很容易上手。

df = df.groupby(['id','name'])[‘score’].mean()
#这句表示将t按照列id和name进行分组，将分组后的每个组根据score求每个#组score的平均值。
1
2
13、drop_duplicates()函数去重

#用于去除重复的行
Df.drop_duplicates(inplace=True)
1
2
14、修改列的数据类型

 df[‘score’]=df[‘score’].astype(‘str’)
 #表示将原来的数据类型改成了字符串类型
1
2
15、unstack()函数 转换行值为列名
经过对两列groupby后，会产生两个索引，
groupby([‘id’,’name’]),或者自己加的多重索引。
在Dataframe中存在多重索引，如果只是要重新定义索引，可以直接用reset_index()或者将某列定义为setindex(‘id’)
使用unstack函数可以直接将索引变成列

index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),...                                    ('two', 'a'), ('two', 'b')])
s = pd.Series(np.arange(1.0, 5.0), index=index)
#得到：
one  a   1.0
     b   2.0
two  a   3.0
     b   4.0
dtype: float64
1
2
3
4
5
6
7
8
s.unstack(level=-1)
     a   b
one  1.0  2.0
two  3.0  4.0
s.unstack(level=0)
   one  two
a  1.0   3.0
b  2.0   4.0
1
2
3
4
5
6
7
8
16、Dataframe把索引变成一列

df['newcol']=df.index.values
1
我在pandas中最常用的就是使用groupby分组，分组后直接使用统计方法求均值啊什么的，所以一定要学会将以上方法组合使用，基本可以解决大部分数据处理的功能。而且代码写出来简洁美观。
注意：
还有一定要注意，groupby后的索引index是不变的，为了方便后续的处理，以及防止出错，最后对处理后的数据表进行reset_index()，或者setindex来指定一列作为索引，新手建议不要使用多重索引，怕弄乱了。
mege和concat一定要注意合并的是行还是列。
添加新的列的时候可以新建一个Dataframe，来生成新的列，最后将两个列用merge或者concat组合起来。
综上所述：pandas用好了，根本不需要什么for循环。
后续我会继续练习pandas，把新学的东西继续加进来。。。

未完。。。待续。。。。
---------------------
作者：DivinerShi
来源：CSDN
原文：https://blog.csdn.net/sxf1061926959/article/details/56280759
版权声明：本文为博主原创文章，转载请附上博文链接！