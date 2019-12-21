
message1 = "pauL"

# title 首字母大写 其他字母小写
print(message1.title())

# lower 全部小写
print(message1.lower())

# upper 全部大写
print(message1.upper())

# + 字符串的拼接
message2 = "geoRge"

message = message1 + " " + message2
print(message.title())

# strip 删除字符串两端的空格 lstrip 删除字符串左边的空格 rstrip 删除字符串右边的空格
favorite_language = ' python '
print(favorite_language.strip())  # 空格去掉了
print(favorite_language)    # 空格没有被去掉,因为这个作用是临时的
favorite_language = favorite_language.strip() # 赋值给新的变量,变量被改变
print(favorite_language)

