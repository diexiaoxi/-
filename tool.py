import pandas as pd
myfile = pd.read_csv(‘myfile.csv’)

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
#为了对每一行进行处理，可以直接用apply或者map
#例如df中有列名time，形如2017-02-03，我们计算每行数据属于星期几
#这样df中增加了一列weekday。
#Split()函数是用于分割字符串的，上面的x.split(‘-’)[0]表示将x根据‘-’分割，取出分割后的第一份数据。

from datetime import date
df['weekday']=df.time.apply(lambda x:date(int(x.split('-')[0]),int(x.split('-')[1]),int(x.split('-')[2])).weekday()+1)

# 有时候对每行数据要进行复杂的操作，可能用简单的一行写不下，那么可以单独写一个函数，来处理，再将函数传给apply函数即可，如：
def computeweek(x)
    Do it
    Return num

#定义函数
#这里可以不用传参数x，apply函数可以自动传入参数。
df['weekday']=df.time.apply(computeweek)

#表示将time列只保留年份
同样，map函数也对每一行进行处理，如
df[‘year’]=df.time.map(x:x.split('-')[0])


#这个函数是用来将列中的值转化为列名，简单点说就是可以做onehot编码。
get_dummies()函数实现onehot编码


#这样就将上面weekday中1~7的值变成了7列，列名分别为weekday_1~weekday_7
week =pd.get_dummies(train_x['weekday']).add_prefix('weekday_')


#将t按照列id和name进行分组，将分组后的每个组根据score求每个#组score的平均值。
df = df.groupby(['id','name'])[‘score’].mean()


#用于去除重复的行
Df.drop_duplicates(inplace=True)


#修改列的数据类型, 将原来的数据类型改成了字符串类型
 df[‘score’]=df[‘score’].astype(‘str’)


