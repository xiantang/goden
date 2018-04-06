import xlwt
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet=book.add_sheet('goden')
sheet.write(1,0,'sdfdsdfvdfgvdf') #第一个参数代表行 第二个代表列
book.save(r'C:\Users\战神皮皮迪\Documents\GitHub\goden\goden\test1.xls')