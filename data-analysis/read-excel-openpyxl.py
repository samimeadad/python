from openpyxl import load_workbook

dataPath = "D:\Training\Big-Data-Data-Analytics-Data-Science-Pondit\Excel Files\CustomerMaster.xlsx"

wb = load_workbook(dataPath)

print(wb)