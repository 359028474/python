# coding=utf-8

import sys
from iop_label.bzk_label.dm.sub.bzk_customers_of_level1_DQ import bzk_customers_of_level1_DQ

class Tdm_IOP_Label_Bzk_Customers(object):
    '''
    ---------------------------------------
    @名称 --%@NAME: Tdm_IOP_Lbael_Bzk_Customers
    @功能描述 --%@COMMENT:
    @创建人 --%@CREATEOR: ZhangJian
    @备注 --%@REMARK:
    @修改记录 --%@MODIFY:
    ---------------------------------------
    '''

    planname = sys.argv[1]
    taskname = sys.argv[2]
    statis_date = sys.argv[3]

    flag = bzk_customers_of_level1_DQ().tdm_BZK_customers_of_level1dp(planname,taskname,statis_date)
    sys.exit(flag)