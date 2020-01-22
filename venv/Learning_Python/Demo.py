'''
---------------------------------------
@名称 --%@NAME: Demo
@功能名称 --%@COMMENT:
@执行参数 --%@PERIOD:
@创建人 --%@CREATEOR: ZhangJian
@创建时间 --%@CREATED_TIME: 2019/12/21
@修改记录 --%@MODIFY:
@来源表 --%@FROM:
@目标表 --%@TO:
---------------------------------------
'''

import sys
try:
    while True:
        print('Please input a number:')
        n = int(sys.stdin.readline().strip('\n')) # strip('\n')表示以\n分隔，否则输出是“字符串+\n”的形式
        print('Please input some numbers:')
        sn = sys.stdin.readline().strip() # 若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn == '': # 输入空格结束
            break
        sn = list(map(int,sn.split())) # 如果要强制转换成int等类型，可以调用map()函数。
        print(n)
        print(sn,'\n')
except:
    pass
