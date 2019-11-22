# coding=utf-8

import sys
from common.dbtool.ACDao import HiveDB
from common.utils.Log import Log
from common.utils.util import days

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
    def tdm_BZK_customers_of_level1dq(self,planname,taskname,statis_date):
        '''
        ---------------------------------------
        @名称 --%@NAME: tdm_BZK_customers_of_level1dq
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
        try:
            hd = HiveDB()
            flag = 0
            file = open('/home/vas/vgop_py/iop_label/the_latest_date.txt')
            the_lasted_date = file.readline()
            file.close()

            # 判断是否有分区
            sql_1 = '''
            alter table dm.tdm_iop_label_bzk_customers_of_level1_dq_d drop if exists partition(statis_date=%(statis_date)s)
            '''% { 'STATIS_DATE':statis_date }
            hd.execute(sql_1)

            # 配置MR任务开启并行执行
            sql_1 = '''set hive.exec.parallel=true'''
            hd.execute(sql_1)

            # 配置倾斜数据处理
            sql_1 = '''set hive.groupby.skewindata=true'''
            hd.execute(sql_1)

            # 设置reduce任务个数的最大值
            sql_1 = '''set hive.exec.reducers.max=300'''
            hd.execute(sql_1)

            # 2019年6月起至今,一经在网的宝藏卡客户
            sql = 'sql_1'
            sql_1 = '''
                insert into table dm.tdm_iop_bzk_customer_label_d partition(statis_date=%(statis_date)s)
                select '01',tb.buy_serv_num,'y'
                from ods_vas.tods_busi_order_history_d tb
                join ods_vas.tods_super_bass_user_info_fig_d ts
                on tb.buy_serv_num = ts.serv_num
                where  ts.user_stat like "1%%" and tb.buy_state="8" and tb.statis_date  >= "20190601" and tb.statis_date <= %(statis_date)s 
                and ts.statis_date =  %(the_lasted_date)s
            ''' % { 'statis_date':statis_date,'the_lasted_date':the_lasted_date}
            hd.execute(sql_1)

            # 2019年6月起至今,一经在网的一级电渠宝藏卡客户
            sql = 'sql_2'
            sql_2= '''
                insert into table dm.tdm_iop_bzk_customer_label_d partition(statis_date=%(statis_date)s)
                select '02',tb.buy_serv_num,'y'
                from ods_vas.tods_busi_order_history_d tb
                join ods_vas.tods_super_bass_user_info_fig_d ts
                on tb.buy_serv_num = ts.serv_num
                join dim.td_plat_dft_tb_rwk_chn_data_d tp
                on tb.channe_id = tp.chn_id
                where  ts.user_stat like "1%" and tb.buy_state="8" and tp.chn_code='jy11010000' and tb.statis_date  >= "20190601" and tb.statis_date <= %(statis_date)s 
                and ts.statis_date =  %(the_lasted_date)s                               
            ''' % { 'statis_date':statis_date,'the_lasted_date':the_lasted_date}

            hd.execute(sql_2)
            hd.close
            return flag

        except Exception as e:
            flag = 1
            # 参数说明
            Log().do_log(planname,taskname,sys.argv[0].replace('\\','\\\\'),statis_date,e,sql,hd)
            hd.close()
            return flag


