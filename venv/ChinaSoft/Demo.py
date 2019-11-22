#!/usr/bin/python
# print('hello world')
# print("I'm %s. I'm %d year old" % ('Vamei', 99))
#
# statis_month = 201911
# sql_1 = '''
# insert overwrite table dm.table_name partition(statis_month=%(statis_month)s)
# ''' % { 'statis_month': statis_month}
# print(sql_1)
'''---------------test---------------'''
f = open('D:\\test.txt')
t = f.readline()
print(type(t))
print(t)