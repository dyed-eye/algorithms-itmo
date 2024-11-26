#ifndef MERGESORT_H
#define MERGESORT_H

#include <vector>

class MergeSort {
public:
    void sort(std::vector<int>& array);
private:
    void mergeSort(std::vector<int>& array, std::vector<int>& temp, int leftStart, int rightEnd);
    void merge(std::vector<int>& array, std::vector<int>& temp, int leftStart, int middle, int rightEnd);
};

#endif // MERGESORT_H
