#include "MergeSort.h"

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
    mergeSort(array, temp, leftStart, middle); // Sort left half
    mergeSort(array, temp, middle + 1, rightEnd); // Sort right half
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
