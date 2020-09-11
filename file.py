import openpyxl as xl


from openpyxl.chart import BarChart, Reference


def process_workbook(filename):
	wb = xl.loadworkbook(filename)
	sheet = wb['Sheet1']
	#cell = sheet['a1']
	cell = sheet.cell(1, 1)
	#print(cell.value)
	#print(sheet.max_row)
