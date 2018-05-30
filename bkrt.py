from models_bk import *
from models import *
from converts import *


def export_db(infodate,main_file,bk_file):
    set_table(main_file)
    set_bk_table(bk_file,new_table=True)
    print('>> Export Databse:')
    project_set=StockRecord.selectBy(infodate=infodate).throughTo.project.distinct()
    total=project_set.count()
    print('   %s project(s) to export\n   ...' % total)
    i=0
    for p in project_set:
        try:
            i=i+1
            print('   %s/%s -> %s'%(i,total,p))
            p_k=Project_bk(**obj2dict(p))
            guarantor_set=Project.selectBy(id=p.id).throughTo.guarantor.distinct()
            if guarantor_set.count()!=0:
                for a in guarantor_set:
                    if Guarantor_bk.selectBy(nid=a.nid).count()==0:
                        a_k=Guarantor_bk(**obj2dict(a))
                    else:
                        a_k=Guarantor_bk.byNid(a.nid)
                    p_k.addGuarantor_bk(a_k)

            stock_set=StockRecord.selectBy(project=p, infodate=infodate)
            if stock_set.count()!=0:
                for s in stock_set:
                    arg=obj2dict(s)
                    arg['projectID']=p_k.id
                    StockRecord_bk(**arg)

            nav_set = NavRecord.selectBy(project=p, infodate=infodate)
            if nav_set.count()!=0:
                for n in nav_set:
                    arg = obj2dict(n)
                    arg['projectID'] = p_k.id
                    NavRecord_bk(**arg)
        except Exception as e:
            print('   Error on %s <- %s' % (p,e))
    print('   Done!')
    os.system("start explorer %s" % os.path.dirname(os.path.abspath(bk_file)))


def merge_db(infodate,main_file,bk_file):
    set_table(main_file)
    set_bk_table(bk_file,False)
    print('>> Merge Databse:')
    project_bk_set=StockRecord_bk.selectBy(infodate=infodate).throughTo.project.distinct()
    total=project_bk_set.count()
    print('   %s project(s) to import\n   ...' % total)
    i=0
    for p_k in project_bk_set:
        try:
            i = i + 1
            print('   %s/%s -> %s' % (i, total, p_k))
            if Project.selectBy(nid=p_k.nid).count()==0:
                p=Project(**obj2dict(p_k))
            else:
                p=Project.byNid(p_k.nid)
                p.set(**obj2dict(p_k))
            guarantor_bk_set=Project_bk.selectBy(id=p_k.id).throughTo.guarantor.distinct()
            guarantor_set=Project.selectBy(id=p.id).throughTo.guarantor.distinct()
            for a in guarantor_set:
                p.removeGuarantor(a)
            for a_k in guarantor_bk_set:
                if Guarantor.selectBy(nid=a_k.nid).count()==0:
                    a=Guarantor(**obj2dict(a_k))
                else:
                    a=Guarantor_bk.byNid(a_k.nid)
                a.addProject_bk(p)

            stock_set=StockRecord.selectBy(project=p, infodate=infodate)
            for s in stock_set:
                StockRecord.delete(s.id)
            stock_bk_set = StockRecord_bk.selectBy(project=p_k, infodate=infodate)
            for s_k in stock_bk_set:
                arg=obj2dict(s_k)
                arg['projectID']=p.id
                StockRecord(**arg)

            nav_set=NavRecord.selectBy(project=p, infodate=infodate)
            for n in nav_set:
                NavRecord.delete(n.id)
            nav_bk_set = NavRecord_bk.selectBy(project=p_k, infodate=infodate)
            for n_k in nav_bk_set:
                arg = obj2dict(n_k)
                arg['projectID'] = p.id
                NavRecord(**arg)
        except Exception as e:
            print('   Error on %s <- %s' % (p_k,e))
    print('   Done!')