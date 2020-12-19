import xlwt
import datetime
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('Worksheet')
# 写入excel参数对应 行, 列, 值
worksheet.write(0, 0, label='测试')
# 设置单元格宽度
worksheet.col(0).width = 3333

# 设置单元格高度
tall_style = xlwt.easyxf('font:height 520;')
worksheet.row(0).set_style(tall_style)

# 设置对齐方式
alignment = xlwt.Alignment()  # Create Alignment
# May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER
# May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()  # Create Style
style.alignment = alignment  # Add Alignment to Style
worksheet.write(2, 0, '居中', style)

# 写入带颜色背景的数据
pattern = xlwt.Pattern()  # Create the Pattern
# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
style = xlwt.XFStyle()  # Create the Pattern
style.pattern = pattern  # Add Pattern to Style
worksheet.write(0, 1, '颜色', style)

# 写入日期
style = xlwt.XFStyle()
# Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
style.num_format_str = 'M/D/YY'
worksheet.write(0, 2, datetime.datetime.now(), style)

# 写入公式
worksheet.write(0, 3, 5)  # Outputs 5
worksheet.write(0, 4, 2)  # Outputs 2
# Should output "10" (A1[5] * A2[2])
worksheet.write(1, 3, xlwt.Formula('D1*E1'))
# Should output "7" (A1[5] + A2[2])
worksheet.write(1, 4, xlwt.Formula('SUM(D1,E1)'))

# 写入超链接
worksheet.write(1, 0, xlwt.Formula('HYPERLINK("http://www.baidu.com";"百度一下")'))
# 保存
workbook.save('Excel_test.xls')
