'''
 * @Description
 * @Author zhangjian<zhangjian044 @ chinasoftinc.com>
 * @Version V1.0.0
 * @Since 1.0
 * @Date 2019/12/16
 * @Desc: 构造程序逻辑
'''
class complex_Class():
    """
    寻找1000以内的水仙花数
    说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
    该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
    """
    def func1():
        for i in range(100,1000):
            a = i % 10
            b = i // 10 % 10
            c = i // 100
            if (a**3 + b**3 + c**3 == i):
                print('%d 是一个水仙花数;' % i)

complex_Class.func1()



