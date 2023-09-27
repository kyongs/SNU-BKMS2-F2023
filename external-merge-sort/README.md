# HW1. External Merge Sort 

## Overview

For HW 1, you will implement external-merge-sort. You need to sort a 20 MB file with limited resources of 1MB. <br/>
Implement on your local environment in Python. (Not Ubuntu!)

<br/>
Configurations are as follows.

- **Size of Input File**: 20MB
- **RAM Size**: 1MB
- **Buffer Size**: 50KB, 100KB
- We assume that there are only input buffers in RAM. (RAM에는 input 버퍼들로만 구성되어있고, input buffer들을 sorting하는 역할을 하는 output buffer는 용량 제한없이 사용할 수 있다고 가정한다. 예를 들면, buffer size 50KB 설정시 1MB ram 안에는 20개의 input buffer가 존재한다. 이들을 merge하기 위한 추가적인 자료구조는 용량에 구애받지 않고 사용할 수 있다. )



### Skeleton Code
- [link](./skeleton.py)
- This code is written for your convenience. You are free to change.
- Related code snippets > [File IO Example Code](./code-snippet.md)



### Input File
- The file to sort. [link](./input_file.txt)
- Sort the file with 'key' value.

- For example, if the data is as below, result should be like this.
  
  Input File Example
  ```
    9122873593MuHNIryLwoSuJOUbvPZiFzKcPXtAfWnbVFTnGXHDCWBRNcYmaByksMUGSspdwVgDgkLTOpxKqhWYFjhbEuqDQeZClY
    8918265496PTyopqdDJHJBuhxLuQLsGRwECzhKIeSQzMvDZfdYZtjSXffzgEhbwvrXvpUVFnjOuHZqDkdMlgXoKgCnmxapPamWbt
    3010583290phDaCnsNdDVvlWCcZoukbOYMMUwRgmxoVPKNsrPTqheaiezXObBdShKTLsYbKmCuTXEFcaJkHfiJHiXqyAmqPfSEvj
    9229061361sJRYxBVeJocGkuoloqnuyedztGuEIiTvHQXUsjObHAnFUCygYSZZwQtbaWTkxJvEIhrhLPjPqNVKURFdPgCAMCBSil
    9363798209angGDhbnDzZUlLeMIBuwVRvfWKHHBsyArOqtAbRmEHpPpEYDxuizcnclUjxSvBOjZCJeQNoxFdsTtCTaRFJXVcXmKG
    1416363649iKbajocMyCFBTXkgdKOfwFbeXRJgxRjOPvTCYHRfjBhLyGcUQEuHZtVhSwQSuYEVampAqzkxNitmxGEVvmCzNnJUnc
    8382079481KIYlZWGWPZWneVRoyBBXtzCMNiLpKkxhSRytLBmCxnOJuczHAbFdHUmrlgOwsoSsFEIibvqChQMXlcvzTksrPtZbjm
  ```
  Corresponding Output
  ```
    1416363649iKbajocMyCFBTXkgdKOfwFbeXRJgxRjOPvTCYHRfjBhLyGcUQEuHZtVhSwQSuYEVampAqzkxNitmxGEVvmCzNnJUnc
    3010583290phDaCnsNdDVvlWCcZoukbOYMMUwRgmxoVPKNsrPTqheaiezXObBdShKTLsYbKmCuTXEFcaJkHfiJHiXqyAmqPfSEvj
    8382079481KIYlZWGWPZWneVRoyBBXtzCMNiLpKkxhSRytLBmCxnOJuczHAbFdHUmrlgOwsoSsFEIibvqChQMXlcvzTksrPtZbjm
    8918265496PTyopqdDJHJBuhxLuQLsGRwECzhKIeSQzMvDZfdYZtjSXffzgEhbwvrXvpUVFnjOuHZqDkdMlgXoKgCnmxapPamWbt
    9122873593MuHNIryLwoSuJOUbvPZiFzKcPXtAfWnbVFTnGXHDCWBRNcYmaByksMUGSspdwVgDgkLTOpxKqhWYFjhbEuqDQeZClY
    9229061361sJRYxBVeJocGkuoloqnuyedztGuEIiTvHQXUsjObHAnFUCygYSZZwQtbaWTkxJvEIhrhLPjPqNVKURFdPgCAMCBSil
    9363798209angGDhbnDzZUlLeMIBuwVRvfWKHHBsyArOqtAbRmEHpPpEYDxuizcnclUjxSvBOjZCJeQNoxFdsTtCTaRFJXVcXmKG
  ```


### Result
- After you execute the program, the result should be as follows.
- i.e)
    ```
    $ python3 ./skeleton.py 2
    [PASS 0]
    > # of Generated Runs: 6
    > # of IOs: 12

    [PASS 1]
    > # of Generated Runs: 2
    > # of IOs: 12

    ...

    ===========================
    Execution Time: 1.2938 sec
    ```

- `# of Generated Runs`: The number of runs generated at the end of each pass.
- `# of IOs`: The number of IO operations that occurred during each pass. 
- `Execution Time`: The time from the start of the Split Phase until the end of the Merge Phase.


### Submission Guide
> **Due Date**: **2023.10.6** (Sunday) PM 11:59
>
> **Where to Submit**: ETL
>
> **Submit Format**: HW1-[studentID].pdf    ex)HW1-2020-00000.pdf

- The report is in a **free format**, but please be sure to write the following items.
  - Report Title:   "HW1. External Merge Sort"
  - Student ID
  
- All reports must be in either Korean or English
- Make sure your report includes below chapters:
  - Code Explanation
  - Screenshot of Result (Refer to **Result** section above.)
  - Result analysis varying buffer size **(50KB, 100KB)**.

  
