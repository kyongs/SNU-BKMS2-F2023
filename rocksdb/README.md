# How to Install RocksDB and DBBench

## Overview

This week you will install RocksDB and run DB_Bench on your own system.

Follow the guide below. If you have any questions, don't hesitate to contact me via email. 

> NOTE: This lab is based on the Linux environment. If you don't have a Linux machine, use [VirturalBox](https://www.virtualbox.org/). (Recommended: Ubuntu 18.04)

## Instructions

### 1. Install pre-requisites:

**Linux - Ubuntu**
- `$ sudo apt-get update`
- Upgrade gcc version at least 4.8
- gflags: `sudo apt-get install libgflags-dev`
  If this doesn't work, here's a nice tutorial: [tutorial link](http://askubuntu.com/questions/312173/installing-gflags-12-04)
- snappy: `sudo apt-get install libsnappy-dev`
- zlib: `sudo apt-get install zlib1g-dev`
- bzip2: `sudo apt-get install libbz2-dev`
- lz4: `sudo apt-get install liblz4-dev`
- zstandard: `sudo apt-get install libzstd-dev`
- java: `sudo apt install default-jdk
sudo apt install default-jre`

**[Other platform](https://github.com/facebook/rocksdb/blob/master/INSTALL.md#supported-platforms)**

### 2. Build and install RocksDB
- Change the number 8 to the number of CPU cores. (Change the number of cores that matches your computer's(or vm's) specifications.)
```bash
$ git clone https://github.com/facebook/rocksdb
$ cd rocksdb
$ make static_lib -j8
$ make db_bench DEBUG_LEVEL=0 -j8
```

### 3. Run DB_Bench

```bash
$ ./db_bench
```

You can see options of `db_bench` using below command ([Details](https://github.com/facebook/rocksdb/wiki/Benchmarking-tools)):

```bash
$ ./db_bench --help
```

For the report, run the below command and measure the performance of RocksDB on your system:

> Update `-db="/path/to/datadir"` path according to your experimetal environment

```bash
$ ./db_bench --benchmarks="readrandomwriterandom" \
        -db="/path/to/datadir" \
        -use_direct_io_for_flush_and_compaction=true \
        -use_direct_reads=true \
        -write_buffer_size=2097152 \
        -max_bytes_for_level_base=16777216 \
        -max_bytes_for_level_multiplier=5 \
        -duration=600 \
        -statistics \
        -stats_dump_period_sec=30 \
        -stats_interval_seconds=10 2>&1 | tee result.txt
```
- `--benchmarks="readrandomwriterandom"`: 1 writer, N threads doing random reads
- `-db="/path/to/datadir"`: The path of RocksDB data directory 
- `-use_direct_io_for_flush_and_compaction=true`: Use O_DIRECT for background flush and compaction I/O
- `-use_direct_reads=true`: Use O_DIRECT for reading data
    - You should update this value to change the compaction style
- `-write_buffer_size=2097152`: Number of bytes to buffer in memtable before compacting
    - You should change this value according to the capacity of your system
- `-max_bytes_for_level_base=16777216`: Max bytes for level-1
    - You should change this value according to the capacity of your system
- `-max_bytes_for_level_multiplier=5`: A multiplier to compute max bytes for level-N (N >= 2)
    - You should change this value according to the capacity of your system
- `-duration=600`: Time in seconds for the random-ops tests to run
- `-statistics`: Database statistics
- `-stats_dump_period_sec=30`: Gap between printing stats to log in seconds
- `-stats_interval_seconds=10`: Report stats every N second


> If the level does not increase, you need to increase the benchmark execution time or adjust the memtable size or the multiplier value according to the free capacity of your system.


### 4. Record the experimental result

At the end of the benchmark, you can see the below result:

```bash
...
------------------------------------------------
DB path: [/tmp/rocksdbtest-1000/dbbench]
readrandomwriterandom :       6.014 micros/op 166281 ops/sec 60.019 seconds 9979999 operations; ( reads:8982000 writes:997999 total:1000000
 found:3298804)
...
```


- `micros/op`: Microseconds spent processing one operation
- `ops/sec`: Processed operations per second

> In the above result, `/tmp/rocksdbtest-100/dbbench` is the DB path.




### 5. Examine the compaction  stats of RocksDB

Observe the compaction result in `/path/to/rocksdb-data/LOG`

```
$ vim /path/to/rocksdb-data (RocksDB log file)
...
** Compaction Stats [default] **
Level    Files   Size     Score Read(GB)  Rn(GB) Rnp1(GB) Write(GB) Wnew(GB) Moved(GB) W-Amp Rd(MB/s) Wr(MB/s) Comp(sec) CompMergeCPU(sec) Comp(cnt) Avg(sec) KeyIn KeyDrop Rblob(GB) Wblob(GB)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  L0      2/0    1.82 MB   0.5      0.0     0.0      0.0       1.2      1.2       0.0   1.0      0.0     87.3     14.64             13.69      1406    0.010       0      0       0.0       0.0
  L1      1/0   15.99 MB   1.0      4.1     1.2      2.8       3.9      1.1       0.0   3.1     72.7     69.5     57.15             53.19       351    0.163     63M  2808K       0.0       0.0
  L2      1/0   61.43 MB   0.4      4.3     1.0      3.3       3.3      0.0       0.0   3.2     87.2     67.1     50.55             46.96        57    0.887     70M    15M       0.0       0.0
 Sum      4/0   79.24 MB   0.0      8.4     2.3      6.1       8.4      2.4       0.0   6.8     70.0     70.6    122.35            113.85      1814    0.067    134M    18M       0.0       0.0
 Int      0/0    0.00 KB   0.0      0.0     0.0      0.0       0.0      0.0       0.0   4.5     61.1     74.9      0.27              0.26         6    0.046    256K    11K       0.0       0.0
 ...
```

## Report submission
1. Run DB_Bench to benchmark RocksDB on your system.
2. Present the ecperimental results. You must include a screenshot of the terminal that includes `readrandomwriterandom :` result. (i.e.) # of level, about compaction, ops)

Organize the results into a single report and submit it. Follow the [submission guide](./submission-guide.md) for your report.

## Frequently asked questions
- DBBench # of concurrent threads : 1 default thread

## References
- [RocksDB GitHub](https://github.com/facebook/rocksdb) 
- [RocksDB Installation](https://github.com/facebook/rocksdb/blob/main/INSTALL.md)
- [RocksDB Benchmarking tools](https://github.com/facebook/rocksdb/wiki/Benchmarking-tools)
- [Mijin An, How to use db_bench](https://github.com/meeeejin/til/blob/master/rocksdb/how-to-use-db_bench.md)
