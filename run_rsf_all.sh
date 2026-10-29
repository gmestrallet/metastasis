#!/bin/bash

filename=$1
st=$2
ti=$3
name=$4
i1=$5
i2=$6

for ((i=i1; i<=i2; i++));
do
	#echo $i
	sbatch run_RSF_model.sbatch $1 $2 $3 $4 $i
done

