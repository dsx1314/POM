import xlrd
from xlutils.copy import copy

from common_object.读取txt import read_txt
def remove():
    rb = xlrd.open_workbook('D:\\POM\\data\\车辆导入模板 (6).xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(1,12):
        ws.write(i,0,read_txt()[i-1])
    wb.save('D:\\POM\\data\\车辆导入模板 (6).xls')
    # print('success-2')

if __name__ == '__main__':
    remove()