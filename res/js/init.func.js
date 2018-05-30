// 配置HTML页面布局
var cur_sidebar = "grid3x1";
var config = {
	layout: {
		name: "layout",
		padding: 5,
		panels: [
			{ type: "top", size: 70, resizable: false, style: "background-color: #add8e6;" },
			{ type: "left", size: 180, resizable: false },
			{ type: "main", overflow: false, resizable: true },
			{ type: "preview", size: "50%", resizable: false, hidden: true },
			{ type: "bottom", size: 30, resizable: false, style: "background-color: #add8e6;" }
		]
	},
	sidebar: {
		name: "sidebar",
		nodes: [
			{
				id: "group1", text: "功能区", group: true, expanded: true,
				nodes: [
					{ id: "function0", text: "初始化导入", img: "icon-folder" },
					{ id: "function3", text: "数据库导入", img: "icon-folder" },
					{ id: "function2", text: "数据库导出", img: "icon-folder" },
					{ id: "grid2x1", text: "导入净值", img: "icon-page" },
					{ id: "function1", text: "生成统计数据", img: "icon-folder" }
				]
			},
			{
				id: "group2", text: "统计", group: true, expanded: true,
				nodes: [
					{ id: "grid3x1", text: "信息概览", img: "icon-page", selected: true },
					{ id: "grid3x2", text: "机构维度", img: "icon-page" },
					{ id: "grid3x3", text: "项目维度", img: "icon-page" },
					{ id: "grid3x4", text: "标的维度", img: "icon-page" },
					{ id: "grid3x5", text: "差补人维度", img: "icon-page" },
					{ id: "grid3x6", text: "投资顾问", img: "icon-page", hidden: true },
					{ id: "grid3x7", text: "次级客户", img: "icon-page", hidden: true }
				]
			},
			{
				id: "group3", text: "数据", group: true, expanded: true,
				nodes: [
					{ id: "grid1x1", text: "项目列表", img: "icon-page" },
					{ id: "grid2x2", text: "净值数据", img: "icon-page" },
					{ id: "grid2x3", text: "底仓数据", img: "icon-page" },
				]
			}
		],
		onClick: function (event) {
			switch (event.target) {
				case "function0":
					setSidebarState("function0");
					window.handler.mainSignal("func_init", "null", "null", function (result) { if (result == false) w2alert("Cannot do it.") });
					break;
				case "function1":
					setSidebarState("function1");
					//window.handler.mainSignal("func_stat", "null", "null", function (result) { if (result == false) w2alert("Cannot do it.") });
					func_stat();
					break;
				case "function2":
					setSidebarState("function2");
					window.handler.mainSignal("func_export", "get", "null", function (result) { if (result == false) w2alert("Cannot do it.") });
					//func_export();
					break;
				case "function3":
					setSidebarState("function3");
					func_import();
					break;
				case "grid1x1":
					setSidebarState("grid1x1");
					window.handler.mainSignal("grid1x1", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid1x1);
					w2ui.layout.hide("preview");
					break;
				case "grid2x1":
					setSidebarState("grid2x1");
					window.handler.mainSignal("grid2x1", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid2x1main);
					w2ui.layout.content("preview", w2ui.grid2x1preview);
					w2ui.layout.show("preview");
					break;
				case "grid2x2":
					setSidebarState("grid2x2");
					window.handler.mainSignal("grid2x2", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid2x2);
					w2ui.layout.hide("preview");
					break;
				case "grid2x3":
					setSidebarState("grid2x3");
					window.handler.mainSignal("grid2x3", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid2x3);
					w2ui.layout.hide("preview");
					break;
				case "grid3x1":
					setSidebarState("grid3x1");
					window.handler.mainSignal("grid3x1", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", '<h1>此处显示报表</h1>');
					w2ui.layout.hide("preview");
					break;
				case "grid3x2":
					setSidebarState("grid3x2");
					window.handler.mainSignal("grid3x2", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x2);
					w2ui.layout.hide("preview");
					break;
				case "grid3x3":
					setSidebarState("grid3x3");
					window.handler.mainSignal("grid3x3", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x3);
					w2ui.layout.hide("preview");
					break;
				case "grid3x4":
					setSidebarState("grid3x4");
					window.handler.mainSignal("grid3x4", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x4);
					w2ui.layout.hide("preview");
					break;
				case "grid3x5":
					setSidebarState("grid3x5");
					window.handler.mainSignal("grid3x5", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x5);
					w2ui.layout.hide("preview");
					break;
				case "grid3x6":
					setSidebarState("grid3x6");
					window.handler.mainSignal("grid3x6", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x6);
					w2ui.layout.hide("preview");
					break;
				case "grid3x7":
					setSidebarState("grid3x7");
					window.handler.mainSignal("grid3x7", "refresh", "null", function (result) { if (result == false) w2alert("Cannot open grid."); });
					w2ui.layout.content("main", w2ui.grid3x7);
					w2ui.layout.hide("preview");
					break;
			}
		}
	},
	grid1x1: {
		name: "grid1x1",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarAdd: true,
			toolbarEdit: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [
			{ field: "nid", caption: "编号", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "branch", caption: "经营机构", size: "10", sortable: true, searchable: true },
			{ field: "type", caption: "类型", size: "10", sortable: true, searchable: true },
			{ field: "f_code", caption: "审批编号", size: "10", sortable: true, searchable: true },
			{ field: "issue_date", caption: "发行日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "amount", caption: "金额", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "duration", caption: "期限", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "leverage_ratio", caption: "杠杆率", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "warning_line", caption: "预警线", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "stop_line", caption: "平仓线", size: "10", sortable: true, searchable: true, render: "float:2" }
		],
		toolbar: {
			onClick: function (event) {
				switch (event.target) {
					case "w2ui-reload":
						// 刷新数据
						window.handler.mainSignal("grid1x1", "refresh", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
					case "w2ui-add":
						// 增加记录
						func_add();
						break;
					case "w2ui-edit":
						// 编辑记录
						window.handler.mainSignal("grid1x1", "get", JSON.stringify(w2ui["grid1x1"].getSelection()), function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						var s = '[[{"nid":"编号","name":"名称","branch":"经营机构","type":"类型","f_code":"审批编号","issue_date":"2018-05-29","amount":10000.00,"duration":12,"leverage_ratio":2.00,"warning_line":0.90,"stop_line":0.85}],[{"nid":"2018","name":"张三"},{"nid":"2019","name":"李四"}],[{"nid":"2018","name":"张三"},{"nid":"2019","name":"李四"}],[{"nid":"2018","name":"张三"},{"nid":"2019","name":"李四"}]]';
						func_edit(s);
						break;
					case "w2ui-delete":
						// 删除记录
						window.handler.mainSignal("grid1x1", "delete", JSON.stringify(w2ui["grid1x1"].getSelection()), function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		},
		onExpand: function (event) {
			$('#' + event.box_id).html('<div style="padding: 10px; height: 100px">此处显示关于选定记录的信息</div>');
		}
	},
	grid2x1main: {
		name: "grid2x1main",
		header: "原始文件",
		selectType: "cell",
		show: {
			header: true,
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: false,
			toolbarAdd: false,
			toolbarEdit: false,
			toolbarDelete: false,
			toolbarSave: false,
			lineNumbers: true,
			footer: true
		},
		columns: [
			{ field: "A", caption: "A", size: 10, hidden: true },
			{ field: "B", caption: "B", size: 10, hidden: true },
			{ field: "C", caption: "C", size: 10, hidden: true },
			{ field: "D", caption: "D", size: 10, hidden: true },
			{ field: "E", caption: "E", size: 10, hidden: true },
			{ field: "F", caption: "F", size: 10, hidden: true },
			{ field: "G", caption: "G", size: 10, hidden: true },
			{ field: "H", caption: "H", size: 10, hidden: true },
			{ field: "I", caption: "I", size: 10, hidden: true },
			{ field: "J", caption: "J", size: 10, hidden: true },
			{ field: "K", caption: "K", size: 10, hidden: true },
			{ field: "L", caption: "L", size: 10, hidden: true },
			{ field: "M", caption: "M", size: 10, hidden: true },
			{ field: "N", caption: "N", size: 10, hidden: true },
			{ field: "O", caption: "O", size: 10, hidden: true },
			{ field: "P", caption: "P", size: 10, hidden: true },
			{ field: "Q", caption: "Q", size: 10, hidden: true },
			{ field: "R", caption: "R", size: 10, hidden: true },
			{ field: "S", caption: "S", size: 10, hidden: true },
			{ field: "T", caption: "T", size: 10, hidden: true },
			{ field: "U", caption: "U", size: 10, hidden: true },
			{ field: "V", caption: "V", size: 10, hidden: true },
			{ field: "W", caption: "W", size: 10, hidden: true },
			{ field: "X", caption: "X", size: 10, hidden: true },
			{ field: "Y", caption: "Y", size: 10, hidden: true },
			{ field: "Z", caption: "Z", size: 10, hidden: true }
		],
		toolbar: {
			items: [
				{ id: "excel", type: 'button', caption: '选择净值表文件', icon: 'w2ui-icon-plus' },
			],
			onClick: function (event) {
				switch (event.target) {
					case "excel":
						// JS安全策略拒绝获取文件路径，调用python窗口获取文件地址
						window.handler.mainSignal("grid2x1main", "excel", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid2x1preview: {
		name: "grid2x1preview",
		header: "识别结果",
		show: {
			header: true,
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarAdd: true,
			toolbarEdit: false,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true
		},
		columns: [
			{ field: "code", caption: "代码", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "holdings", caption: "持股数量", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "purchase_price", caption: "成本价", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "costs", caption: "总成本", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "cost2nav", caption: "成本占净值比例", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "market_price", caption: "收盘价", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "mv", caption: "市值", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "mv2nav", caption: "市值占净值比例", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "valuation", caption: "估值损益", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "status", caption: "交易状态", size: "10", sortable: true, searchable: true }
		],
		toolbar: {
			items: [
				{ type: "break" },
				{ id: "save", type: "button", caption: "确认导入", icon: "w2ui-icon-check" },
				{ type: "spacer" },
				{ type: "break" },
				{ id: "date_txt", type: "button", text: "口径日期", icon: "w2ui-icon-pencil" },
				{ type: "break" },
				{ id: "value_txt", type: "button", text: "单位净值", icon: "w2ui-icon-pencil" }
			],
			onClick: function (event) {
				switch (event.target) {
					case "w2ui-add":
						// JS安全策略拒绝获取文件路径，调用python窗口获取文件地址
						w2ui.grid2x1preview.add({ recid: w2ui.grid2x1preview.records.length + 1 });
						break;
					case "save":
						window.handler.mainSignal("grid2x1preview", "get", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						//func_project();
						break;
					case "date_txt":
						func_modify_date();
						break;
					case "value_txt":
						func_modify_value();
						break;
				}
			}
		}
	},
	grid2x2: {
		name: "grid2x2",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true
		},
		columns: [
			{ field: "project", caption: "项目", size: "10", sortable: true, searchable: true },
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "nav", caption: "单位净值", size: "10", sortable: true, render: "float:4" }
		]
	},
	grid2x3: {
		name: "grid2x3",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true
		},
		columns: [
			{ field: "project", caption: "项目", size: "10", sortable: true, searchable: true },
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "code", caption: "代码", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "holdings", caption: "持股数量", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "purchase_price", caption: "成本价", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "costs", caption: "总成本", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "cost2nav", caption: "成本占净值比例", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "market_price", caption: "收盘价", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "mv", caption: "市值", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "mv2nav", caption: "市值占净值比例", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "valuation", caption: "估值损益", size: "10", sortable: true, searchable: false, render: "float:2" },
			{ field: "status", caption: "交易状态", size: "10", sortable: true, searchable: true }
		]
	},
	grid3x2: {
		name: "grid3x2",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true
		},
		columns: [
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "name", caption: "经营机构", size: "10", sortable: true, searchable: true },
			{ field: "amount_total", caption: "总优先金额", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "amount_avg", caption: "平均优先金额", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "amount_max", caption: "最大优先金额", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "project_num", caption: "项目数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num_stop", caption: "破止损数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num_warn", caption: "破预警数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num", caption: "标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_st", caption: "ST标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_suspend", caption: "停牌标的数", size: "10", sortable: true, searchable: true, render: "int" }
		],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x2", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid3x3: {
		name: "grid3x3",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "project", caption: "项目", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "nid", caption: "编号", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "branch", caption: "经营机构", size: "10", sortable: true, searchable: true },
			{ field: "type", caption: "类型", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "f_code", caption: "审批编号", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "issue_date", caption: "发行日期", size: "10", sortable: true, hidden: true, searchable: true, render: "date" },
			{ field: "amount", caption: "金额", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "duration", caption: "期限", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "leverage_ratio", caption: "杠杆率", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "warning_line", caption: "预警线", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "stop_line", caption: "平仓线", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "stock_num", caption: "标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_st", caption: "ST标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_sup", caption: "停牌标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "nav_now", caption: "当期净值", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "nav_last", caption: "上期净值", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "nav_pct", caption: "净值变动", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "nav2stop", caption: "止损溢价", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "nav2warn", caption: "预警溢价", size: "10", sortable: true, searchable: true, render: "float:2" }
		],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x3", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid3x4: {
		name: "grid3x4",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "code", caption: "代码", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "project_num", caption: "项目数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num_20", caption: "成本超20项目数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "date_before_suspend", caption: "停牌前交易日", size: "10", sortable: true, searchable: true },
			{ field: "holdings", caption: "持股数量", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "holdings_to_total", caption: "占总股本比例", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "mv", caption: "市值", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "avg_turnover", caption: "平均换手率", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "days_to_settle", caption: "处置天数", size: "10", sortable: true, searchable: true, render: "float:2" }
		],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x4", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid3x5: {
		name: "grid3x5",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [
			{ field: "infodate", caption: "日期", size: "10", sortable: true, searchable: true, render: "date" },
			{ field: "nid", caption: "证件号", size: "10", sortable: true, searchable: true },
			{ field: "name", caption: "名称", size: "10", sortable: true, searchable: true },
			{ field: "amount_total", caption: "总金额", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "amount_avg", caption: "平均金额", size: "10", sortable: true, searchable: true, render: "float:2" },
			{ field: "branch_num", caption: "经营机构数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num", caption: "项目数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num_stop", caption: "破止损数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "project_num_warn", caption: "破预警数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num", caption: "标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_st", caption: "ST标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "stock_num_sup", caption: "停牌标的数", size: "10", sortable: true, searchable: true, render: "int" },
			{ field: "tp1_code", caption: "代码1", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "tp1_name", caption: "简称1", size: "10", sortable: true, searchable: true },
			{ field: "tp1_mv", caption: "市值1", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp1_pct", caption: "占比1", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp2_code", caption: "代码2", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "tp2_name", caption: "简称2", size: "10", sortable: true, searchable: true },
			{ field: "tp2_mv", caption: "市值2", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp2_pct", caption: "占比2", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp3_code", caption: "代码3", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "tp3_name", caption: "简称3", size: "10", sortable: true, searchable: true },
			{ field: "tp3_mv", caption: "市值3", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp3_pct", caption: "占比3", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp4_code", caption: "代码4", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "tp4_name", caption: "简称4", size: "10", sortable: true, searchable: true },
			{ field: "tp4_mv", caption: "市值4", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp4_pct", caption: "占比4", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp5_code", caption: "代码5", size: "10", sortable: true, hidden: true, searchable: true },
			{ field: "tp5_name", caption: "简称5", size: "10", sortable: true, searchable: true },
			{ field: "tp5_mv", caption: "市值5", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" },
			{ field: "tp5_pct", caption: "占比5", size: "10", sortable: true, hidden: true, searchable: true, render: "float:2" }
		],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x5", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid3x6: {
		name: "grid3x6",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x6", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	},
	grid3x7: {
		name: "grid3x7",
		show: {
			toolbar: true,
			toolbarReload: true,
			toolbarColumns: true,
			toolbarSearch: true,
			toolbarDelete: true,
			toolbarSave: false,
			lineNumbers: true,
			footer: true,
			selectColumn: true,
			expandColumn: true
		},
		columns: [],
		toolbar: {
			items: [
				{ type: "spacer" },
				{
					id: "date_stat", type: "button", text: "指定统计日期", icon: "w2ui-icon-pencil"
				},
				{ type: "html", html: '<div style="width: 15px;"></div>' }
			],
			onClick: function (event) {
				switch (event.target) {
					case "date_stat":
						window.handler.mainSignal("grid3x7", "getdate", "null", function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						break;
				}
			}
		}
	}
}
// 初始化布局
$("#layout").w2layout(config.layout);
//初始化标题栏
w2ui.layout.content('top', '<div style="width:470px;float:left;margin-left:0"><img src="./img/titlebar.png"></div><div style="width: 300px;float:right;margin-right:0px;padding-top:15px;"><p style="text-align:right;padding-right:15px">当前用户：<span id="user">北京分行</span></p></div>')
// 初始化侧边栏
w2ui.layout.content('left', $().w2sidebar(config.sidebar));
// 初始化首页
w2ui.layout.content('main', '<h1>此处显示报表</h1>');
// 未显示页面配置全部载入内存等待调用
//w2ui.layout.content('preview', $().w2grid(config.grid2x1preview));
$().w2grid(config.grid1x1);
$().w2grid(config.grid2x1main);
$().w2grid(config.grid2x1preview);
$().w2grid(config.grid2x2);
$().w2grid(config.grid2x3);
$().w2grid(config.grid3x1);
$().w2grid(config.grid3x2);
$().w2grid(config.grid3x3);
$().w2grid(config.grid3x4);
$().w2grid(config.grid3x5);
// $().w2grid(config.grid3x6);
// $().w2grid(config.grid3x7);

/* "enum"使用的json数据统一使用{id:"id@name", text"id@name"} */
function func_add() {
	if (!w2ui.formadd) {
		$().w2form({
			name: 'formadd',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div style="width:360px;float:left;margin-right:0"><div style="padding:3px;font-weight:700;color:#777">项目基本信息 <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:370px"><div class="w2ui-field w2ui-span4"><label>编号</label><div><input name="nid" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>名称</label><div><input name="name" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>经营机构</label><div><input name="branch" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>类型</label><div><input name="type" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>审批编号</label><div><input name="f_code" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>发行日期</label><div><input name="issue_date" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>金额</label><div><input name="amount" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>期限</label><div><input name="duration" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>杠杆率</label><div><input name="leverage_ratio" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>预警线</label><div><input name="warning_line" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>平仓线</label><div><input name="stop_line" type="text" style="width:100%" /></div></div></div></div><div style="width:360px;float:right;margin-left:0"><div style="padding:3px;font-weight:700;color:#777">差额补足人（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="guarantor" type="text" style="width:340px;height:75px;resize:none" /></div></div>' + /*<div style="padding:3px;font-weight:700;color:#777">投资顾问（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="adviser" type="text" style="width:340px;height:75px;resize:none" /></div></div><div style="padding:3px;font-weight:700;color:#777">次级客户（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="posterior" type="text" style="width:340px;height:75px;resize:none" /></div></div>*/ '</div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "nid", type: "text", required: true },
				{ field: "name", type: "text", required: true },
				{ field: "branch", type: "text", required: true },
				{ field: "type", type: "text", required: true },
				{ field: "f_code", type: "text", required: true },
				{ field: "issue_date", type: "date", required: true },
				{ field: "amount", type: "money", required: true },
				{ field: "duration", type: "int", required: true },
				{ field: "leverage_ratio", type: "float: 2", required: true },
				{ field: "warning_line", type: "float: 2", required: true },
				{ field: "stop_line", type: "float: 2", required: true },
				{
					field: "guarantor", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				}/*,
				{
					field: "adviser", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				},
				{
					field: "posterior", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				}*/
			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						var rec = '[[{"nid":"' + $("#nid").val() +
							'","name":"' + $("#name").val() +
							'","branch":"' + $("#branch").val() +
							'","type":"' + $("#type").val() +
							'","f_code":"' + $("#f_code").val() +
							'","issue_date":"' + $("#issue_date").val() +
							'","amount":' + $("#amount").val().replace(/,/g, "").replace(/¥/g, "") +
							',"duration":' + $("#duration").val().replace(/,/g, "") +
							',"leverage_ratio":' + $("#leverage_ratio").val() +
							',"warning_line":' + $("#warning_line").val() +
							',"stop_line":' + $("#stop_line").val() +
							'}],[';
						s = $("#guarantor").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}
						/*rec = rec.substr(0, rec.length - 1);
						rec += '],[';
						s = $("#adviser").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}
						rec = rec.substr(0, rec.length - 1);
						rec += '],[';
						s = $("#posterior").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}*/
						rec = rec.substr(0, rec.length - 1);
						rec += ']]';
						//传值到Python
						window.handler.mainSignal("grid1x1", "new", rec, function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '增加项目',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 750,
		height: 540,
		onToggle: function (event) {
			$(w2ui.formadd.box).hide();
			event.onComplete = function () {
				$(w2ui.formadd.box).show();
				w2ui.formadd.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formadd');
			}
		}
	})
}

function func_edit(rdata) {
	if (!w2ui.formedit) {
		$().w2form({
			name: 'formedit',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div style="width:360px;float:left;margin-right:0"><div style="padding:3px;font-weight:700;color:#777">项目基本信息 <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:370px"><div class="w2ui-field w2ui-span4"><label>编号<span style="color:red;font-weight:400">*</span></label><div><input name="nid" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>名称<span style="color:red;font-weight:400">*</span></label><div><input name="name" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>经营机构<span style="color:red;font-weight:400">*</span></label><div><input name="branch" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>类型<span style="color:red;font-weight:400">*</span></label><div><input name="type" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>审批编号<span style="color:red;font-weight:400">*</span></label><div><input name="f_code" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>发行日期<span style="color:red;font-weight:400">*</span></label><div><input name="issue_date" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>金额<span style="color:red;font-weight:400">*</span></label><div><input name="amount" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>期限<span style="color:red;font-weight:400">*</span></label><div><input name="duration" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>杠杆率<span style="color:red;font-weight:400">*</span></label><div><input name="leverage_ratio" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>预警线<span style="color:red;font-weight:400">*</span></label><div><input name="warning_line" type="text" style="width:100%" /></div></div><div class="w2ui-field w2ui-span4"><label>平仓线<span style="color:red;font-weight:400">*</span></label><div><input name="stop_line" type="text" style="width:100%" /></div></div></div></div><div style="width:360px;float:right;margin-left:0"><div style="padding:3px;font-weight:700;color:#777">差额补足人（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="guarantor" type="text" style="width:340px;height:75px;resize:none" /></div></div>' + /*<div style="padding:3px;font-weight:700;color:#777">投资顾问（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="adviser" type="text" style="width:340px;height:75px;resize:none" /></div></div><div style="padding:3px;font-weight:700;color:#777">次级客户（姓名@证件号） <span style="color:red;font-weight:400">*</span></div><div class="w2ui-group" style="height:102px"><div class="w2ui-field w2ui-span4"><input name="posterior" type="text" style="width:340px;height:75px;resize:none" /></div></div>*/ '</div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "nid", type: "text", required: false },
				{ field: "name", type: "text", required: false },
				{ field: "branch", type: "text", required: false },
				{ field: "type", type: "text", required: false },
				{ field: "f_code", type: "text", required: false },
				{ field: "issue_date", type: "date", required: false },
				{ field: "amount", type: "money", required: false },
				{ field: "duration", type: "int", required: false },
				{ field: "leverage_ratio", type: "float: 2", required: false },
				{ field: "warning_line", type: "float: 2", required: false },
				{ field: "stop_line", type: "float: 2", required: false },
				{
					field: "guarantor", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				}/*,
				{
					field: "adviser", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				},
				{
					field: "posterior", type: "enum", required: true,
					options: {
						openOnFocus: true,
						onNew: function (event) {
							$.extend(event.item);
						}
					}
				}*/
			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						var rec = '[[{"nid":"' + $("#nid").val() +
							'","name":"' + $("#name").val() +
							'","branch":"' + $("#branch").val() +
							'","type":"' + $("#type").val() +
							'","f_code":"' + $("#f_code").val() +
							'","issue_date":"' + $("#issue_date").val() +
							'","amount":' + $("#amount").val().replace(/,/g, "").replace(/¥/g, "") +
							',"duration":' + $("#duration").val().replace(/,/g, "") +
							',"leverage_ratio":' + $("#leverage_ratio").val() +
							',"warning_line":' + $("#warning_line").val() +
							',"stop_line":' + $("#stop_line").val() +
							'}],[';
						s = $("#guarantor").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}
						/*rec = rec.substr(0, rec.length - 1);
						rec += '],[';
						s = $("#adviser").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}
						rec = rec.substr(0, rec.length - 1);
						rec += '],[';
						s = $("#posterior").data("selected");
						for (var i in s) {
							rec += '{"nid":"' + s[i].text.split("@")[1] +
								'","name":"' + s[i].text.split("@")[0] +
								'"},'
						}*/
						rec = rec.substr(0, rec.length - 1);
						rec += ']]';
						alert(rec);
						//传值到Python
						window.handler.mainSignal("grid1x1", "edit", JSON.stringify(rec), function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '编辑项目',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 750,
		height: 540,
		onToggle: function (event) {
			$(w2ui.formedit.box).hide();
			event.onComplete = function () {
				$(w2ui.formedit.box).show();
				w2ui.formedit.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formedit');
				rdata = rdata.replace("[[", "");
				rdata = rdata.replace("]]", "");
				//alert(rdata);
				alert(rdata.split("],[")[0]);
				//alert(rdata.split("],[")[1]);
				var proj = JSON.parse(rdata.split("],[")[0]);
				//var guar = JSON.parse(rdata.split("],[")[1]);
				$("#nid").val(JSON.stringify(proj["nid"]).replace('"', '').replace('"', ''));
				$("#name").val(JSON.stringify(proj["name"]).replace('"', '').replace('"', ''));
				$("#branch").val(JSON.stringify(proj["branch"]).replace('"', '').replace('"', ''));
				$("#type").val(JSON.stringify(proj["type"]).replace('"', '').replace('"', ''));
				$("#f_code").val(JSON.stringify(proj["f_code"]).replace('"', '').replace('"', ''));
				$("#issue_date").val(JSON.stringify(proj["issue_date"]).replace('"', '').replace('"', ''));
				$("#amount").val(JSON.stringify(proj["amount"]).replace('"', '').replace('"', ''));
				$("#duration").val(JSON.stringify(proj["duration"]).replace('"', '').replace('"', ''));
				$("#leverage_ratio").val(JSON.stringify(proj["leverage_ratio"]).replace('"', '').replace('"', ''));
				$("#warning_line").val(JSON.stringify(proj["warning_line"]).replace('"', '').replace('"', ''));
				$("#stop_line").val(JSON.stringify(proj["stop_line"]).replace('"', '').replace('"', ''));
				// s = "";
				// for (key in guar) {
				// 	s += '{"id":"' + guar[key].name + '@' + guar[key].nid + '","text":"' + guar[key].name + '@' + guar[key].nid + '"},'
				// }
				// s = s.substr(0, s.length - 1);
				// s = $("#guarantor").data("selected", JSON.parse(s)).change();;
			}
		}
	})
}

function func_modify_date() {
	if (!w2ui.formmodifydate) {
		$().w2form({
			name: 'formmodifydate',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>口径日期</label><div><input name="date" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date", type: "date", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						w2ui["grid2x1preview"].toolbar.set("date_txt", { text: "口径日期：" + $("#date").w2field().get() });
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '修改口径日期',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formmodifydate.box).hide();
			event.onComplete = function () {
				$(w2ui.formmodifydate.box).show();
				w2ui.formmodifydate.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formmodifydate');
				text = (w2ui["grid2x1preview"].toolbar.get("date_txt"))["text"];
				if (text == "口径日期") {
					w2alert("未定义口径日期！");
				}
				else {
					$("#date").w2field().set(text.replace("口径日期：", ""));
				}
			}
		}
	})
}

function func_modify_value() {
	if (!w2ui.formmodifyvalue) {
		$().w2form({
			name: 'formmodifyvalue',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>单位净值</label><div><input name="value" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "value", type: "float", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						w2ui["grid2x1preview"].toolbar.set("value_txt", { text: "单位净值：" + $("#value").w2field().get() });
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '修改单位净值',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formmodifyvalue.box).hide();
			event.onComplete = function () {
				$(w2ui.formmodifyvalue.box).show();
				w2ui.formmodifyvalue.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formmodifyvalue');
				text = (w2ui["grid2x1preview"].toolbar.get("value_txt"))["text"];
				if (text == "单位净值") {
					w2alert("未定义单位净值！");
				}
				else {
					$("#value").w2field().set(text.replace("单位净值：", "").replace(/,/g, ""));
				}
			}
		}
	})
}

function func_project(project_list) {
	alert(project_list)
	if (!w2ui.formproject) {
		$().w2form({
			name: 'formproject',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>口径日期</label><div><input name="date" type="text" style="width:400px" disabled="disabled" /></div><label>单位净值</label><div><input name="value" type="text" style="width:400px" disabled="disabled" /></div><label>项目名称</label><div><input name="project" type="list" style="width:400px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">导入</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date", type: "date", required: false },
				{ field: "value", type: "float", required: false },
				{ field: "project", type: "list", required: true }
			],
			actions: {
				"save": function () {
					if (date_txt == "口径日期" || value_txt == "单位净值") {
						w2alert("未定义口径日期或单位净值！");
					}
					else {
						if (this.validate() == false) {
							// 项目编号名称、口径日期、单位净值、所有记录
							text = '[[{"nid":"' + $("#project").w2field().get()["id"] +
								'","name":"' + $("#project").w2field().get()["text"] +
								'"}],[{"date":"' + $("#date").w2field().get() +
								'"}],[{"value":' + $("#value").w2field().get() +
								'}],[';
							currentrecid = 0;
							while (w2ui["grid2x1preview"].nextRow(currentrecid - 1) != null) {
								var i = 0;
								text += '{"code":"' + w2ui["grid2x1preview"].getCellValue(currentrecid, 0) +
									'","name":"' + w2ui["grid2x1preview"].getCellValue(currentrecid, 1) +
									'","holdings":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 2) +
									',"purchase_price":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 3) +
									',"costs":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 4) +
									',"cost2nav":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 5) +
									',"market_price":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 6) +
									',"mv":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 7) +
									',"mv2nav":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 8) +
									',"valuation":' + w2ui["grid2x1preview"].getCellValue(currentrecid, 9) +
									',"status":"' + w2ui["grid2x1preview"].getCellValue(currentrecid, 10) +
									'"},'
								currentrecid++;
							}
							text = text.substr(0, text.length - 1);
							text += "]]";
							window.handler.mainSignal("grid2x1preview", "new", text, function (result) {
								if (result == false) {
									w2alert("操作失败！");
								} else {
									w2alert("操作成功！")
								}
							});
							this.clear();
							w2popup.close();
						}
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '请确认项目信息',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 600,
		height: 240,
		onToggle: function (event) {
			$(w2ui.formproject.box).hide();
			event.onComplete = function () {
				$(w2ui.formproject.box).show();
				w2ui.formproject.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formproject');
				date_txt = (w2ui["grid2x1preview"].toolbar.get("date_txt"))["text"];
				value_txt = (w2ui["grid2x1preview"].toolbar.get("value_txt"))["text"];
				if (date_txt == "口径日期" || value_txt == "单位净值") {
					w2alert("未定义口径日期或单位净值！");
				}
				else {
					$("#date").w2field().set(date_txt.replace("口径日期：", ""));
					$("#value").w2field().set(value_txt.replace("单位净值：", "").replace(/,/g, ""));
					// project_list = '[{ "id": "项目编号1", "text": "项目名称1" }, { "id": "项目编号2", "text": "项目名称2" }]';
					$("#project").w2field("list", { items: JSON.parse(project_list) });
				}
			}
		}
	})
}

function setSidebarState(grid_name) {
	if (grid_name == "function0" || grid_name == "function1" || grid_name == "function2" || grid_name == "function3") {
		w2ui["sidebar"].unselect(grid_name);
		w2ui["sidebar"].select(cur_sidebar);
	}
	else {
		cur_sidebar = grid_name;
	}
}

function func_stat() {
	if (!w2ui.formstat) {
		$().w2form({
			name: 'formstat',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>选择日期</label><div><input name="date_stat_input" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">下一步：选择外部数据文件</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date_stat_input", type: "date", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						window.handler.mainSignal("func_stat", "go", $("#date_stat_input").val(), function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '计算统计表',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formstat.box).hide();
			event.onComplete = function () {
				$(w2ui.formstat.box).show();
				w2ui.formstat.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formstat');

			}
		}
	})
}

function func_export(date_list) {
	if (!w2ui.formexport) {
		$().w2form({
			name: 'formexport',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>选择日期</label><div><input name="date_export_input" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">下一步：选择数据文件</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date_export_input", type: "list", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						window.handler.mainSignal("func_export", "new", $("#date_export_input").val(), function (result) {
							if (result == false) {
								w2alert("Cannot do it.");
							} else {
								w2alert("导出成功！");
							}
						});
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '导出数据库',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formexport.box).hide();
			event.onComplete = function () {
				$(w2ui.formexport.box).show();
				w2ui.formexport.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formexport');
				//date_json = "[";
				//for (var i in date_list) {
				//	date_json += '{"id":"' + i + '","text":"' + i + '"},';
				//}
				//date_json = date_json.substr(0, date_json.length - 1);
				//date_json += ']';
				$("#date_export_input").w2field("list", { items: JSON.parse(date_list) });
			}
		}
	})
}

function func_import() {
	if (!w2ui.formimport) {
		$().w2form({
			name: 'formimport',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>选择日期</label><div><input name="date_import_input" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date_import_input", type: "date", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {

						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '导入数据库',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formimport.box).hide();
			event.onComplete = function () {
				$(w2ui.formimport.box).show();
				w2ui.formimport.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formimport');
			}
		}
	})
}

function date_stat(grid_name, date_list) {
	if (!w2ui.formdatestat) {
		$().w2form({
			name: 'formdatestat',
			style: 'border: 0px; background-color: transparent;',
			formHTML: '<div class="w2ui-page page-0"><div class="w2ui-field"><label>选择日期</label><div><input name="date_stat_input" type="text" style="width:210px" /></div></div></div><div class="w2ui-buttons"><button class="w2ui-btn" name="save">保存</button> <button class="w2ui-btn" name="cancel">取消</button></div>',
			fields: [
				{ field: "date_stat_input", type: "list", required: true }

			],
			actions: {
				"save": function () {
					if (this.validate() == false) {
						w2ui["grid3x2"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						w2ui["grid3x3"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						w2ui["grid3x4"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						w2ui["grid3x5"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						//w2ui["grid3x6"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						//w2ui["grid3x7"].toolbar.set("date_stat", { text: "统计日期：" + $("#date_stat_input").w2field().get() });
						window.handler.mainSignal(grid_name, "setdate", $("#date_stat_input").w2field().get(), function (result) {
							if (result == false) {
								w2alert("操作失败！");
							} else {
								w2alert("操作成功！")
							}
						});
						this.clear();
						w2popup.close();
					}
				},
				"cancel": function () {
					this.clear();
					w2popup.close();
				}
			}
		})
	}
	$().w2popup('open', {
		title: '设置统计时间',
		body: '<div id="form" style="width: 100%; height: 100%;"></div>',
		style: 'padding: 15px 0px 0px 0px',
		width: 450,
		height: 180,
		onToggle: function (event) {
			$(w2ui.formdatestat.box).hide();
			event.onComplete = function () {
				$(w2ui.formdatestat.box).show();
				w2ui.formdatestat.resize();
			}
		},
		onOpen: function (event) {
			event.onComplete = function () {
				$('#w2ui-popup #form').w2render('formdatestat');
				$("#date_stat_input").w2field("list", { items: JSON.parse(date_list) });
			}
		}
	})
}
