import random

def sampler(file:str,prefix:str="sample",cnt=50):
    """
    sample txt data
    :param file: file name
    :param prefix: target file prefix
    :param cnt: total lines of sample data
    :return:
    """
    with open(file) as fp, open(f"{file.split('.')[0]}-{prefix}.txt",'w') as \
            tfp:
        lines = fp.readlines()
        assert len(lines)>cnt,f"length of {file} must be greater than {cnt}, " \
                              f"got file length {len(file)} but cnt is {cnt}"
        t_lines = random.sample(lines,cnt)
        for line in t_lines:
            print(line,file=tfp)