# MIN HEAP
# - Min Heap: The root node is the smallest node
# - Max Heap: The root is the max node.

# Heaps are represented as arrays s.t.
# - Node: i
# - Root: 0 
# - Parent: (i - 1 / 2)
# - Left Child: 2i + 1
# - Right Child: 2i + 2

class MinHeap():
    def __init__(self):
        # store integers
        self.heap = []

    def heapify_up(self, i):
        parent = (i - 1) // 2 
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2 

    def heapify_down(self, i):
        left_idx = (2*i) + 1
        right_idx = (2*i) + 2

        while (
            (left_idx < len(self.heap) and self.heap[i] > self.heap[left_idx])
            or 
            (right_idx < len(self.heap) and self.heap[i] > self.heap[right_idx]) 
        ):
            if self.heap[i] > self.heap[left_idx]:
                self.heap[i], self.heap[left_idx] = self.heap[left_idx], self.heap[i]
                i = left_idx
            elif self.heap[i] > self.heap[right_idx]:
                self.heap[i], self.heap[right_idx] = self.heap[right_idx], self.heap[i]
                i = right_idx
            # reset children
            left_idx = (2*i) + 1
            right_idx = (2*i) + 2

    def update_value(self):
        # sift up or down depending on the size of the node
        # if the new value is greater, sift_down
        # else, sift_up
        return
        
    def heap_push(self, n):
        self.heap.append(n)
        self.heapify_up(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0] if len(heap) > 0 else None

    # delete minimum
    def extract_min(self):
        # swap leaf and root
        leaf_val = self.heap[len(self.heap) - 1]
        self.heap[0] = leaf_val
        self.heapify_down(0)
        return 

    def get_heap(self):
        return self.heap

    def init_heap_from_array(self, arr):
        for elem in arr:
            self.heap_push(elem)
        return self.heap

# TEST CASE 1 
# Example Heap
# [1, 3, 6, 5, 9, 8]
#         1
#     3       6 
#  5     9  8

heap = MinHeap()
heap.heap_push(1)
heap.heap_push(3)
heap.heap_push(6)
heap.heap_push(5)
heap.heap_push(9)
heap.heap_push(8)
print(heap.get_heap())

# Heap Push 2:
#         1
#     3       2 
#   5   9   8   6
# [1, 3, 5, 9, 2, 8, 6]

heap.heap_push(2)
print(heap.get_heap())

# testing heapify_down; extract min
#         6
#     3       2 
#   5   9   8   

#         3
#     6       2 
#   5   9   8   

#         3
#     5       2 
#   6   9   8   
# [3, 5, 2, 6, 9, 8, 6]
heap.extract_min()
print(heap.get_heap())

# TEST CASE 2 
heap2 = MinHeap()
heap2.init_heap_from_array([7, 8, 4, 9, 12, 6, 10, 14, 15, 13, 18, 11, 9])
print(heap2.get_heap())
