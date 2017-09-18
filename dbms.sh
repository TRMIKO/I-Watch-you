#!/bin/bash

systemctl status mysql.service | grep running 2>/dev/null >/dev/null

if [ $? -ne 0 ]; then
	python  /home/arturo/Documentos/iwy/iwy_warn.py
fi