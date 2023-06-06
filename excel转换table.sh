#!/bin/bash

cd configs
find . -name '*.xls' -type f -print0 | while IFS= read -r -d '' file; do
  base=$(basename "$file" .xls)
  python ../ExcelTool/ExcelToTable.py "$file" ../ConfigTable
done

read -p "Press any key to continue..."
