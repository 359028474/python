# python通过jdbc连接数据库的模块
import jaydebeapi
from pyhive import hive

statis_month = '201911'
# connect(驱动jar包,['host'.'用户名'.'密码'],'驱动包地址')
conn=jaydebeapi.connect('com.mysql.jdbc.Driver',['jdbc:mysql://192.168.134.15:3306/exam_1','root','123456'],'/opt/app/hive/lan/codes/useJPype/mysql-connector-java-5.1.36/mysql-connector-java-5.1.36-bin.jar')
# 其中mysql的用户名和密码都是hive,最后一个参数是驱动的jar包
# curs是连接连接对象
curs=conn.cursor()
sql_1 = '''
insert overwrite table dm.table_name partition(statis_month=%(statis_month)s)
''' % { 'statis_month': statis_month}
curs.execute("create table user('ID' int,'NAME' string)")
curs.execute("insert into user values(1,'John')")
curs.execute("select * from user")
curs.execute(sql_1)
# 接收返回的结果行
result = curs.fetchall()
for e in result:
    print(e)
# [(1,u'John')]





