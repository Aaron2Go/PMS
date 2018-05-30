import pandas as pd
import numpy
from models import *
from converts import *
import datetime


def clt_stock(infodate, wind_file):
    print('>> Stock Summary:')
    t1 = datetime.datetime.now()
    for item in StockLedge.selectBy(infodate=infodate):
        item.delete(item.id)
    item_list = unique(StockRecord.selectBy(infodate=infodate), 'code')
    if len(item_list) > 0:
        print('   %s item(s) to calculate\n   ...' % len(item_list))
        # ledge = pd.DataFrame(
        #    columns=['infodate','code', 'name', 'date_before_suspend', 'project_num', 'project_num_20', 'holdings', 'holdings_to_total',
        #             'mv', 'avg_turnover', 'days_to_settle'])
        hist = pd.read_excel(wind_file)
        if len(hist['date'].drop_duplicates()) != 1 or hist['date'][0].date().isoformat() != infodate:
            print('   possible error on wind data file!')
            return False
        for row in range(len(hist)):
            hist.loc[row, 'code'] = hist.loc[row, 'code'][:6]
        for i in item_list:
            try:
                name = hist[hist['code'] == i]['name'].iloc[0]
                price = hist[hist['code'] == i]['price'].iloc[0]

                records = StockRecord.selectBy(infodate=infodate, code=i)
                holdings = records.sum('holdings')
                project_num = records.throughTo.project.count()
                project_num_20 = records.filter(
                    AND(StockRecord.q.cost2nav > 0.2, StockRecord.q.code == i)).throughTo.project.distinct().count()

                common_stock_outstanding = hist[hist['code'] == i]['totala'].iloc[0]
                holdings_to_total = holdings * 100 / common_stock_outstanding
                mv = price * holdings

                last_trade_day = hist[hist['code'] == i]['last_date'].iloc[0].date().isoformat()
                if last_trade_day != infodate:
                    date_before_suspend = last_trade_day
                else:
                    date_before_suspend = None

                avg_turnover = hist[hist['code'] == i]['tr_year'].iloc[0]
                if str(avg_turnover) == 'nan':
                    avg_turnover = -1
                days_to_settle = holdings * 100 / avg_turnover / common_stock_outstanding

                new_ledge = {
                    'infodate': infodate,
                    'code': i,
                    'name': name,
                    'date_before_suspend': date_before_suspend,
                    'project_num': int(project_num),
                    'project_num_20': int(project_num_20),
                    'holdings': float(holdings),
                    'holdings_to_total': float(holdings_to_total),
                    'mv': float(mv),
                    'avg_turnover': float(avg_turnover),
                    'days_to_settle': float(days_to_settle)
                }
                StockLedge(**new_ledge)
                # print(new_ledge)
                # ledge = ledge.append(new_ledge, ignore_index=True)
            except Exception as e:
                print('   Error on %s <- %s' % (i, str(e)))
        # print(ledge)
    else:
        print('   No records for %s!' % infodate)
    print('   Time Consumed：%s' % (datetime.datetime.now() - t1))
    print('   Done!')


def clt_project(infodate):
    print('>> Project Summary:')
    t1 = datetime.datetime.now()
    for i in ProjectLedge.selectBy(infodate=infodate):
        i.delete(i.id)
    item_list = StockRecord.selectBy(infodate=infodate).throughTo.project
    if item_list.count() > 0:
        print('   %s item(s) to calculate\n   ...' % item_list.count())
        for i in item_list:
            try:
                nav_now = NavRecord.selectBy(project=i, infodate=infodate)[0].nav
                avail_dates = sorted(unique(NavRecord.selectBy(project=i), 'infodate'))
                last_date = avail_dates[avail_dates.index(infodate) - 1]
                if last_date < infodate:
                    nav_last = NavRecord.selectBy(project=i, infodate=last_date)[0].nav
                    nav_pct = (nav_now - nav_last) * 100 / nav_last
                else:
                    nav_last = None
                    nav_pct = None
                new_pledge = {
                    'infodate': infodate,
                    'project': i,
                    'nid': i.nid,
                    'name': i.name,
                    'branch': i.branch,
                    'type': i.type,
                    'f_code': i.f_code,
                    'issue_date': i.issue_date,
                    'duration': i.duration,
                    'amount': i.amount,
                    'leverage_ratio': i.leverage_ratio,
                    'warning_line': i.warning_line,
                    'stop_line': i.stop_line,
                    'stock_num': len(unique(StockRecord.selectBy(project=i, infodate=infodate), 'code')),
                    'stock_num_sup': len(
                        unique(StockRecord.select(AND(StockRecord.q.project == i, StockRecord.q.status == '停牌')),
                               'code')),
                    'stock_num_st': len(
                        unique(StockRecord.select(AND(StockRecord.q.project == i, LIKE(StockRecord.q.name, '%S%T%'))),
                               'code')),
                    'nav_now': nav_now,
                    'nav_last': nav_last,
                    'nav_pct': nav_pct,
                    'nav2stop': nav_now - i.stop_line,
                    'nav2warn': nav_now - i.warning_line,
                }
                ProjectLedge(**new_pledge)
            except Exception as e:
                print('   Error on %s <- %s' % (i, str(e)))
    else:
        print('   No records for %s!' % infodate)
    print('   Time Consumed：%s' % (datetime.datetime.now() - t1))
    print('   Done!')


def clt_guarantor(infodate, wind_file):
    print('>> Guarantor Summary:')
    t1 = datetime.datetime.now()
    for item in GuarantorLedge.selectBy(infodate=infodate):
        item.delete(item.id)
    item_list = StockRecord.selectBy(infodate=infodate).throughTo.project.throughTo.guarantor.distinct()
    if item_list.count() > 0:

        hist = pd.read_excel(wind_file)
        if len(hist['date'].drop_duplicates()) != 1 or hist['date'][0].date().isoformat() != infodate:
            print('   possible error on wind data file!')
            return False
        for row in range(len(hist)):
            hist.loc[row, 'code'] = hist.loc[row, 'code'][:6]

        vector_stock = hist[['code']]

        print('   %s item(s) to calculate\n   ...' % item_list.count())

        for i in item_list:
            try:
                pjt_records = Guarantor.selectBy(id=i.id).throughTo.project
                stk_records = StockRecord.select(
                    IN(StockRecord.q.project, Guarantor.selectBy(id=i.id).throughTo.project))
                print('   %s:' % i)
                stk_ldege = clt_stock_set(stk_records, infodate, wind_file).sort_values(by='mv', ascending=False)
                vector_stock = vector_stock.merge(stk_ldege[['code', 'mv_pct']], how='left', on='code')
                vector_stock.rename(columns={'mv_pct': str(i.id)}, inplace=True)
                new_ledge = {
                    'infodate': infodate,
                    'name': i.name,
                    'nid': i.nid,
                    'branch_num': int(len(unique(pjt_records, 'branch'))),
                    'project_num': int(pjt_records.distinct().count()),
                    'project_num_stop': int(ProjectLedge.select(IN(ProjectLedge.q.project, pjt_records)).filter(
                        AND(ProjectLedge.q.nav2stop < 0, ProjectLedge.q.infodate == infodate)).distinct().count()),
                    'project_num_warn': int(ProjectLedge.select(IN(ProjectLedge.q.project, pjt_records)).filter(
                        AND(ProjectLedge.q.nav2warn < 0, ProjectLedge.q.infodate == infodate)).distinct().count()),
                    'amount_total': float(pjt_records.sum('amount')),
                    'amount_avg': float(pjt_records.avg('amount')),
                    'stock_num': int(len(unique(stk_records, 'code'))),
                    'stock_num_sup': int(len(unique(stk_records.filter(StockRecord.q.status == '停牌'), 'code'))),
                    'stock_num_st': int(len(unique(stk_records.filter(LIKE(StockRecord.q.name, '%S%T%')), 'code'))),
                    'tp1_code': stk_ldege['code'].iloc[0],
                    'tp1_name': stk_ldege['name'].iloc[0],
                    'tp1_mv': float(stk_ldege['mv'].iloc[0]),
                    'tp1_pct': float(stk_ldege['mv_pct'].iloc[0]),
                    'tp2_code': stk_ldege['code'].iloc[1],
                    'tp2_name': stk_ldege['name'].iloc[1],
                    'tp2_mv': float(stk_ldege['mv'].iloc[1]),
                    'tp2_pct': float(stk_ldege['mv_pct'].iloc[1]),
                    'tp3_code': stk_ldege['code'].iloc[2],
                    'tp3_name': stk_ldege['name'].iloc[2],
                    'tp3_mv': float(stk_ldege['mv'].iloc[2]),
                    'tp3_pct': float(stk_ldege['mv_pct'].iloc[2]),
                    'tp4_code': stk_ldege['code'].iloc[3],
                    'tp4_name': stk_ldege['name'].iloc[3],
                    'tp4_mv': float(stk_ldege['mv'].iloc[3]),
                    'tp4_pct': float(stk_ldege['mv_pct'].iloc[3]),
                    'tp5_code': stk_ldege['code'].iloc[4],
                    'tp5_name': stk_ldege['name'].iloc[4],
                    'tp5_mv': float(stk_ldege['mv'].iloc[4]),
                    'tp5_pct': float(stk_ldege['mv_pct'].iloc[4]),
                }
                # print(new_ledge)
                GuarantorLedge(**new_ledge)
            except Exception as e:
                print('   Error on %s <- %s' % (i, str(e)))
        # vector_stock =vector_stock.set_index('code')
        # vector_stock=vector_stock.fillna(0)
        # corr_matrix = pd.DataFrame(index=vector_stock.columns, columns=vector_stock.columns)
        # for c in vector_stock.columns:
        #    for r in vector_stock.columns:
        #        corr_matrix.loc[r, c] = numpy.linalg.norm(vector_stock[c] - vector_stock[r])
        # corr_matrix = corr_matrix.sort_index(axis=1).sort_index()
        # return corr_matrix
    else:
        print('   No records for %s!' % infodate)
    print('   Time Consumed：%s' % (datetime.datetime.now() - t1))
    print('   Done!')


def clt_stock_set(queryset, infodate, wind_file):
    t1 = datetime.datetime.now()
    item_list = unique(queryset, 'code')
    if len(item_list) > 0:

        hist = pd.read_excel(wind_file)
        if len(hist['date'].drop_duplicates()) != 1 or hist['date'][0].date().isoformat() != infodate:
            print('     possible error on wind data file!')
            return False
        for row in range(len(hist)):
            hist.loc[row, 'code'] = hist.loc[row, 'code'][:6]

        print('     %s item(s) to calculate\n   ...' % len(item_list))
        ledge = pd.DataFrame(
            columns=[
                'infodate',
                'code',
                'name',
                'date_before_suspend',
                'project_num',
                'project_num_20',
                'holdings',
                'holdings_to_total',
                'mv',
                'avg_turnover',
                'days_to_settle'
            ]
        )
        for i in item_list:
            try:
                name = hist[hist['code'] == i]['name'].iloc[0]
                price = hist[hist['code'] == i]['price'].iloc[0]

                records = queryset.filter(StockRecord.q.code == i)
                holdings = records.sum('holdings')
                project_num = records.throughTo.project.count()
                project_num_20 = records.filter(
                    AND(StockRecord.q.cost2nav > 0.2, StockRecord.q.code == i)).throughTo.project.distinct().count()

                common_stock_outstanding = hist[hist['code'] == i]['totala'].iloc[0]
                holdings_to_total = holdings * 100 / common_stock_outstanding
                mv = price * holdings

                last_trade_day = hist[hist['code'] == i]['last_date'].iloc[0].date().isoformat()
                if last_trade_day != infodate:
                    date_before_suspend = last_trade_day
                else:
                    date_before_suspend = None

                avg_turnover = hist[hist['code'] == i]['tr_year'].iloc[0]
                if str(avg_turnover) == 'nan':
                    avg_turnover = -1
                days_to_settle = holdings * 100 / avg_turnover / common_stock_outstanding

                new_pledge = {
                    'infodate': infodate,
                    'code': i,
                    'name': name,
                    'date_before_suspend': date_before_suspend,
                    'project_num': int(project_num),
                    'project_num_20': int(project_num_20),
                    'holdings': float(holdings),
                    'holdings_to_total': float(holdings_to_total),
                    'mv': float(mv),
                    'avg_turnover': float(avg_turnover),
                    'days_to_settle': float(days_to_settle)
                }
                # StockPledge(**new_pledge)
                # print(new_pledge)
                ledge = ledge.append(new_pledge, ignore_index=True)

            except Exception as e:
                print('     Error on %s <- %s' % (i, str(e)))
        total_mv = ledge['mv'].sum()
        ledge['mv_pct'] = ledge.apply(lambda x: x.mv * 100 / total_mv, axis=1)
    else:
        print('     No records for %s!' % infodate)
    print('     Time Consumed：%s' % (datetime.datetime.now() - t1))
    print('     Done!')
    return ledge


def clt_branch(infodate):
    print('>> Branch Summary:')
    t1 = datetime.datetime.now()
    for item in BranchLedge.selectBy(infodate=infodate):
        item.delete(item.id)
    item_list = unique(StockRecord.selectBy(infodate=infodate).throughTo.project, 'branch')
    if len(item_list) > 0:
        print('   %s item(s) to calculate\n   ...' % len(item_list))
        for i in item_list:
            new_pledge = {
                'infodate': infodate,
                'name': i,
                'amount_total': ProjectLedge.selectBy(branch=i, infodate=infodate).sum('amount'),
                'amount_avg': ProjectLedge.selectBy(branch=i, infodate=infodate).avg('amount'),
                'amount_max': ProjectLedge.selectBy(branch=i, infodate=infodate).max('amount'),
                'project_num': ProjectLedge.selectBy(branch=i, infodate=infodate).distinct().count(),
                'project_num_stop': ProjectLedge.selectBy(branch=i, infodate=infodate).filter(
                    ProjectLedge.q.nav2stop < 0).distinct().count(),
                'project_num_warn': ProjectLedge.selectBy(branch=i, infodate=infodate).filter(
                    ProjectLedge.q.nav2warn < 0).distinct().count(),
                'stock_num': len(unique(
                    StockRecord.select(IN(StockRecord.q.project, ProjectLedge.selectBy(branch=i).throughTo.project)),
                    'code')),
                'stock_num_st': len(unique(StockRecord.select(
                    IN(StockRecord.q.project, ProjectLedge.selectBy(branch=i).throughTo.project)).filter(
                    StockRecord.q.name == '%S%T%'), 'code')),
                'stock_num_suspend': len(unique(StockRecord.select(
                    IN(StockRecord.q.project, ProjectLedge.selectBy(branch=i).throughTo.project)).filter(
                    StockRecord.q.status == '停牌'), 'code')),
            }
            BranchLedge(**new_pledge)
    print('   Time Consumed：%s' % (datetime.datetime.now() - t1))
    print('   Done!')


def clt_all(infodate, wind_file):
    clt_stock(infodate, wind_file)
    clt_project(infodate)
    clt_guarantor(infodate, wind_file)
    clt_branch(infodate)
