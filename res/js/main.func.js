// 侧边栏消息通知，根据此消息查询数据
// 信号：表名称
function sidebarsignal(gridid){
    return gridid;
}

// 打开Excel文件并批量导入数据
// 信号：文件路径（验证文件类型）
function importexcelsignal(){
    ;
}

// 保存记录：新增、修改、删除
// 数据有变动但未保存时提示
function saverecordssignal(){
    ;
}

// 参数：项目名称、口径日期、单位净值、JSON数据
// “导入净值表”中“打开Excel文件”改成“确认导入数据”
// recid作为识别码

function getexceldata(){
    ;
}

// 获取数据库操作消息（成果or失败）
function resetgrid(){
    ;
}

/*
grid1x1: 项目列表和差额补足人两个Excel文件同时传入
grid2x1: 导入一个Excel文件
         确认所有数据正确的时候，从python取回项目列表并由用户选择项目，项目、口径日期、单位净值、JSON数据一起传给python

*/

// 封装函数：显示数据到网页

