import math
class heap:

    def __init__(self, array, heap_size, array_length):
        self.array = array
        self.heap_size = heap_size
        self.array_length = array_length

    def max_heapify(self, i):
        """ i is the index of array to be manipulated to make the heap """
        l = self.left(i)
        r = self.right(i)
        A = self.array;
        if l < self.heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and A[r] > A[largest]:
            largest = r
        # print ("A:", A,"l:",l,"r:",r,"i:",i,"heap size:",self.heap_size,"largest:",largest)
        if largest != i:
            # swap i with largest
            A[i], A[largest] = A[largest], A[i]
            self.array = A
            # recurse with largest index we just swapped with i
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(int((self.array_length - 1)/2),-1,-1):
            self.max_heapify(i)


    def parent(self,i):
        if i == 0:
            return 0
        return math.floor((i - 1)/2)

    def left(self,i):
        """for 0 based array for 1 based it is 2*i as mentioned in cormen"""
        return 2*i+1

    def right(self, i):
        """for 0 based array for 1 based it is 2*i + 1 as mentioned in cormen"""
        return 2*i + 2
