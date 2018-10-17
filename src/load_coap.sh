#!/bin/bash
source ../config/env.sh

#real-time run
YYMMDD=$(date +%Y%m%d)
YYMMDD=20180915
python -W ignore real.py -t $YYMMDD
