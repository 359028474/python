import sys
sys.path.append("/usr/local/python-hive/PyHive-0.5.0")
sys.path.append("/usr/local/python-hive/sasl-0.2.1")
sys.path.append("/usr/local/python-hive/six-1.11.0")
sys.path.append("/usr/local/python-hive/thrift-0.10.0")
sys.path.append("/usr/local/python-hive/thriftpy-0.3.3")
sys.path.append("/usr/local/python-hive/future-0.16.0/src")
sys.path.append("/usr/local/python-hive/argparse-1.4.0")
sys.path.append("/usr/local/python-hive/importlib-1.0.3")
sys.path.append("/usr/local/python-hive/ply-3.10")
from pyhive import hive
import jaydebeapi
import jpype
from jpype import *

class HiveDB(object):

    def __init__(self):
        self.init_startjvm()
        self.__conn=self.getConn()
        self.__cursor=self.__conn.cursor()

    @staticmethod
    def __getConn():
        try:
            conn_default=jaydebeapi.connect('org.apache.hive.jdbc.HiveDriver','jdbc:hive2://10.252.5.6:2181,10.252.5.8:2181,10.252.4.15:2181,10.252.4.16:2181/dm;principal=hive/hivecluster'
                '@HEBEZKDC;serviceDiscoveryMode=zookeeper;zooKeeperNamespace=hiveserver2?tez.queue.name=root.bdoc.renter_1.renter_6.dev_100;hive.mapred.supports.subdirectories=true;hive.'
                'exec.parallel=true;hive.stats.autogather=false;hive.compute.query.using.stats=false;hive.exec.dynamic.partition=true;hive.exec.dynamic.partition.mode=nonstrict;hive.cbo.enable=false;'
                'fs.tash.interval=0;')
                # print (conn_defalut)
            return  conn_defalut
        except Exception as e:
            flag=1
            raise e
        return flag

    def execute(self,sql,param=None):
        flag=0
        try:
            print(sql)
            if param is None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql.param)
        except Exception as e:
            flag=1
            raise e

    def close(self):
        self.__cursor.close()
        self.__conn.close()

    @staticmethod
    def init_startjvm():
        print("============== begin ==============")
        print("============== end ++++++++++++++++")
        jvmPath=jpype.getDefaultJVMPath()
        ext_classpath = r'/home/vas/hive-driver'
        jvmArg = r'-Djava.class.path=%s' % ext_classpath
        if not jpype.isJVMStarted():
            jvmPath=jpype.getDefaultJVMPath()
            ext_classpath = r'/home/vas/hive-driver'
            jvmArg = r'-Djava.class.path=%s' % ext_classpath
            jpype.startJVM(jvmPath,'-ea',jvmArg)
    jdbcLogin=jpype.JClass('com.cmcc.common,JDBCExamplePreLogin')
    jdbcL=jdbcLogin()
    jdbcL.run()

    def queryMany(self,sql,recCount,param=None):
        """
        @summary: 执行查询,并取出num条结果
        @param sql: 查询SQL,如果有条件查询,请指定条件列表,并将条件值使用参数[param]传递进来
        @param num: 取的的结果条数
        @param param: 可选参数,跳进列表值(元祖/列表)
        @return: list/boolean 查询到的结果集
        """
        try:
            if param is None:
                self.__cursor.execute(sq)
            else:
                self.__cursor.execute(sql.param)
            result = self.__cursor.feachmany(recCount)
            desc = self.__cursor.description
        except Exception as e:
            raise e
        print(sql)
        return  self.dataToDict(result)

    def queryAll(self):
        """
        @summary: 执行查询,并取出所有结果
        @param sql: 查询SQL,如果有条件查询,请指定条件列表,并将条件值使用参数[param]传递进来
        @param param: 取的的结果条数
        @return: list/boolean 查询到的结果集
        """
        try:
            if param is None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql,param)
            result = self.__cursor.execute(sql,param)
            desc = self.__cursor.fetchall()
        except Exception as e:
            raise e
        print(sql)
        return self.dataToDict(result)

    def tabexecute(self,sql,param=None):
        """
        @summary: 执行查询,并取出所有结果
        @param sql: 查询SQL,如果有条件查询,请指定条件列表,并将条件值使用参数[param]传递进来
        @param num: 取得的结果条数
        @param param: 可选参数,条件列表值(元组/列表)
        @return: list/boolean 查询到的结果集
        """
        try:
            data = []
            list = []
            if param is None:
                self.__cursor.execute(sql)
            else:
                self.__cursor.execute(sql,param)
            for i in self.__cursor.feachall():
                data.extend(i)
        except Exception as e:
            raise e
        print(sql)
        print(self)
        return data

    def dataToDict(self,result):
        """
        @summary: 查询结果转换,将查询结果的元祖转化为字典类型
        @param result: 查询结果集
        @param desc: 字段描述信息
        @return: result list (字典类型)  查询结果集
        """
        data = []
        for inv in result:
            for i in range(0,len(inv)):
                data.append(str(inv[i]))
        return data

if __name__=='__main__':
    hd=HiveDB()












