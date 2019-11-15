# coding=utf-8
import sys
# from common.dbtool.ACDao import HiveDB
# from common.utils.Log import Log
# from common.utils.util import days

class BZK_customers_of_level1_DQ(object):
    '''
    ---------------------------------------
    @名称 --%@NAME: BZK_customers_of_level1_DQ
    @功能描述 --%@COMMENT: 一级电渠订购宝藏卡客户(订购号码 6月至今)
    @创建人 --%@CREATOR: ZhangJian
    @备注 --%@REMARK:
    @修改记录 --%@MODIFY:
    ---------------------------------------
    '''
    def tdm_BZK_customers_of_level1dq(self,planname,taskname,the_lasted_date):
        '''
        ---------------------------------------
        @名称 --%@NAME: __function__
        @功能描述 --%@COMMENT: 一级电渠订购宝藏卡客户(订购号码 6月至今)
        @执行周期 --%@PERIOD: 日
        @参数 --%@PARAM: the_lasted_date eg:'20191115'
        @创建人 --%@CREATEOR: ZhangJian
        @创建时间 --%@CREATED_TIME: 20181114
        @修改记录 --%@MODIFY:
        @来源表 --%@FROM:
        @目标表 --%@TO:
        ---------------------------------------
        '''
        statis_month = str(the_lasted_date)[0,6]
        try:
            hd = HiveDB()
            flag = 0

            # 判断是否有分区
            sql_1 = '''
            alter table DM.TDM_IOP_LABEL_BZK_CUSTOMERS_OF_LEVEL1_DQ_D drop if exists partition(STATIS_DATE=%(STATIS_DATE)S)
            '''% { STATIS_DATE:the_lasted_date }
            hd.execute(sql_1)

            # 配置MR任务开启并行执行
            sql_1 = '''set hive.exec.parallel=true'''
            hd.execute(sql_1)

            # 配置倾斜数据处理
            sql_1 = '''set hive.groupby.skewindata=true'''
            hd.execute(sql_1)

            # 设置reduce任务个数的最大值
            sql_1 = '''set hive.exec.reducers.max=true'''
            hd.execute(sql_1)

            # 2019年6月起,一经在网的
            sql_1 = '''
                INSERT INTO TABLE DM.TDM_IOP_LABEL_BZK_CUSTOMERS_OF_LEVEL1_DQ_D PARTITION(STATIS_DATE=%(STATIS_DATE)S)
                SELECT TB.BUY_SERV_NUM
                FROM ODS_VAS.TODS_BUSI_ORDER_HISTORY_D TB
                JOIN ODS_VAS.TODS_SUPER_BASS_USER_INFO_FIG_D TS
                ON TB.BUY_SERV_NUM = TS.SERV_NUM
                WHERE  TS.USER_STAT LIKE "1%" AND TB.BUY_STATE="8" AND SUBSTR(STATIS_DATE,1,6)  BETWEEN "20190601" AND %(STATIS_DATE)S
            ''' % { STATIS_DATE:the_lasted_date }
            hd.execute(sql_1)

        except Exception as e:
            flag = 1
            # 参数说明
            Log().do_log(planname,taskname,sys.argv[0].replace('\\','\\\\'),statis_month,e,sql,hd)
            hd.close()
            return flag


