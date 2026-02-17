class MinHeap:
    def __init__(self):
        self.h=[]
    def insert(self,x):
        if not self.h:
            self.h.append(x)
            return
        self.h.append(x)
        y=len(self.h)-1
        p=(y-1)//2
        while p>=0 and self.h[y]<self.h[p]:
            self.h[p],self.h[y]=self.h[y],self.h[p]
            y=p
            p=(y-1)//2



#2. cleaner code to heapify up.
class MinHeap:
    def __init__(self):
        self.h = []

    def insert(self, x):
        self.h.append(x)
        i = len(self.h) - 1

        # heapify up
        while i > 0:
            parent = (i - 1) // 2
            if self.h[i] < self.h[parent]:
                self.h[i], self.h[parent] = self.h[parent], self.h[i]
                i = parent
            else:
                break

#         1
#       /   \
#      3     4
#     / \   / \
#    8   9  5  6
    def extract_min(self):
        if not self.h:
            return None

        if len(self.h) == 1:
            return self.h.pop()

        root = self.h[0]
        self.h[0] = self.h.pop()

        i = 0
        n = len(self.h)

        # heapify down
        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and self.h[left] < self.h[smallest]:
                smallest = left

            if right < n and self.h[right] < self.h[smallest]:
                smallest = right

            if smallest != i:
                self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
                i = smallest
            else:
                break

        return root


        

