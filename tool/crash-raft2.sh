#!/bin/bash
dqlite-benchmark --db 172.24.2.2:9002 --join 172.24.2.1:9001 & 
sleep 1
pkill dqlite-benchmark