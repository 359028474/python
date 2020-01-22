'''
---------------------------------------
@名称 --%@NAME: if_else_Class
@功能名称 --%@COMMENT:
@执行参数 --%@PERIOD:
@创建人 --%@CREATEOR: ZhangJian
@创建时间 --%@CREATED_TIME: 2020/1/17
@修改记录 --%@MODIFY:
@来源表 --%@FROM:
@目标表 --%@TO:
---------------------------------------
'''

class if_else_Class():

    def func1():
        username = input('请输入用户名:')
        password = input('请输入口令:')
        if username == 'admin' and password == '123456':
            print('身份验证成功!')
        else:
            print('身份验证失败!')

    # 分段函数求知
    def func2():
        x = float(input('x = '))
        if x > 1:
            y = 3 * x -5
        elif x >= -1 and x <= 1:
            y = x + 2
        else:
            y = 5 * x + 3
        print('f(%.2f) = %.2f' % (x,y))

if_else_Class.func1()
if_else_Class.func2()
