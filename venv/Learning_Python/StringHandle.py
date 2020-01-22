import sys

class StringHandle():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # def info(self):
    #     print('%s:%s' % (self.name,self.age))
    #     message1 = "pauL"
    #
    #     # title 首字母大写 其他字母小写
    #     print(message1.title())
    #
    #     # lower 全部小写
    #     print(message1.lower())
    #
    #     # upper 全部大写
    #     print(message1.upper())
    #
    #     # + 字符串的拼接
    #     message2 = "geoRge"
    #
    #     message = message1 + " " + message2
    #     print(message.title())
    #
    #     # strip 删除字符串两端的空格 lstrip 删除字符串左边的空格 rstrip 删除字符串右边的空格
    #     favorite_language = ' python '
    #     print(favorite_language.strip())  # 空格去掉了
    #     print(favorite_language)  # 空格没有被去掉,因为这个作用是临时的
    #     favorite_language = favorite_language.strip()  # 赋值给新的变量,变量被改变
    #     print(favorite_language)
    #
    #     # 截取字符串
    #     n1 = input("请输入您要截取的字符串起始字符索引:\n")
    #     n2 = input("请输入您要截取的字符串结束字符索引:\n")
    #     # input 获取到的内容格式一律为字符串格式
    #     print(type(n1))
    #     print(favorite_language[int(n1):int(n2)]) # 从第1个字符开始到第4个字符
    #
    #     # 获取系统输入的两种方式
    #     num1 = input("请输入第一个数字:")
    #     sys.stdout.write("请输入第二个数字:")
    #     num2 = sys.stdin.readline()
    #     print("num1 + num2 = "+int(num1)+int(num2))

    def stringFunc(self):

        # find 返回要字符串在原字符串中的索引
        str = 'Paul George'
        res = str.find('e', 0, str.__len__())
        print(res)

        # index 跟find()方法一样，只不过如果sub不在string中会报一个异常 'substring not found'
        res = str.index('G',0,str.__len__())
        print(res)

        # count() 统计字符串出现的次数
        res = str.count('e',0,str.__len__())
        print(res)

        # replace() 替换并指定替换的次数
        res = str.replace('Paul','',str.count('Paul'))
        print(res)

        # split 字符串切割函数 , 遍历字符串
        res = str.split(' ',str.count(' '))
        for element in res:
            print(element)

        # startwith()
        res = str.startswith('Paul')
        res1 = str.endswith('rge')
        res2 = str.isalnum() # 判断字符串是否是只有字母和数字组成
        res3 = str.isalpha() # 判断字符串是否是只有字母组成
        res4 = str.isdigit() # 判断字符串是否是只有数字组成
        res5 = str.isnumeric() # 判断字符串是否是包含数字组成
        res6 = str.isdecimal() # 判断字符串是否是只含十进制
        print(res)

        # 按行分隔,一行一个元素
        res = str.splitlines()
        for element in res:
            print(element)

        # 字符串追加R
        res = str.join(' is FMVP!')
        print(res)

        # 字符串反转
        res = str[::-1]
        print(res)

George = StringHandle('George','27')
George.stringFunc()

