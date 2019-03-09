import time 

reps = 1000
repllist = range(reps)

def timer(func, *args, **kwargs):
    start = time.clock()
    for i in repllist:
        ret = (func, *args, **kwargs)
    elapsed = time.clock() - start
    return(elapsed, ret)
    