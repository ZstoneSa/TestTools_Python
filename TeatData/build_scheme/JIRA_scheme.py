import xlsxwriter
from jira import JIRA


def allofbug():
    '''登录jira'''
    jira = JIRA(server='http://jira.quickcan.com', basic_auth=('zhengshi', 'Zs17600972766'))

    '''获取项目中面板，存入数组'''
    list_num = []

    '''循环遍历每个面板的BUG数，存入数组'''
    for i in affectedVersion:
        allOfBug = 'affectedVersion = ' + i
        issues = jira.search_issues(allOfBug, fields='', maxResults=10000)
        bugNum = len(issues)
        list_num.append(bugNum)

    # 创建一个excel
    workbook = xlsxwriter.Workbook("numberodBUGs.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet()
    # worksheet = workbook.add_worksheet("bug_analysis")

    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})

    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    headings = ['面板', 'BUG总数']

    # 写入表头
    worksheet.write_row('A1', headings, bold)

    # 写入数据
    worksheet.write_column('A2', affectedVersion)
    worksheet.write_column('B2', list_num)
    # worksheet.write_column('C2', data[2])

    # --------2、生成图表并插入到excel---------------
    # 创建一个条形图(line chart)
    chart_col = workbook.add_chart({'type': 'line'})

    # 配置第一个系列数据
    chart_col.add_series({
        # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
        # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
    })

    # 配置第二个系列数据
    # chart_col.add_series({
    #     'name': '=Sheet1!$C$1',
    #     'categories':  '=Sheet1!$A$2:$A$7',
    #     'values':   '=Sheet1!$C$2:$C$7',
    #     'line': {'color': 'yellow'},
    # })

    # 配置第二个系列数据(用了另一种语法)
    # chart_col.add_series({
    #     'name': ['Sheet1', 0, 2],
    #     'categories': ['Sheet1', 1, 0, 6, 0],
    #     'values': ['Sheet1', 1, 2, 6, 2],
    #     'line': {'color': 'yellow'},
    # })

    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': 'BUG总数'})
    chart_col.set_x_axis({'name': '版本（version）'})
    chart_col.set_y_axis({'name': '总数 (num)'})

    # 设置图表的风格
    chart_col.set_style(1)

    # 把图表插入到worksheet并设置偏移
    worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

    workbook.close()


def issueanlysis():
    '''  登录jira  '''
    jira = JIRA(server='http://jira.quickcan.com', basic_auth=('zhengshi', 'Zs15825413766'))

    '''获取项目中面板，存入数组'''
    list_avoid = []
    list_unclear = []
    list_newissue = []


    '''循环遍历每个面板的BUG数，存入数组'''
    for i in affectedVersion:
        allOfBug = 'affectedVersion = ' + i + ' AND 缺陷类型 = 开发中可避免的问题'
        issues = jira.search_issues(allOfBug, fields='', maxResults=10000)
        bugNum = len(issues)
        list_avoid.append(bugNum)

    for i in affectedVersion:
        allOfBug = 'affectedVersion = ' + i + ' AND 缺陷类型 = "功能需求不明确/需求变动"'
        issues = jira.search_issues(allOfBug, fields='', maxResults=10000)
        bugNum = len(issues)
        list_unclear.append(bugNum)

    for i in affectedVersion:
        allOfBug = 'affectedVersion = ' + i + ' AND 缺陷类型 = 修复引入新问题'
        issues = jira.search_issues(allOfBug, fields='', maxResults=10000)
        bugNum = len(issues)
        list_newissue.append(bugNum)

    # 创建一个excel
    workbook = xlsxwriter.Workbook("IssueAnalysis.xlsx")
    # 创建一个sheet
    worksheet = workbook.add_worksheet()
    # worksheet = workbook.add_worksheet("bug_analysis")

    # 自定义样式，加粗
    bold = workbook.add_format({'bold': 1})

    # --------1、准备数据并写入excel---------------
    # 向excel中写入数据，建立图标时要用到
    headings = ['面板', '开发中可避免的问题', '功能需求不明确/需求变动', '修复引入新问题']

    # 写入表头
    worksheet.write_row('A1', headings, bold)

    # 写入数据
    worksheet.write_column('A2', affectedVersion)
    worksheet.write_column('B2', list_avoid)
    worksheet.write_column('C2', list_unclear)
    worksheet.write_column('D2', list_newissue)

    # --------2、生成图表并插入到excel---------------
    # 创建一个条形图(line chart)
    chart_col = workbook.add_chart({'type': 'line'})

    # 配置第一个系列数据
    chart_col.add_series({
        # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
        # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
    })

    # 配置第二个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$C$1',
        'categories':  '=Sheet1!$A$2:$A$7',
        'values':   '=Sheet1!$C$2:$C$7',
        'line': {'color': 'yellow'},
    })

    # 配置第二个系列数据
    chart_col.add_series({
        'name': '=Sheet1!$D$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$D$2:$D$7',
        'line': {'color': 'blue'},
    })

    # 配置第二个系列数据(用了另一种语法)
    # chart_col.add_series({
    #     'name': ['Sheet1', 0, 2],
    #     'categories': ['Sheet1', 1, 0, 6, 0],
    #     'values': ['Sheet1', 1, 2, 6, 2],
    #     'line': {'color': 'yellow'},
    # })

    # 设置图表的title 和 x，y轴信息
    chart_col.set_title({'name': '问题统计'})
    chart_col.set_x_axis({'name': '版本（version）'})
    chart_col.set_y_axis({'name': '总数 (num)'})

    # 设置图表的风格
    chart_col.set_style(10)

    # 把图表插入到worksheet并设置偏移
    worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

    workbook.close()


if __name__ == '__main__':
    print("------------- 请将版本号以以下的形式输入输入框 ------------- \n(例如：付费V5.5,付费V5.6,付费V5.7,付费V5.8,付费V5.9,付费V6.0) \n " )
    note = input("---> 请输入多个版本号 :")
    affectedVersion = note.split(',')
    print(affectedVersion)
    print(type(affectedVersion))
    if isinstance(affectedVersion, list):
        print('生成图表中，请稍候.....')
        allofbug()
        issueanalysis()
        print('图表已生成，请检查当前文件夹.xlsx文件两种图表是否正确')
    else:
        print('输入有误')