#!/bin/bash

for i in $(ls *csv);
do
    python3 plot.py $i&
done
