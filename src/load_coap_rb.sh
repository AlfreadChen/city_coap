#!/bin/bash
source ../config/env.sh

#real-time run
 BegTime=$(date -d"2018-10-05" '+%s')
 EndTime=$(date -d"2018-10-15" '+%s')
 #EndTime=$(date -d"2017-12-01" '+%s')
 while [ $BegTime -le $EndTime ]; do
       YYMMDD=$(date -d@${BegTime} +%Y%m%d)
       python -W ignore real.py -t $YYMMDD
       let BegTime=BegTime+24*3600
 done

