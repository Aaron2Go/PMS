import pandas as pd
from models import *
from converts import *
import sys
import re


def go():
    ip_navfile('other\\1.xls', 1)
    ip_navfile('other\\2.xls', 2)
    ip_navfile('other\\3.xls', 3)
    ip_navfile('other\\1.xls', 4)
    ip_navfile('other\\2.xls', 5)
    ip_navfile('other\\3.xls', 6)
    ip_navfile('other\\1.xls', 7)
    ip_navfile('other\\2.xls', 8)


def del_record(tblid, recid):
    if tblid == 1:
        try:
            Project.delete(recid)
            print('Deleted!\n>> Record:\n   id:' + str(recid) + ' in table:Project')
            return [True, 'Done!']
        except Exception as e:
            print('Delete Failed!\n>> Record:\n   id:' + str(recid) + ' in table:Project\n>> Error:\n   ' + str(e))
            return [False, str(e)]
    else:
        print('Cannot Recognize Target Table!')
        return [False, 'Cannot Recognize Target Table!']


def mod_record(tblid, recid, content):
    # import json
    if tblid == 1:
        try:
            Project.get(recid).set(**content)
            print('Updated!\n>> Record:\n   id:' + str(recid) + ' in table:Project')
            return [True, 'Done!']
        except Exception as e:
            print('Update Failed!\n>> Record:\n   id:' + str(recid) + ' in table:Project\n>> Error:\n   ' + str(e))
            return [False, str(e)]
    else:
        print('Cannot Recognize Target Table!')
        return [False, 'Cannot Recognize Target Table!']


def ip_project(file_path):
    print('>> Import Project:')
    df = pd.read_excel(file_path, sheet_name='项目')
    print('   file loaded: ' + file_path)
    sys.stdout.write('   writing: ')
    sys.stdout.flush()
    ps0 = 0
    for i in range(0, len(df)):
        ps = (i + 1) * 100 / (len(df) + 1)
        if ps - ps0 > 8:
            sys.stdout.write('.')
            sys.stdout.flush()
            ps0 = ps
        new_project = {
            'nid': df['项目编码'][i],
            'name': df['项目名称'][i],
            'branch': df['经营机构'][i],
            'type': df['项目类型'][i],
            'a_code': str(df['申请书编号'][i]),
            'f_code': str(df['审批通知书编号'][i]),
            'issue_date': df['发行日期'][i].strftime('%Y-%m-%d'),
            'amount': df['金额（万）'][i].tolist(),
            'duration': df['期限（月）'][i].tolist(),
            'leverage_ratio': df['杠杆比例'][i].tolist(),
            'warning_line': df['预警线'][i].tolist(),
            'stop_line': df['止损线'][i].tolist(),
            'status': df['存续状态'][i],
        }
        if Project.selectBy(nid=new_project['nid']).count() == 0:
            Project(**new_project)
        else:
            print('   Skipped %s <- Project id already exist.' % new_project['nid'])
    print('   done!')


def ip_navfile(file_path, project_id):
    print('>> Reading Nav File:')
    df = pd.read_excel(file_path, sheet_name=0)
    print('   file loaded: ' + file_path)
    ptn1 = re.compile(r'估?值?日期:?：?\s*([0-9]{4}\S?[0-9]{2}\S?[0-9]{2})')
    ptn2 = re.compile(r'今?日?单位净值:?：?\s*([0-9]+.[0-9]+)')
    ptn3 = re.compile(r'[累计年初期昨修正调整]')
    str1 = ''
    print('   searching nav:')
    for row in range(0, len(df)):
        for col in range(0, df.shape[1] - 1):
            tmpstr = str(df.iat[row, col]) + str(df.iat[row, col + 1])
            if re.search(ptn1, tmpstr) is not None:
                str0 = re.search(ptn1, tmpstr).group(0)
                for i in range(0, len(str0)):
                    if str0[i].isdigit():
                        str1 += str0[i]
                        if len(str1) == 4:
                            str1 += '-'
                        elif len(str1) == 7:
                            str1 += '-'
                print('   口径日期: ', str1)
            elif re.search(ptn2, tmpstr) is not None and re.search(ptn3, tmpstr) is None:
                str2 = re.search(ptn2, tmpstr).group(1)
                print('   单位净值: ', str2)
    NavRecord(
        project=Project.get(project_id),  # 项目
        infodate=str1,  # 口径日期
        nav=float(str2),  # 净值
    )
    print('   analysing stock records...')
    df = df.fillna(0)
    field_row = 0
    target_field_id = '科目代码'
    valid_rows_list = []
    for field_row in range(0, len(df)):
        if df.iat[field_row, 0] == target_field_id:
            break
    field_row_repeat = 0
    while df.iat[field_row + field_row_repeat, 0] == target_field_id:
        field_row_repeat += 1
    target_field_state = '停牌信息'
    for field_column in range(0, df.shape[1]):
        if df.iat[field_row, field_column] == target_field_state:
            break
    for row in range(field_row + field_row_repeat, len(df)):
        if '正常' in str(df.iat[row, field_column]) or '停牌' in str(df.iat[row, field_column]):
            valid_rows_list.append(row)
    field_list_name = ['科目代码', '科目名称', '数量', '单位成本', '成本', '成本占比', '市价', '市值', '市值占比', '估值增值', '停牌信息']
    field_list_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for column in range(0, df.shape[1]):
        if '科目代码' in df.iat[field_row, column]:
            field_list_number[0] = column
        elif '科目名称' in df.iat[field_row, column]:
            field_list_number[1] = column
        elif '数量' in df.iat[field_row, column]:
            field_list_number[2] = column
        elif '单位成本' in df.iat[field_row, column]:
            field_list_number[3] = column
        elif '成本' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[4] = column
        elif '成本' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[5] = column
        elif '市价' in df.iat[field_row, column] or '行情' in df.iat[field_row, column]:
            field_list_number[6] = column
        elif '市值' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[7] = column
        elif '市值' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[8] = column
        elif '估值' in df.iat[field_row, column] or '增值' in df.iat[field_row, column]:
            field_list_number[9] = column
        elif '停牌' in df.iat[field_row, column] or '交易' in df.iat[field_row, column]:
            field_list_number[10] = column
    sys.stdout.write('>> writing: ')
    sys.stdout.flush()
    ps0 = 0
    temp_list = []
    k = 0
    for i in valid_rows_list:
        k = k + 1
        ps = k * 100 / (len(valid_rows_list) + 1)
        if ps - ps0 > 8:
            sys.stdout.write('.')
            sys.stdout.flush()
            ps0 = ps
        for j in range(0, len(field_list_name)):
            if j == 0:
                temp_list.append(format_field_id(df.iat[i, field_list_number[j]]))
            elif j == 1:
                temp_list.append(format_field_name(df.iat[i, field_list_number[j]]))
            elif j == 10:
                temp_list.append(format_field_status(df.iat[i, field_list_number[j]]))
            elif j == 5 or j == 8:
                temp_list.append(format_field_percentage(df.iat[i, field_list_number[j]]))
            else:
                temp_list.append(df.iat[i, field_list_number[j]])

        new_record = {
            'project': Project.get(project_id),
            'infodate': str1,
            'code': temp_list[0],
            'name': temp_list[1],
            'holdings': int(temp_list[2]),
            'purchase_price': float(temp_list[3]),
            'costs': float(temp_list[4]),
            'cost2nav': float(temp_list[5]),
            'market_price': float(temp_list[6]),
            'mv': float(temp_list[7]),
            'mv2nav': float(temp_list[8]),
            'valuation': float(temp_list[9]),
            'status': str(temp_list[10]),
        }
        StockRecord(**new_record)
        temp_list.clear()
    print('   done!')


def read_navfile(file_path):
    print('>> Reading Nav File:')
    df = pd.read_excel(file_path, sheet_name=0)
    print('   file loaded: ' + file_path)
    ptn1 = re.compile(r'估?值?日期:?：?\s*([0-9]{4}\S?[0-9]{2}\S?[0-9]{2})')
    ptn2 = re.compile(r'今?日?单位净值:?：?\s*([0-9]+.[0-9]+)')
    ptn3 = re.compile(r'[累计年初期昨修正调整]')
    str1 = ''
    print('   searching nav:')
    for row in range(0, len(df)):
        for col in range(0, df.shape[1] - 1):
            tmpstr = str(df.iat[row, col]) + str(df.iat[row, col + 1])
            if re.search(ptn1, tmpstr) is not None:
                str0 = re.search(ptn1, tmpstr).group(0)
                for i in range(0, len(str0)):
                    if str0[i].isdigit():
                        str1 += str0[i]
                        if len(str1) == 4:
                            str1 += '-'
                        elif len(str1) == 7:
                            str1 += '-'
                print('   口径日期: ', str1)
            elif re.search(ptn2, tmpstr) is not None and re.search(ptn3, tmpstr) is None:
                str2 = re.search(ptn2, tmpstr).group(1)
                print('   单位净值: ', str2)
    nav_record = {
        'infodate': str1,  # 口径日期
        'nav': float(str2),  # 净值
    }
    print('   done!')
    df = df.fillna(0)
    field_row = 0
    target_field_id = '科目代码'
    valid_rows_list = []
    for field_row in range(0, len(df)):
        if df.iat[field_row, 0] == target_field_id:
            break
    field_row_repeat = 0
    while df.iat[field_row + field_row_repeat, 0] == target_field_id:
        field_row_repeat += 1
    target_field_state = '停牌信息'
    for field_column in range(0, df.shape[1]):
        if df.iat[field_row, field_column] == target_field_state:
            break
    for row in range(field_row + field_row_repeat, len(df)):
        if '正常' in str(df.iat[row, field_column]) or '停牌' in str(df.iat[row, field_column]):
            valid_rows_list.append(row)
    field_list_name = ['科目代码', '科目名称', '数量', '单位成本', '成本', '成本占比', '市价', '市值', '市值占比', '估值增值', '停牌信息']
    field_list_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for column in range(0, df.shape[1]):
        if '科目代码' in df.iat[field_row, column]:
            field_list_number[0] = column
        elif '科目名称' in df.iat[field_row, column]:
            field_list_number[1] = column
        elif '数量' in df.iat[field_row, column]:
            field_list_number[2] = column
        elif '单位成本' in df.iat[field_row, column]:
            field_list_number[3] = column
        elif '成本' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[4] = column
        elif '成本' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[5] = column
        elif '市价' in df.iat[field_row, column] or '行情' in df.iat[field_row, column]:
            field_list_number[6] = column
        elif '市值' in df.iat[field_row, column] and '占' not in df.iat[field_row, column]:
            field_list_number[7] = column
        elif '市值' in df.iat[field_row, column] and '占' in df.iat[field_row, column]:
            field_list_number[8] = column
        elif '估值' in df.iat[field_row, column] or '增值' in df.iat[field_row, column]:
            field_list_number[9] = column
        elif '停牌' in df.iat[field_row, column] or '交易' in df.iat[field_row, column]:
            field_list_number[10] = column

    Record_List = pd.DataFrame(
        columns=[
            'code',
            'name',
            'holdings',
            'purchase_price',
            'costs',
            'cost2nav',
            'market_price',
            'mv',
            'mv2nav',
            'valuation',
            'status',
        ]
    )
    column_name = {
        'code': '代码',
        'name': '简称',
        'holdings': '持股数量',
        'purchase_price': '成本价',
        'costs': '总成本',
        'cost2nav': '成本占净值比例',
        'market_price': '收盘价',
        'mv': '市值',
        'mv2nav': '市值占净值比例',
        'valuation': '估值损益',
        'status': '交易状态',
    }
    # Record_List=Record_List.append(column_name,ignore_index=True)

    sys.stdout.write('   analysing: ')
    sys.stdout.flush()
    ps0 = 0
    temp_list = []
    k = 0
    for i in valid_rows_list:
        k = k + 1
        ps = k * 100 / (len(valid_rows_list) + 1)
        if ps - ps0 > 8:
            sys.stdout.write('.')
            sys.stdout.flush()
            ps0 = ps
        for j in range(0, len(field_list_name)):
            if j == 0:
                temp_list.append(format_field_id(df.iat[i, field_list_number[j]]))
            elif j == 1:
                temp_list.append(format_field_name(df.iat[i, field_list_number[j]]))
            elif j == 10:
                temp_list.append(format_field_status(df.iat[i, field_list_number[j]]))
            elif j == 5 or j == 8:
                temp_list.append(format_field_percentage(df.iat[i, field_list_number[j]]))
            else:
                temp_list.append(df.iat[i, field_list_number[j]])
        new_record = {
            'code': temp_list[0],
            'name': temp_list[1],
            'holdings': int(temp_list[2]),
            'purchase_price': float(temp_list[3]),
            'costs': float(temp_list[4]),
            'cost2nav': float(temp_list[5]),
            'market_price': float(temp_list[6]),
            'mv': float(temp_list[7]),
            'mv2nav': float(temp_list[8]),
            'valuation': float(temp_list[9]),
            'status': str(temp_list[10]),
        }
        Record_List = Record_List.append(new_record, ignore_index=True)
        temp_list.clear()
    print(' done!')
    return [Record_List, nav_record]


def load_excel(file_path):
    a = pd.read_excel(file_path)
    c_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    i = 0
    for c in a.columns:
        a.rename(columns={c: c_list[i], }, inplace=True)
        i = i + 1
    return a


def ip_guarantor(file_path):
    print('>> Import Garantor:')
    df = pd.read_excel(file_path, sheet_name='差补人')
    print('   file loaded: ' + file_path)
    sys.stdout.write('   writing: ')
    sys.stdout.flush()
    ps0 = 0
    for i in range(0, len(df)):
        ps = (i + 1) * 100 / (len(df) + 1)
        if ps - ps0 > 8:
            sys.stdout.write('.')
            sys.stdout.flush()
            ps0 = ps
        # people_type = df['类型'][i]
        new_people = {
            'nid': str(df['证件号'][i]),
            'name': str(df['名称'][i]),
        }
        if Project.selectBy(nid=df['项目编码'][i]).count() == 0:
            print('   Error: %s <- Project not found!' % df['项目编码'][i])
        else:
            # if people_type == '差补人':
            if Guarantor.selectBy(nid=new_people['nid']).count() == 0:
                g = Guarantor(**new_people)
            else:
                g = Guarantor.byNid(new_people['nid'])
            g.addProject(Project.byNid(df['项目编码'][i]))
            # else:
            #    print('   Error: %s <- Unexpected type' % people_type)
    print('   done!')


def ip_pg(file_path):
    ip_project(file_path)
    ip_guarantor(file_path)


def add_project(jsondata):
    pjt_list = jsondata[0]
    for p in pjt_list:
        if Project.selectBy(nid=p['nid']).count() == 0:
            np = Project(**p)
        else:
            print('   Error <- Project already exists.')
            return False
    gr_list = jsondata[1]
    for g in gr_list:
        if Guarantor.selectBy(nid=g['nid']).count() == 0:
            ng = Guarantor(**g)
        else:
            ng = Guarantor.byNid(g['nid'])
        np.addGuarantor(ng)
    return True


def write_navfile(jsondata):
    print('   writing navfile to database...')
    pjt=jsondata[0][0]
    infodate=jsondata[1][0]['date']
    nav_record={
        'project':Project.get(pjt['nid']),
        'infodate':infodate,
        'nav':jsondata[2][0]['value']
    }
    NavRecord(**nav_record)
    stk_set=jsondata[3]
    for s in stk_set:
        s['infodate']=infodate
        s['project']=Project.get(pjt['nid'])
        StockRecord(**s)