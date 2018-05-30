# 2018/05/20
from sqlobject import *


class Project(SQLObject):
    nid = StringCol(unique=True)
    name = StringCol()
    branch = StringCol()  # ForeignKey('Branch')
    type = StringCol()
    a_code = StringCol()
    f_code = StringCol()
    issue_date = DateCol()
    duration = IntCol()
    amount = IntCol()
    leverage_ratio = FloatCol()
    warning_line = FloatCol()
    stop_line = FloatCol()
    status = StringCol(default='存续')
    guarantor = RelatedJoin('Guarantor')
    adviser = RelatedJoin('Adviser')
    posterior = RelatedJoin('Posterior')

    def __str__(self):
        return '(' + str(self.nid) + ')' + str(self.name)


class Guarantor(SQLObject):
    project = RelatedJoin('Project')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class Adviser(SQLObject):
    project = RelatedJoin('Project')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class Posterior(SQLObject):
    project = RelatedJoin('Project')
    nid = StringCol(unique=True)
    name = StringCol()

    def __str__(self):
        return str(self.name) + '(' + str(self.nid) + ')'


class StockRecord(SQLObject):
    project = ForeignKey('Project')
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


class NavRecord(SQLObject):
    project = ForeignKey('Project')
    infodate = DateCol()
    nav = FloatCol()

    def __str__(self):
        return str(self.infodate) + ' : ' + str(self.nav)

    def __float__(self):
        return self.nav


class StockLedge(SQLObject):
    infodate = DateCol()
    code = StringCol()
    name = StringCol()
    date_before_suspend = DateCol(notNone=False)
    project_num = IntCol()
    project_num_20 = IntCol()
    holdings = IntCol()
    holdings_to_total = FloatCol()
    mv = FloatCol()
    avg_turnover = FloatCol()
    days_to_settle = FloatCol()

    def __str__(self):
        return "%s(%s)" % (self.name, self.infodate)


class ProjectLedge(SQLObject):
    infodate = DateCol()
    project = ForeignKey('Project')
    nid = StringCol()
    name = StringCol()
    branch = StringCol()
    type = StringCol()
    f_code = StringCol()
    issue_date = DateCol()
    duration = IntCol()
    amount = IntCol()
    leverage_ratio = FloatCol()
    warning_line = FloatCol()
    stop_line = FloatCol()
    stock_num = IntCol()
    stock_num_st = IntCol()
    stock_num_sup = IntCol()
    nav_now = FloatCol()
    nav_last = FloatCol()
    nav_pct = FloatCol()
    nav2stop = FloatCol()
    nav2warn = FloatCol()


class BranchLedge(SQLObject):
    infodate = DateCol()
    name = StringCol()
    amount_total = FloatCol()
    amount_avg = FloatCol()
    amount_max = FloatCol()
    project_num = IntCol()
    project_num_stop = IntCol()
    project_num_warn = IntCol()
    stock_num = IntCol()
    stock_num_st = IntCol()
    stock_num_suspend = IntCol()

    def __str__(self):
        return "%s(%s)" % (self.name, self.infodate)


class GuarantorLedge(SQLObject):
    infodate = DateCol()
    name = StringCol()
    nid = StringCol()
    branch_num = IntCol()
    project_num = IntCol()
    project_num_stop = IntCol()
    project_num_warn = IntCol()
    amount_total = FloatCol()
    amount_avg = FloatCol()
    stock_num = IntCol()
    stock_num_sup = IntCol()
    stock_num_st = IntCol()
    tp1_code = StringCol()
    tp1_name = StringCol()
    tp1_mv = FloatCol()
    tp1_pct = FloatCol()
    tp2_code = StringCol()
    tp2_name = StringCol()
    tp2_mv = FloatCol()
    tp2_pct = FloatCol()
    tp3_code = StringCol()
    tp3_name = StringCol()
    tp3_mv = FloatCol()
    tp3_pct = FloatCol()
    tp4_code = StringCol()
    tp4_name = StringCol()
    tp4_mv = FloatCol()
    tp4_pct = FloatCol()
    tp5_code = StringCol()
    tp5_name = StringCol()
    tp5_mv = FloatCol()
    tp5_pct = FloatCol()


def set_table(db_name):
    print('>> Setting main database to %s' % db_name)
    from sqlobject.sqlite import builder
    try:
        cnx = builder()(db_name)

        Project._connection = cnx
        NavRecord._connection = cnx
        StockRecord._connection = cnx
        Guarantor._connection = cnx
        Adviser._connection = cnx
        Posterior._connection = cnx
        ProjectLedge._connection = cnx
        StockLedge._connection = cnx
        BranchLedge._connection = cnx
        GuarantorLedge._connection = cnx

        Project.createTable(ifNotExists=True)
        NavRecord.createTable(ifNotExists=True)
        StockRecord.createTable(ifNotExists=True)
        Guarantor.createTable(ifNotExists=True)
        Adviser.createTable(ifNotExists=True)
        Posterior.createTable(ifNotExists=True)
        ProjectLedge.createTable(ifNotExists=True)
        StockLedge.createTable(ifNotExists=True)
        GuarantorLedge.createTable(ifNotExists=True)
        BranchLedge.createTable(ifNotExists=True)

    except Exception as e:
        print('   Error:%s' % e)


set_table('data\\data.db')
