import random
from math import sqrt

"""
 * @Description
 * @Author zhangjian<zhangjian044 @ chinasoftinc.com>
 * @Version V1.0.0
 * @Since 1.0
 * @Date 2019/12/16
 * @Desc: https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/04.%E5%BE%AA%E7%8E%AF%E7%BB%93%E6%9E%84.md
"""
class cycle_Class():
    """
    for 循环
    """
    def func1():
        sum = 0
        # range(101) 0-100 整数序列
        # range(1,100) 1-99 整数序列
        # range(1,100,2) 1-99 奇数序列
        # range(初始值,结束值,步长)
        for x in range(101):
            sum += x
        print(sum)

    def func2():
        sum = 0
        for x in range(2,101,2):
            sum += x
        print(sum)

    """
    while循环
    猜数字游戏
    计算机出一个1~100之间的随机数由人来猜
    计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
    """
    def func3():
        answer = random.randint(1,100)
        counter = 0
        while True:
            counter+=1
            number = int(input('请输入:'))
            if number < answer:
                print('大一点')
            elif number > answer:
                print('小一点')
            else :
                print('恭喜你猜对了!')
                break
        print('你总共猜了%d次' % counter)
        if counter > 7:
            print('你的智商余额明显不足')

    """
    九九乘法表
    """
    def func4():
        for i in range(1,10):
            for j in range(1,i + 1):
                print('%d*%d=%d' % (i,j,i*i),end='\t')
            print()

    """
    输入一个正整数判断它是不是素数
    """
    def func5():
        num = int(input('请输入一个正整数:'))
        end = int(sqrt(num))
        is_prime = True
        for x in range(2,end + 1):
            if num % x == 0:
                is_prime = False
                break
            if is_prime and num != 1:
                print('%d是素数' % num)
            else:
                print('%d不是素数' % num)

    """
    输入两个正整数计算它们的最大公约数和最小公倍数
    """
    def func6():
        x = int(input('x= '))
        y = int(input('y= '))
        # 如果x大于y就交换x和y的值
        if x > y:
            # 通过下面的操作将y的值赋给x, 将x的值赋给y
            x,y = y,x
        # 从两个数中较小的数开始做递减的循环
        for factor in range(x,0,-1):
            if x % factor == 0 and y %factor == 0:
                print('%d和%d的最大公约数是%d' % (x, y, factor))
                print('%d和%d的最小公倍数是%d' % (x, y, x * y / factor))
                break
    """
    打印三角形
    *         *     *
    **       **    ***
    ***     ***   *****
    ****   ****  *******
    ***** ***** *********
    """
    def func7():
        row = int(input('请输入行数:'))
        for i in range(1,row + 1):
            for _ in range(i):
                print('*',end=' ')
            print()

        row = int(input('请输入行数:'))
        for i in range(1,row + 1):
            for _ in range(row - i):
                print(' ',end=' ')
            for _ in range(i):
                print('*',end=' ')
            print()
        row = int(input('请输入行数:'))
        for i in range(1,row+1):
            for _ in range(row - i):
                print(' ',end=' ')
            for _ in range(2*i-1):
                 print('*',end=' ')
            for _ in range(row - i):
                print(' ',end=' ')
            print()

# cycle_Class.func1()
# cycle_Class.func2()
# cycle_Class.func3()
# cycle_Class.func4()
# cycle_Class.func5()
# cycle_Class.func6()
cycle_Class.func7()