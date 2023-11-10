from openpyxl import load_workbook

dataPath = "/Users/sami/Downloads/book1.xlsx";

wb = load_workbook(dataPath);

print(wb);