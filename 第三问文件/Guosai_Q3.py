import xlrd
import xlwt


data = xlrd.open_workbook('D:\Desktop\国赛\第二问文件\第三问按规模增益.xlsx')
data2 = xlrd.open_workbook('D:\QQ下载\附件2：302家无信贷记录企业的相关数据.xlsx')
table = data.sheet_by_name('Sheet1')
table2 = data2.sheet_by_name('企业信息')
# print("总行数：" + str(table.nrows))
# print("总列数：" + str(table.ncols))
col_1 = table.col_values(0)  # 企业代号
col_3 = table.col_values(3)  # 销项的金额加税额
col_5 = table.col_values(5)  # 违约率
individual_A = table2.col_values(2)  # individual_A[1:53]
service_A = table2.col_values(3)  # service_A[1:197]
sale_B = table2.col_values(4)  # sale_B[1:12]
commercial_C = table2.col_values(5)  # commercial_C[1:6]
tech = table2.col_values(6)  # tech[1:12]
medical = table2.col_values(7)  # medical[1:7]
计算规模
for i in range(302):
    if col_1[i] in individual_A[1:53] or col_1[i] in service_A[1:197]:
        col_3[i] = col_3[i] * (1 - 0.256)
    elif col_1[i] in sale_B[1:12]:
        col_3[i] = col_3[i] * (1 - 0.128)
    elif col_1[i] in commercial_C[1:6]:
        col_3[i] = col_3[i] * (1 - 0.064)
    elif col_1[i] in medical[1:7]:
        col_3[i] = col_3[i] * (1 + 0.3)
sum_of_money = sum(col_3)
for i in range(302):
    col_3[i] = col_3[i] / sum_of_money
    print(col_3[i])

# 计算违约率
for i in range(302):
    if col_1[i] in individual_A[1:53] or col_1[i] in service_A[1:197]:
        col_5[i] = col_5[i] * 10
    elif col_1[i] in sale_B[1:12]:
        col_5[i] = col_5[i] * 4
    elif col_1[i] in commercial_C[1:6]:
        col_5[i] = col_5[i] * 2
    elif col_1[i] in medical[1:7]:
        col_5[i] = col_5[i] * 0.7
for i in range(302):
    print(col_5[i])
