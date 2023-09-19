# Lab Report Submission

Make sure that you submit your own individual work. (TBA: 아직 따라하지 마세요)

## Formatting

- Download the REPORT(TBA).
- All reports must be in either *Korean or English*
- Make sure that your report includes below chapters:
    - Purpose of the experiment (실험 목적)
    - Experimental setup (실험 환경); For example:
        - System setup:
        
        | Type | Specification |
        |:-----------:|:----------------------------------------------------------:|
        | OS          | Ubuntu 18.04.5 LTS                                         |
        | CPU         | Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz (Total 32 cores)|
        | Memory      | 32GB                                                       |
        | Kernel      | 5.4.0-66-generic                                           |
        | Data Device *(Optional)* | Intel® Optane™ SSD 900P Series 480GB          |
        | Log Device *(Optional)* | Samsung 850 PRO SSD 256GB                     |
        
        - If you didn't mount any device, specify the device's name on which the root file system is mounted:
            1. Check your device using `mount | grep "on / type"`
            2. Then, find the device model name using `sudo smartctl -a /dev/sda1` for SATA devices and `sudo nvme list` for NVMe devices
        - Benchmark setup:
      
        | Type | Configuration |
        |:----------------:|:----------------------:|
        | DB size          | 2GB (20 warehouse)     |
        | Buffer Pool Size | 500MB (25% of DB size) |
        | Benchmark Tool   | tpcc-mysql             |
        | Runtime          | 1200s                  |
        | Connections      | 8                      |
        
    - Experimental methods (실험 내용 및 방법)
    - Experimental results (실험 결과)
    - Analysis of the results (실험 결과 분석)
    - Reference; if necessary (참고 문헌)
- Submit a PDF file with the following file name: `{Student ID}-{Name}-{week#}.pdf` (e.g., `2018000000-이보현-week2.pdf`)
- Only `.pdf` formats should be submitted

## Due date
- TBD
- Submit your report via *ETL*
