'''
---------------------------------------
@名称 --%@NAME: Demo2
@功能名称 --%@COMMENT:
@执行参数 --%@PERIOD:
@创建人 --%@CREATEOR: ZhangJian
@创建时间 --%@CREATED_TIME: 2020/1/17
@修改记录 --%@MODIFY:
@来源表 --%@FROM:
@目标表 --%@TO:
---------------------------------------
'''

f = open('C:\\Users\\DellDe\\Downloads\\5gcwb.txt','r') #打开文件
i = 0 #设置计数器
while i<2476237 : #这里12345表示文件行数，如果不知道行数可用每行长度等其他条件来判断
 with open('newfile'+str(i),'w') as f1:
  for j in range(0,1474160) : #这里设置每个子文件的大小
   if i < 12345 : #这里判断是否已结束，否则最后可能报错
    f1.writelines(f.readline())
    i = i+1
   else:
    break