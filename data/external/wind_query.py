from WindPy import w
from pandas import DataFrame as DF
from pandas import merge
from datetime import *
import os


def get_data(jdate):
    return fill_data(load_code_list(jdate))


def load_code_list(jdate):
    if not w.isconnected():
        w.start()
    stock = w.wset("sectorconstituent", "date=" + jdate + ";sectorid=a001010100000000")
    stock_df = DF(stock.Data, index=stock.Fields, columns=stock.Codes)
    stock_df = stock_df.T
    return stock_df


def fill_data(data):
    if not w.isconnected():
        w.start()
    jdate = data['date'][0].date().isoformat()
    sdate = (data['date'][0].date() + timedelta(days=-365)).isoformat()
    code_list = str(data['wind_code'].tolist()).replace("'", "").replace("[", "").replace("]", "")
    a = w.wss(code_list, "close,pq_avgturn2,share_totala,lastradeday_s,trade_status",
              "tradeDate=%s;priceAdj=U;cycle=D;startDate=%s;endDate=%s;unit=1" % (jdate, sdate, jdate))
    ddt = DF(a.Data, index=a.Fields, columns=a.Codes).T.reset_index()
    n_data = merge(data, ddt, left_on='wind_code', right_on='index')
    n_data.rename(
        columns={
            'wind_code': 'code',
            'sec_name': 'name',
            'CLOSE': 'price',
            'PQ_AVGTURN2': 'tr_year',
            'SHARE_TOTALA': 'totala',
            'LASTRADEDAY_S': 'last_date',
            'TRADE_STATUS': 'status',
        }, inplace=True)
    del n_data['index']
    return n_data


if __name__ == "__main__":
    print('====================================================================')
    print('                  底仓数据系统 - Wind 数据提取脚本')
    print('====================================================================')
    print('>> 说明：使用本程序需要安装 万得Wind软件并且启用 wind python 量化插件。')
    print('--------------------------------------------------------------------')
    jdate = input(">> 请输入口径日期（YYYY-MM-DD): ")
    print('....................................................................')
    data = get_data(jdate)
    print('....................................................................')
    print('>> 数据样本：')
    print(data.head(4))
    print('....................................................................')
    print('>> 统计信息：')
    print(data.describe())
    print('====================================================================')
    data.to_excel('%s.xls' % jdate)
    file_path = os.path.abspath('%s.xls' % jdate)
    print('>> 文件已保存至：%s' % file_path)
    os.system("start explorer %s" % os.path.dirname(file_path))
    holder = input(">> 按回车退出： ")