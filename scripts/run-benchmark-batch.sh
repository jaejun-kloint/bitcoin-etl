#!/bin/bash

START=837027
BATCH_NUM=100
WORKER=5
ENRICH=False
for SIZE in "1d" "1w" "1m"
do
    for ENRICH in "False" "True"
    do
        for BATCH_NUM in 50 100 150
        do
            for WORKER in 5 10 15 20
            do  
                NEWDIR=./experiments/s${SIZE}_b${BATCH_NUM}_w${WORKER}_${ENRICH}
                echo "Start new exp: ${NEWDIR}"
                
                if [ $SIZE == "1d" ]; then
                    START=837027
                elif [ $SIZE == "1m" ]; then
                    START=836004
                else
                    START=832602
                fi 
                
                mkdir -p $NEWDIR
                SECONDS=0
                python3 bitcoinetl.py export_all -s ${START} -e 837164 -p http://bitcoin:kloint_bitcoin@10.0.3.100:8332 -o ${NEWDIR} -b ${BATCH_NUM} -w ${WORKER} --enrich ${ENRICH}
                duration=$SECONDS
                echo "$((duration / 60)) minutes and $((duration % 60)) seconds elapsed." > ${NEWDIR}/result.txt

                echo "${SIZE},${BATCH_NUM},${WORKER},${ENRICH},${duration}" >> ./final_result_$(date +%m-%d-%y).csv
                echo "Rest for 1 minute."    
                sleep 60
            done
        done
    done
done