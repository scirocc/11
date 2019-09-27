import array
from datetime import datetime, timedelta

if __name__=='__main__':
    size = 1000000
    def tranverse(a):
        t = datetime.now()
        for i in range(size):
            a[i]
        print('elapsed %s'% (datetime.now()- t))

    a = array.array('i', [i for i in range(size)])
    print('test array')
    tranverse(a)


    a = {}
    for i in range(size):
        a[i] = i
    print('test dict')
    tranverse(a)


    from multiprocessing import Manager
    manager = Manager()
    a = manager.list([i for i in range(size)])
    print( 'test shared manager list')
    tranverse(a)


    from multiprocessing.sharedctypes import RawArray
    a = RawArray( 'i', [i for i in range(size)] )
    print( 'test sharedctypes list in main process')
    tranverse(a)

    from multiprocessing import Process
    ps = [Process(target=tranverse, args=(a, )) for i in range(8)]
    print( 'test sharedctypes list in subprocess')
    for p in ps:
        p.start()
    for p in ps:
        p.join()