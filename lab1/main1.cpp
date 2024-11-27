#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono> // Include the chrono library
#include "DataGenerator.h"
#include "HeapSort.h"

int main() {
    DataGenerator dataGen;
    HeapSort heapSort;

    const int numFiles = 10;
    const int numNumbers = 10000;
    const std::string baseFilename = "data_";

    // Generate files with random numbers
    dataGen.generateFiles(numFiles, numNumbers, baseFilename);

    std::vector<int> allNumbers;

    // Read numbers from all files
    for (int i = 0; i < numFiles; ++i) {
        std::vector<int> numbers = dataGen.readFile(baseFilename + std::to_string(i) + ".txt");
        allNumbers.insert(allNumbers.end(), numbers.begin(), numbers.end());
    }

    // Start timing the sorting execution
    auto start = std::chrono::high_resolution_clock::now();

    // Sort all numbers using Heap Sort
    heapSort.sort(allNumbers);

    // Stop timing the sorting execution
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    // Print the time taken for sorting
    std::cout << "Time taken for sorting: " << duration.count() << " seconds" << std::endl;

    // Print the first 1000 smallest and largest numbers
    std::cout << "First 1000 smallest numbers: ";
    for (size_t i = 0; i < 1000 && i < allNumbers.size(); ++i) {
        std::cout << allNumbers[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "First 1000 largest numbers: ";
    for (size_t i = allNumbers.size() - 1000; i < allNumbers.size(); ++i) {
        std::cout << allNumbers[i] << " ";
    }
    std::cout << std::endl;

    // Delete the generated files
    dataGen.deleteFiles(numFiles, baseFilename);

    return 0;
}
