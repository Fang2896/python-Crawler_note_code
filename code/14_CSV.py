import csv


# 读CSV文件的操作方法

# 方法1 ：以列表的下标的方式读取 
with open("stock.csv", 'r') as fp:
    # reader是一个迭代器
    reder = csv.reader(fp)
    next(reader)    # 跳过第一行（标题）
    for x in reader:
        # 获取所有数据（由一个个列表组成）
        print(x)
        # 获取第4列和最后一列的数据
        name = x[3]
        volumn = x[-1]

# 方法二：通过字典的方法获取（比如列的名字，行的名字）
with open("stock.csv", "r") as fp:
    reader = csv.DictReader(fp)
    # 这个DictReader返回了一个字典。而且不包含标题那行的数据
    # reader是一个迭代器。遍历这个迭代器，返回来的是一个字典
    for x in reader:
        print(x) 
        print(x["name"])  # 等等。以此类推 


# 表头信息
headers = ['username', 'age', 'height']
# 数据信息：
values = [
    {"张三", 19, 180},
    {"李四", 19, 160}
]
# 写入CSV文件, 注意文件编码

# 1. 用元组的方式写数据
# 注意这个open函数里面的参数，newline，如果不指定的话默认是\n，也就是换行符，所以如果不指定的话，写入数据的时候，数据行与行之间会多一行空行。所以这里newline='' ， 这样就可以避免
with open('classroom.csv','w', encoding="utf-8", newline='') as fp:
    writer = csv.writer(fp)
    # 这样就可以用writer来操作这个csv文件了
    # 我们先要写表头信息
    writer.writerow(headers)
    # 然后写数据
    writer.writerows(values)
    # writerows一次性写入多行数据


# 2. 用字典的方式写数据
values1 = [
    {'username':'张三', 'age':16, 'height':160},
    {'username':'李四', 'age':18, 'height':180},
]
with open("classroom1.csv", "w", encoding="utf-8", newline='') as fp:
    # 注意这里需要两个参数，一个文件指针，一个表头信息
    writer = csv.DictWriter(fp, headers)
    # 注意！！！写入表头数据的时候，需要调用writeheader方法！！！！！！！！！！！！！！！！！！
    writer.writeheader()
    # 写数据的时候也有两种方法,一种只能写一行，一种写多行
    writer.writerows(values1)
