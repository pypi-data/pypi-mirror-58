from guang.Utils.toolsFunc import probar
import os
def reduce_from_duration(filelist):
    """
    return: reduce_list, reduced_list, IDX
    """
    reduce_list = []
    reduced_list = []
    IDX = []
    for idx, i in probar(filelist):
        try:
            print(i)
            if librosa.get_duration(filename = i) < 10:
                reduce_list.append(i)
            else:
                reduced_list.append(i)
                IDX.append(idx)
        except:
            print(f'file {i} open failed, and has been ignored')
            continue
    print(F'The number that need to be deleted:{len(reduce_list)}')
    return reduce_list, reduced_list, IDX

if __name__ == "__main__":
    from glob import glob
    flist = glob(r"data/*")
#     print(flist)
    reduce_from_duration(flist)
