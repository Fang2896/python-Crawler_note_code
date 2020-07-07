import json

# 将python对象转换为字符串

persons = [
    {
        "user":"张三",
        "age":20,
    },
    {
        "user":"李四",
        "age":24,
    }
]

# 将数据转换成json字符串
# json_str = json.dumps(persons)
# print(type(json_str))
# print(json_str)


# 将json数据直接dump到文件
# 注意这里dump中的ensure_ascii参数设置为False
# 不然会将中文等特殊字符自动转换为ASCII码类型
# 而且open中要指定编码类型，中文才不会乱码
with open("person.json", "w", encoding="utf-8") as fp:
    json.dump(persons, fp, ensure_ascii=False)

    # 注意，dumps不能存到文件当中，dump才能

# json字符串load成python对象
json_str = '[{"user":"张三","age":20,},{"user":"李四","age":24,}]'

# 将字符串load成json数据类型
persons = json.loads(json_str)

# 直接从文件中读取json数据类型：
with open("person.json", "r", encoding="utf-8") as fp:
    persons = json.load(fp)
    # 现在这个persons是列表类型
    for person in persons:
        print(person)
