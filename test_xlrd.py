import xlrd

def read_excel():
    excel_content_list = []
    wb = xlrd.open_workbook('file/模板.xls')
    sheet = wb.sheet_by_index(0)
    print(f"表单名字：{sheet.name}, 表单行数：{sheet.nrows}, 表单列数：{sheet.ncols}")
    print(f"获取第二行内容：{sheet.row_values(1)}")
    print(f"获取第三列内容：{sheet.row_values(2)}")

    for row in range(sheet.nrows):
        row_content_dict = {"L1":'', "L2":'', "Question":'', "Answer":'', "Similar":''}
        row_content_dict['L1'] = sheet.cell_value(row,0)
        row_content_dict['L2'] = sheet.cell_value(row, 1)
        row_content_dict['Question'] = sheet.cell_value(row, 2)
        row_content_dict['Answer'] = sheet.cell_value(row, 4)
        row_content_dict['Similar'] = sheet.cell_value(row, 6)
        excel_content_list.append(row_content_dict)
    print(f"Total rows: {len(excel_content_list)}")
    return excel_content_list





if __name__ == '__main__':
    print(read_excel())