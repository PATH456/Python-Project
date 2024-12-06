import xlrd
import csv

workbook = xlrd.open_workbook("raw_text.xls")
sheet = workbook.sheet_by_name("Sheet1")
processed_data = []
raw_headers = [sheet.cell_value(0, col_idx) for col_idx in range(sheet.ncols)]

header_mapping = {
    "Category": "Category",
    "Function": "Name",
    "Description": "Description",
    "New?": "Status",
    "Help Topic": "Code",
    "Help": "Sum_Code"
}

required_headers = []
for header in raw_headers:
    required_headers.append(header_mapping.get(header.strip()))


for row_idx in range(1, sheet.nrows):
    row = sheet.row(row_idx)
    category = row[0].value
    name = row[1].value
    description = row[2].value
    status = row[3].value
    code = row[4].value
    sum_code = sum(int(digit) for digit in str(code) if digit.isdigit())
    if "Returns" in description:
        processed_data.append([category, name, description, status, code, sum_code])

with open("processed_data.csv", "w", newline= "") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(required_headers)
    csv_writer.writerows(processed_data)





























