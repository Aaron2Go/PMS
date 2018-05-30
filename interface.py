# -*- coding: utf-8 -*-
print('====================================================================')
print('                          底 仓 数 据 系 统')
print('====================================================================')
print('>> 说明：')
print('        1、使用过程中请不要关闭本窗口。')
print('        2、请勿点击本窗口内部，该操作会造成程序暂停。')
print('        3、如点击后出现白色光标，请按回车键使程序继续执行。')
print('--------------------------------------------------------------------')
print('>> Loading packages...')
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from os.path import abspath
from PyQt5.QtCore import QUrl, QObject, pyqtSlot  # , pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt
from actions import *
from calculates import *
from bkrt import *
from models_user import *
import sys
import os
import json

# Define database connection
main_db = 'data/data.db'
usr_db = 'data/user'
set_user_table(usr_db)
set_table(main_db)

# Create an application
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

app = QApplication(sys.argv)
login_user = ''
c_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']


class CallHandler_Main(QObject):
    @pyqtSlot(str, str, str, result=bool)
    def mainSignal(self, grid_name, operation, jsdata):
        if grid_name == "func_init":
            # 初始化
            filename, filetype = QFileDialog.getOpenFileName(file_dialog, "请选取要导入的Excel文件：",
                                                             os.path.dirname(os.path.abspath('main.html')),
                                                             "Excel文件(*.xls;*.xlsx)")
            if filename:
                reply = QMessageBox.question(file_dialog, '提示', "是否确认导入%s？" % filename,
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    ip_pg(filename)
            return True
        elif grid_name == "func_import":
            pass
            # 数据库导入
        elif grid_name == "func_export":
            # 数据库导出
            if operation == "get":
                # js: func_export(date_list);
                ui.view.page().runJavaScript("func_export('%s');" % str(unique(NavRecord.select(), 'infodate')).replace("'",'"'))
                return True
            elif operation == "new":
                print(jsdata)
                global main_db
                export_db(jsdata, main_db, "%s.db" % jsdata)
                return True
                # jsdata = [{"date":"date", "project": "project"}]
        elif grid_name == "func_stat":
            if operation == "go":
                filename, filetype = QFileDialog.getOpenFileName(file_dialog, "请选取Excel文件：",
                                                                 os.path.dirname(os.path.abspath('main.html')),
                                                                 "Excel文件(*.xls;*.xlsx)")
                if filename:
                    clt_all(jsdata, filename)
                    return True
                else:
                    return False
            # 生成统计数据
            # jsdata = data_str
            elif operation == "get":
                # js: func_export(date_list);
                ui.view.page().runJavaScript("func_export('%s');" % str(unique(NavRecord.select(), 'infodate')).replace("'",'"'))
                return True
        elif grid_name == "grid1x1":
            # 项目列表
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(Project.select())))
                print(">> Operation: ", operation)
                return True
            elif operation == "new":
                # 增加记录
                print(">> Operation: ", operation)
                add_project(json.loads(jsdata))
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(Project.select())))
                return True
            elif operation == "get":
                # js: func_edit(rec)
                print(">> Operation: ", operation)
                return True
            elif operation == "edit":
                pass
                # jsdata = [{...}]
            elif operation == "delete":
                # jsdata = (recid list) -> [1,2,3...]
                print(">> Operation: ", operation)
                lst = json.loads(jsdata)
                for i in lst:
                    Project.get(i).delete(i)
                return True
            else:
                return False
        elif grid_name == "grid2x1":
            # 导入净值表
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                # 注意：grid2x1main和grid2x1preview均需刷新
                print(">> Operation: ", operation)
                return True
            else:
                return False
        elif grid_name == "grid2x1main":
            # 导入净值表 -> Excel数据
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                # 注意：grid2x1main和grid2x1preview均需刷新
                print(">> Operation: ", operation)
                return True
            elif operation == 'excel':
                print(">> Operation: ", operation)
                filename, filetype = QFileDialog.getOpenFileName(file_dialog, "请选取净值表文件：",
                                                                 os.path.dirname(os.path.abspath('main.html')),
                                                                 "Excel文件(*.xls;*.xlsx)")
                if filename:
                    clear_all_grid()
                    excel_loaded = load_excel(filename)
                    excel_read = read_navfile(filename)
                    global c_list
                    ui.view.page().runJavaScript(
                        "w2ui['%s'].hideColumn(%s);" % ("grid2x1main", str(c_list).replace('[', '').replace(']', '')))
                    ui.view.page().runJavaScript("w2ui['%s'].showColumn(%s);" % ("grid2x1main", df2cl(excel_loaded)))
                    ui.view.page().runJavaScript(
                        "w2ui['%s'].add(%s);" % ("grid2x1main", df2w2(excel_loaded)))
                    ui.view.page().runJavaScript(
                        "w2ui['%s'].add(%s);" % ("grid2x1preview", df2w2(excel_read[0])))
                    ui.view.page().runJavaScript(
                        'w2ui["grid2x1preview"].toolbar.set("date_txt", { text: "口径日期：%s"});' % excel_read[1][
                            'infodate'])
                    ui.view.page().runJavaScript(
                        'w2ui["grid2x1preview"].toolbar.set("value_txt", { text: "单位净值：%s"});' % excel_read[1]['nav'])
                # 此处设置口径日期和单位净值
                # 注意此处layout为preview而非main
                # 口径日期：js: w2ui["grid2x1preview"].toolbar.set("date_txt", { text: "口径日期：" + date });
                # 单位净值：js: w2ui["grid2x1preview"].toolbar.set("value_txt", { text: "单位净值：" + value });
                return True
            else:
                return False
        elif grid_name == "grid2x1preview":
            # 导入净值表 -> 净值表数据
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                # 注意：grid2x1main和grid2x1preview均需刷新
                print(">> Operation: ", operation)
                return True
            elif operation == "get":
                ui.view.page().runJavaScript("func_project('%s')" % w2_project(Project.select()))
                return True
                # js: func_project(project_list)
            elif operation == "new":
                # jsdata = [{...}]
                # 注意：grid2x1main和grid2x1preview均需刷新
                print(">> Operation: ", operation)
                write_navfile(json.loads(jsdata))
                return True
            else:
                return False
        elif grid_name == "grid2x2":
            # 净值数据
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(NavRecord.select())))
                return True
            else:
                return False
        elif grid_name == "grid2x3":
            # 底仓数据
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(StockRecord.select())))
                print(">> Operation: ", operation)
                return True
            else:
                return False
        elif grid_name == "grid3x1":
            # 信息概览
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                return True
            else:
                return False
        elif grid_name == "grid3x2":
            # 按经营机构统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(BranchLedge.select())))
                return True
            else:
                return False
        elif grid_name == "grid3x3":
            # 按项目统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(ProjectLedge.select())))
                return True
            else:
                return False
        elif grid_name == "grid3x4":
            # 按标的统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(StockLedge.select())))
                return True
            else:
                return False
        elif grid_name == "grid3x5":
            # 按差额补足人统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                clear_all_grid()
                ui.view.page().runJavaScript("w2ui['%s'].add(%s);" % (grid_name, w2_records(GuarantorLedge.select())))
                return True
            else:
                return False
        elif grid_name == "grid3x6":
            # 按投资顾问统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)

                return True
            else:
                return False
        elif grid_name == "grid3x7":
            # 按次级客户统计
            print(">> Current grid: ", grid_name)
            if operation == "refresh":
                # 刷新页面
                print(">> Operation: ", operation)
                return True
            else:
                return False
        else:
            return False


class UI_Main(QWidget):
    layout = QVBoxLayout()
    view = QWebEngineView()
    handler = CallHandler_Main()
    channel = QWebChannel()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('结构化项目底仓数据系统')
        self.setWindowIcon(QIcon('file:///' + abspath('res\\icon.png').replace('\\', '/')))
        self.setLayout(self.layout)
        self.layout.addWidget(self.view)
        self.setContentsMargins(0, 0, 0, 0)
        self.view.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, '提示', "是否确认退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class CallHandler_Login(QObject):
    # result = pyqtSignal(int) # self.result.emit(sss)
    @pyqtSlot(str, str, result=bool)
    def login(self, user, code):
        print('')
        if code == User.byName(user).code:
            global login_user
            login_user = user
            ui.view.load(
                QUrl('file:///' + abspath('res\main.html').replace('\\', '/')))
            ui.setWindowTitle('结构化项目底仓数据系统 [%s]' % login_user)
            ui.view.page().setWebChannel(ui.channel)
            ui.channel.registerObject('handler_ui', ui.handler)
            ui.showMaximized()
            login.close()
            return True
        else:
            return False


class UI_Login(QWidget):
    layout = QVBoxLayout()
    view = QWebEngineView()
    handler = CallHandler_Login()
    channel = QWebChannel()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('登陆')
        self.setWindowIcon(QIcon('file:///' + abspath('res/icon.png').replace('\\', '/')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setLayout(self.layout)
        self.layout.addWidget(self.view)
        self.setContentsMargins(0, 0, 0, 0)
        self.view.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.view.load(
            QUrl('file:///' + abspath('res/login.html').replace('\\', '/')))
        self.view.page().setWebChannel(self.channel)
        self.channel.registerObject('handler_login', self.handler)
        self.view.page().loadFinished.connect(load_user)


def load_user():
    login.view.page().runJavaScript("""
    var users = %s
    var targetSelect = document.getElementById('user');
    var frag = document.createDocumentFragment();
    for (var i = 0; i < users.length; i++) {
        var option = document.createElement("option");
        option.value = users[i];
        option.style = 'background-color: #1f1f2c;'
        option.innerHTML = users[i];
        frag.appendChild(option);
    }
    targetSelect.appendChild(frag);
    """ % str(unique(User.select(), 'name'))
                                    )


def clear_all_grid():
    grid_list = ['grid3x2', 'grid3x3', 'grid3x4', 'grid3x5', 'grid2x1preview', 'grid2x1main',
                 'grid2x2', 'grid1x1', 'grid2x3', ] # , 'grid3x6', 'grid3x7'
    for g in grid_list:
        ui.view.page().runJavaScript("w2ui['%s'].clear();" % g)


if __name__ == "__main__":
    print('--------------------------------------------------------------------')
    print('>> Starting UI...')
    file_dialog = QWidget()
    login = UI_Login()
    ui = UI_Main()

    login.show()

    sys.exit(app.exec_())
