# 2018/05/20
import os
from sqlobject import *


class Project_bk(SQLObject):
    nid = StringCol(unique=True)
    name = StringCol()
    branch = StringCol()
    type = StringCol()
    a_code = StringCol()
    f_code = StringCol()
    issue_date = DateCol()
    duration = IntCol()
    amount = IntCol()
    leverage_ratio = FloatCol()
    warning_line = FloatCol()
    stop_line = FloatCol()
    status = StringCol()
    guarantor = RelatedJoin('Guarantor_bk')
    adviser = RelatedJoin('Adviser_bk')
    posterior = RelatedJoin('Posterior_bk')

    def __str__(self):
        return '(' + str(self.nid) + ')' + str(self.name)


class Guarantor_bk(SQLObject):
    project = RelatedJoin('Project_bk')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class Adviser_bk(SQLObject):
    project = RelatedJoin('Project_bk')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class Posterior_bk(SQLObject):
    project = RelatedJoin('Project_bk')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class StockRecord_bk(SQLObject):
    project = ForeignKey('Project_bk')
    infodate = DateCol()
    code = StringCol()
    name = StringCol()
    holdings = IntCol()
    purchase_price = FloatCol()
    costs = FloatCol()
    cost2nav = FloatCol()
    market_price = FloatCol()
    mv = FloatCol()
    mv2nav = FloatCol()
    valuation = FloatCol()
    status = StringCol()


class NavRecord_bk(SQLObject):
    project = ForeignKey('Project_bk')
    infodate = DateCol()
    nav = FloatCol()

    def __str__(self):
        return str(self.infodate) + ' : ' + str(self.nav)

    def __float__(self):
        return self.nav


def set_bk_table(db_name,new_table=True):
    if new_table:
        if os.path.exists(db_name):
            try:
                os.remove(db_name)
            except Exception as e:
                print('   %s' % e)
                print('>> Cannot delete %s!' % db_name)
        print('>> Using %s for data export' % db_name)
    else:
        print('>> Using %s to update main database' % db_name)
    from sqlobject.sqlite import builder
    try:
        cnx_bk = builder()(db_name)

        Project_bk._connection = cnx_bk
        NavRecord_bk._connection = cnx_bk
        StockRecord_bk._connection = cnx_bk
        Guarantor_bk._connection = cnx_bk
        Adviser_bk._connection = cnx_bk
        Posterior_bk._connection = cnx_bk

        Project_bk.createTable(ifNotExists=True)
        NavRecord_bk.createTable(ifNotExists=True)
        StockRecord_bk.createTable(ifNotExists=True)
        Guarantor_bk.createTable(ifNotExists=True)
        Adviser_bk.createTable(ifNotExists=True)
        Posterior_bk.createTable(ifNotExists=True)
    except Exception as e:
        print('   Error:%s' % e)