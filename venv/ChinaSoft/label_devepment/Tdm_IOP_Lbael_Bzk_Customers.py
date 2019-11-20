# coding=utf-8

import sys
from iop_label.bzk_label.dm.sub.bzk_customers_of_level1_DQ import bzk_customers_of_level1_DQ

class Tdm_IOP_Label_Bzk_Customers(object):
    '''
    ---------------------------------------
    @名称 --%@NAME: Tdm_IOP_Lbael_Bzk_Customers
    @功能名称 --%@COMMENT:
    @执行参数 --%@PERIOD:
    @创建人 --%@CREATEOR: ZhangJian
    @创建时间 --%@CREATED_TIME: 2019/11/20
    @修改记录 --%@MODIFY:
    @来源表 --%@FROM:
    @目标表 --%@TO:
    ---------------------------------------
    '''

    planname = sys.argv[1]
    taskname = sys.argv[2]
    statis_date = sys.argv[3]

    flag = bzk_customers_of_level1_DQ().tdm_BZK_customers_of_level1dp(planname,taskname,statis_date)
    sys.exit(flag)