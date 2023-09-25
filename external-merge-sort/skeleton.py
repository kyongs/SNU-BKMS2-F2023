import os
import tempfile
import math
import sys
import math
import time


b = 0

input_file_len = 0
run_list = []

cnt = 0


def split_file(input_file_name, n):
    """Read the input file and parse into runs. 
       The size of each run should be n numbers(=lines). (PASS 0)

    Args:
        input_file_name (_type_): input file name
        n (integer): size of one run
    """

    f = open(input_file_name, 'r')
    pass
    ###################################
    #     IMPLEMENT YOUR OWN CODE     #
    ###################################
    
    
def external_merge_sort(): 
    """  
        Do a k-way merge. (PASS 1, PASS 2, ...)

    """
    ###################################
    #     IMPLEMENT YOUR OWN CODE     #
    ###################################
    pass
        


def print_pass_statistics(n, run, io):
    print('[PASS {0}]'.format(n))
    print('  > # of Generated Runs: {0}'.format(run) )
    print('  > # of IOs: {0}'.format(io)  )

    
def print_time_statistics(start_time, end_time):
    print(f"{end_time - start_time:.5f} sec")
    
    
## !! Do NOT Change the Main Function!!
if __name__ == '__main__':
    
    assert (len(sys.argv)==2), 'Argument Missing. $ python3 ./skeleton.py [n]'
    assert (int(sys.argv[1]) ==50 or int(sys.argv[1]) == 100), f"Argument should be 50 or 100, got {sys.argv[1]}"
    
    # argument parsing
    n = int(sys.argv[1]) # size of buffer
    
    # measure start time
    start_time = time.time()
    math.factorial(100000)
    
    # 1. split phase
    split_file("input_file.txt", int(sys.argv[1]))
    
    # 2. Merge phase
    external_merge_sort()

    # measure end time 
    end_time = time.time()
    
    # print statistics
    print_time_statistics(start_time, end_time)

