#ifndef HEAPSORT_H
#define HEAPSORT_H

#include <vector>

class HeapSort {
public:
    void sort(std::vector<int>& array); // Public method to sort the array

private:
    void heapify(std::vector<int>& array, int n, int i); // Heapify a subtree rooted at index i
};

#endif // HEAPSORT_H
