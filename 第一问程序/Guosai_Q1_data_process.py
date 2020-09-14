import xlrd

data = xlrd.open_workbook('D:\Desktop\国赛\CUMCM2020Probelms\C\附件1：123家有信贷记录企业的相关数据.xlsx')
table = data.sheet_by_name('销项发票信息')
print("总行数：" + str(table.nrows))
print("总列数：" + str(table.ncols))
col_1 = table.col_values(0)  # 企业代号
col_10 = table.col_values(10)  # 有效发票的金额
col_11 = table.col_values(11)  # 有效发票的税额
col_3 = table.col_values(2)  # 日期

# 分公司统计进项销项
sum_of_col = 0
amount = []
for i in range(1, 124):
    for j in range(table.nrows):
        if col_1[j] == 'E' + str(i):
            sum_of_col += col_10[j]
    # print('企业E' + str(i) + '销项' + '的有效发票的金额为：' + str(sum_of_col))
    amount.append(sum_of_col)
    sum_of_col = 0

# 分公司统计进项销项天数
sum_of_date = 0
date = []
for j in range(1, table.nrows):
    col_3[j] = xlrd.xldate_as_tuple(int(col_3[j]), 0)
for i in range(1, 124):
    for j in range(0, table.nrows):
        if col_1[j] == 'E' + str(i):  # 确定某个企业
            if col_3[j][0] != col_3[j - 1][0] or col_3[j][1] != col_3[j - 1][1]:
                sum_of_date += 1
    print('企业'+str(i)+'的月数为：'+str(sum_of_date))
    date.append(sum_of_date)
    sum_of_date = 0

for i in range(0, 123):
    aver = []
    aver.append(amount[i]/date[i])
    print(aver)
    # '企业'+str(i+1)+'的月均销项金额为：'
# 分公司统计进项销项个数
# sum_of_col = 0
# for i in range(1, 124):
#     for j in range(table.nrows):
#         if col_1[j] == 'E' + str(i):
#             sum_of_col += 1
#     print('企业E' + str(i) + '进项' + '的有效发票的个数为：' + str(sum_of_col))
#     sum_of_col = 0

# print(col_3)
# print(type(col_3))
# # for i in range()
# print(len(col_3))
