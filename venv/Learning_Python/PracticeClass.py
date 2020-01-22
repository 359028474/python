'''
---------------------------------------
@名称 --%@NAME: PracticeClass
@功能名称 --%@COMMENT:
@执行参数 --%@PERIOD:
@创建人 --%@CREATEOR: ZhangJian
@创建时间 --%@CREATED_TIME: 2020/1/17
@修改记录 --%@MODIFY:
@来源表 --%@FROM:
@目标表 --%@TO:
---------------------------------------
'''
import math

class PracticeClass():

    # % 是占位符, 在 python 中表示 % 要用 %% 表示
    # %d 整数占位符  %f 小数占位符 %s 字符串占位符
    def func1():
        f = float(input('请输入华氏温度:'))
        c = (f - 32) / 1.8
        print('%.1f华氏度 = %.1f摄氏度' % (f,c))

    def func2():
        radius = float(input('请输入圆的半径:'))
        perimeter = 2 * math.pi * radius
        area = math.pi * radius * radius
        print('周长:%.2f' % perimeter)
        print('面积:%.2f' % area)

    def func3():
        year = int(input('请输入年份:'))
        is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        print(is_leap)

PracticeClass.func1()
PracticeClass.func2()
PracticeClass.func3()

