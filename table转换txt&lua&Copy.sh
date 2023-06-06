#!/bin/bash

rm -rf ./TxtConfigs
mkdir ./TxtConfigs

echo "*** gen txt ***"

mono ./ExcelTool/TableToClient.exe ../ConfigTable/ ./TxtConfigs
sh ./CopyConfigs.sh
read -p "Press enter to continue"
