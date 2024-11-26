#include "DataGenerator.h"
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>

DataGenerator::DataGenerator() {
    std::srand(static_cast<unsigned int>(std::time(nullptr))); // Seed for random number generation
}

void DataGenerator::generateFiles(int numFiles, int numNumbers, const std::string& baseFilename) {
    std::normal_distribution<double> distribution(500, 150); // Mean 500, StdDev 150
    std::default_random_engine generator;

    for (int i = 0; i < numFiles; ++i) {
        std::ofstream outFile(baseFilename + std::to_string(i) + ".txt");
        for (int j = 0; j < numNumbers; ++j) {
            int number = static_cast<int>(std::max(0.0, distribution(generator))); // Ensure positive numbers
            outFile << number << std::endl;
        }
        outFile.close();
    }
}

std::vector<int> DataGenerator::readFile(const std::string& filename) {
    std::vector<int> numbers;
    std::ifstream inFile(filename);
    int number;
    while (inFile >> number) {
        numbers.push_back(number);
    }
    inFile.close();
    return numbers;
}

void DataGenerator::deleteFiles(int numFiles, const std::string& baseFilename) {
    for (int i = 0; i < numFiles; ++i) {
        std::remove((baseFilename + std::to_string(i) + ".txt").c_str());
    }
}
