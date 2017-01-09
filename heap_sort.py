from heap import *


array = [18,25,19,14,7,9,3,16,8,100]
# get length of array
array_length = len(array);
heap_length = array_length;

heap1 = heap(array, array_length, heap_length)


"""
call max_heapify on each element of array from mid to start because
we know A[n/2 .. n] are leaves. So A[0 .. (n/2-1)] are root nodes to
other nodes for sure. we ran algorithm backwards because it is most
efficient to use it bottom up then top down. Top down will need more
no of swaps and eventually will produce wrong result.
"""

# arrange the array into heap which means you should know what are the
# properties of heap google it reader
heap1.build_max_heap()

for i in range((array_length - 1), 0, -1):
    # 0th or root element is max so swap max with last element and exclude last element from heap_size
    # by decrementing it
    heap1.array[0], heap1.array[i] = heap1.array[i], heap1.array[0]
    heap1.heap_size = heap1.heap_size - 1
    # 0th element of array is out of order and malforming the heap so again heapify it
    heap1.max_heapify(0)


#heap1.max_heapify(1)
print (heap1.array)
