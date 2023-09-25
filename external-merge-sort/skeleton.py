import os
import tempfile
import math
import sys
import math
import time


RAM_SIZE = 10000 # number of lines



def split_file(input_file_name):
    """Read the input file and parse into runs. 
       The size of each run should be n numbers(=lines). (PASS 0)

    Args:
        input_file_name (_type_): input file name
        n (integer): size of one run, # of pages
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
    print('  > # of IOs: {0}'.format(io) , endl="\n\n" )


def print_time_statistics(start_time, end_time):
    print("==============================")
    print(f"Execution Time : {end_time - start_time:.5f} sec")


if __name__ == '__main__':
    
    assert (len(sys.argv)==2), 'Missing Argument. $ python3 ./skeleton.py [n]'
    
    # argument parsing
    n = int(sys.argv[1]) # size of buffer
    
    # measure start time
    start_time = time.time()
    math.factorial(100000)
    
    # 1. split phase
    split_file("input_file.txt")
    
    # 2. Merge phase
    external_merge_sort()

    # measure end time 
    end_time = time.time()
    
    # print statistics
    print_time_statistics(start_time, end_time)
