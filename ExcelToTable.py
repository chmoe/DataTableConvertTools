import os
import sys
import pandas as pd
import numpy as np

def write_sheet(tab, name, write_path):
    sb = []
    index = 0
    for row in tab.itertuples():
        # 无ID的行不读
        # if index == 0:
        #     index += 1
        #     continue
        if index > 4 and pd.isnull(row[1]):
            continue
        sb.append('\t'.join(str(cell) for cell in row[1:]))
        sb.append('\r\n')
        index += 1

    # 写文件
    with open(os.path.join(write_path, f"{name}.table"), "w", encoding="gb2312") as file:
        file.writelines(sb)

def write_excel(path, write_path):
    if not os.path.exists(path):
        return

    # 读取Excel文件
    excel = pd.ExcelFile(path)

    for sheet_name in excel.sheet_names:
        name = sheet_name.replace("$", "")
        if name.lower().startswith("sheet"):
            continue
        if name.lower().startswith("0"):
            continue
        tab = excel.parse(sheet_name, header=None)
        tab = tab.replace(np.nan, '')
        if len(tab.index) < 1:
            continue
        write_sheet(tab, name, write_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <excel_file_path> <write_path>")
        return

    excel_file_path = sys.argv[1]
    write_path = sys.argv[2]

    if not excel_file_path.endswith(".xls"):
        print("Invalid Excel file format. Only .xls files are supported.")
        return

    write_excel(excel_file_path, write_path)
    print(f"{excel_file_path} 写入TXT成功！！")

if __name__ == "__main__":
    main()
