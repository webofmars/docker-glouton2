#!/bin/env python

import os
import sys
import signal
import time
import multiprocessing as mp

cpus=abs(int(os.environ.get('CPUS', 1)))
mem=abs(int(os.environ.get('MEM', 256)))
step=abs(int(os.environ.get('STEP', 10)))
memory=''
run = True

def handler_stop_signals(signum, frame):
    global run
    run = False

def do_nothing(process_id):
    print("Generating 1 core cpu load (process %d) ..." % (process_id))
    global run
    while run:
        pass

def consume_memory(step):
    global memory
    if sys.getsizeof(memory) < mem*1024*1024:
        memory +=' '*int(1024*1024*step)

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

if __name__ == "__main__":
    #mp.set_start_method('spawn')
    for num in range(cpus):
        p = mp.Process(target=do_nothing, args=(num,), daemon=True)
        p.start()

while run:
    if __name__ == "__main__":
        consume_memory(step)
        print("Consuming %s MB of memory ..." % (int(sys.getsizeof(memory)/(1024*1024))))
        time.sleep(3)
    else:
        do_nothing(os.getpid())

print("Exiting ...")
