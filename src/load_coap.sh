#!/bin/bash
export PATH=/p200/home/model/xiaolh/conda/bin:$PATH
#real-time run
YYMMDD=$(date +%Y%m%d)
YYMMDD=20180830
python -W ignore real.py -t $YYMMDD
