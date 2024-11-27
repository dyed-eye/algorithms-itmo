#include "HeapSort.h"

void HeapSort::sort(std::vector<int>& array) {
    int n = array.size();

    // Build a max heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(array, n, i);
    }

    // One by one extract elements from the heap
    for (int i = n - 1; i > 0; i--) {
        std::swap(array[0], array[i]); // Move current root to end
        heapify(array, i, 0); // Call heapify on the reduced heap
    }
}

void HeapSort::heapify(std::vector<int>& array, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; // left = 2*i + 1
    int right = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (left < n && array[left] > array[largest]) {
        largest = left;
    }

    // If right child is larger than largest so far
    if (right < n && array[right] > array[largest]) {
        largest = right;
    }

    // If largest is not root
    if (largest != i) {
        std::swap(array[i], array[largest]); // Swap root with largest
        heapify(array, n, largest); // Recursively heapify the affected subtree
    }
}
