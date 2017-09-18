#!/bin/bash

systemctl status mysql.service | grep running 2>/dev/null >/dev/null

if [ $? -eq 0 ]; then
	python  /home/arturo/Documentos/iwy/iwy_ok.py
else
	python  /home/arturo/Documentos/iwy/iwy_warn.py
fi