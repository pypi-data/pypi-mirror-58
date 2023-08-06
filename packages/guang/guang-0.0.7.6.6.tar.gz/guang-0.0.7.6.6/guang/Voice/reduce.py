from multiprocessing import Pool, TimeoutError
import os
import librosa
from glob import glob

def is_lt_duration(file, least_time):
    try:
        if librosa.get_duration(filename = file) < least_time:
            return 1
        else:
            return 0
    except:
        print(f'file {i} open failed, and has been ignored')
#         return None

def reduce_from_duration(filelist, least_time=1):
    '''
    return reduced list
    '''
    with Pool(processes=None) as pool:
        multi_res=[pool.apply_async(is_lt_duration, (i,least_time)) for i in filelist]
        reduce_list = [res.get() for res in multi_res]
        
    return [filelist[idx] for idx,i in enumerate(reduce_list) if i==0]


import time
if __name__ == "__main__":
    t1=time.time()
    flist = glob(r"data/*")
    l = reduce_from_duration(flist, least_time=3)
    print(l)
    print(time.time()- t1)
