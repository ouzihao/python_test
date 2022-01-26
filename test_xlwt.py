import xlwt

def write_excel():
    my_wb = xlwt.Workbook()
    my_sheet = my_wb.add_sheet("Test_Sheet")
    my_style = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    my_sheet.write(1, 2, 1234.56, my_style)
    my_sheet.write(2, 0, 1)  # 写入A3，数值等于1
    my_sheet.write(2, 1, 1)  # 写入B3，数值等于1
    my_sheet.write(2, 2, xlwt.Formula("A3+B3"))  # 写入C3，数值等于2（A3+B3）

    path = 'file/生成的Excel_XLWT.xls'
    my_wb.save(path)
    print(f"save path: {path}")



if __name__ == '__main__':
    write_excel()