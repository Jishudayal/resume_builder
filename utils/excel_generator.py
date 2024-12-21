import openpyxl

def generate_excel(data):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Resume Data"
    ws.append(["Field", "Value"])
    for key, value in data.items():
        ws.append([key, value])
    return wb
