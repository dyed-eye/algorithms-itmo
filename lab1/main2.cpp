#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()

class BubbleSort {
public:
    void sort(std::vector<float>& array) {
        int n = array.size();
        for (int i = 0; i < n - 1; ++i) {
            for (int j = 0; j < n - i - 1; ++j) {
                if (array[j] > array[j + 1]) {
                    std::swap(array[j], array[j + 1]);
                }
            }
        }
    }
};

int main() {
    // Seed for random number generation
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    // Generate a large dataset of grades (e.g., 1000 grades)
    const int numGrades = 1000;
    std::vector<float> grades(numGrades);

    // Fill the vector with random grades in the range [1.0, 5.0]
    for (int i = 0; i < numGrades; ++i) {
        grades[i] = 1.0f + static_cast<float>(std::rand()) / (static_cast<float>(RAND_MAX / (5.0f - 1.0f)));
    }

    BubbleSort bubbleSort;

    // Measure the time taken to sort
    auto start = std::chrono::high_resolution_clock::now();

    bubbleSort.sort(grades);

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    // Output the sorted grades
    std::cout << "Sorted grades: ";
    for (float grade : grades) {
        std::cout << grade << " ";
    }
    std::cout << std::endl;

    // Output the time taken for sorting
    std::cout << "Time taken for sorting: " << duration.count() << " seconds" << std::endl;

    return 0;
}
