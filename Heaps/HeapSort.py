class Solution:
    def heapSort(self, a):
        # Min-heap functions
        def heapify(heap, n, i):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                heapify(heap, n, smallest)

        n = len(a)

        # Build min-heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(a, n, i)

        # Extract min and put at correct position
        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]  # move min to the end
            heapify(a, i, 0)         # heapify reduced heap

        # Now array is sorted in descending order
        a.reverse()  # make ascending
