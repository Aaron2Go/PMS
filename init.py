from actions import *
from calculates import *


def test_init():
    ip_pg('other\初始化.xls')
    go()
    clt_all('2018-02-22','data\external\\2018-02-22.xls')