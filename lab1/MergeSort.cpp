#include "MergeSort.h"
#include <thread> // Include the thread library
#include <vector>

void MergeSort::sort(std::vector<int>& array) {
    if (array.size() <= 1) {
        return; // Base case: array is already sorted
    }
    std::vector<int> temp(array.size());
    mergeSort(array, temp, 0, array.size() - 1);
}

void MergeSort::mergeSort(std::vector<int>& array, std::vector<int>& temp, int leftStart, int rightEnd) {
    if (leftStart >= rightEnd) {
        return; // Base case
    }
    int middle = (leftStart + rightEnd) / 2;

    // Check if the size of the current segment is below the threshold
    if ((rightEnd - leftStart) < THRESHOLD) {
        // Use single-threaded sort for small arrays
        mergeSort(array, temp, leftStart, middle);
        mergeSort(array, temp, middle + 1, rightEnd);
    } else {
        // Create threads for larger arrays
        std::thread leftThread(&MergeSort::mergeSort, this, std::ref(array), std::ref(temp), leftStart, middle);
        std::thread rightThread(&MergeSort::mergeSort, this, std::ref(array), std::ref(temp), middle + 1, rightEnd);

        // Wait for both threads to finish
        leftThread.join();
        rightThread.join();
    }

    merge(array, temp, leftStart, middle, rightEnd); // Merge sorted halves
}

void MergeSort::merge(std::vector<int>& array, std::vector<int>& temp, int leftStart, int middle, int rightEnd) {
    for (int i = leftStart; i <= rightEnd; ++i) {
        temp[i] = array[i]; // Copy to temp array
    }

    int leftIndex = leftStart;
    int rightIndex = middle + 1;
    int currentIndex = leftStart;

    // Merge the temp arrays back into the original array
    while (leftIndex <= middle && rightIndex <= rightEnd) {
        if (temp[leftIndex] <= temp[rightIndex]) {
            array[currentIndex] = temp[leftIndex];
            leftIndex++;
        } else {
            array[currentIndex] = temp[rightIndex];
            rightIndex++;
        }
        currentIndex++;
    }

    // Copy the remaining elements from the left half, if any
    while (leftIndex <= middle) {
        array[currentIndex] = temp[leftIndex];
        leftIndex++;
        currentIndex++;
    }
}
