#!/bin/bash

# txt copy
echo "*** copy ***"
CLIENT_DATATABLE_PATH=../../client/Assets/Game/DataTables/
rm -rf "$CLIENT_DATATABLE_PATH"
mkdir "$CLIENT_DATATABLE_PATH"
cp -R ./TxtConfigs/* "$CLIENT_DATATABLE_PATH"
