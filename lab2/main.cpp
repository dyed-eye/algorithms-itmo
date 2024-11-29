// main.cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include "tsp.h"

void generateRandomPoints(std::vector<Point>& points, int numPoints) {
    for (int i = 0; i < numPoints; ++i) {
        Point p;
        p.x = rand() % 100; // Random x coordinate between 0 and 99
        p.y = rand() % 100; // Random y coordinate between 0 and 99
        points.push_back(p);
    }
}

void printPoints(const std::vector<Point>& points) {
    std::cout << "Generated Points:\n";
    for (size_t i = 0; i < points.size(); ++i) {
        std::cout << "Point " << i + 1 << ": (" << points[i].x << ", " << points[i].y << ")\n";
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number_of_points>\n";
        return 1;
    }

    int numPoints = std::atoi(argv[1]);
    if (numPoints <= 0) {
        std::cerr << "Please enter a positive integer for the number of points.\n";
        return 1;
    }

    std::vector<Point> points;
    srand(static_cast<unsigned int>(time(0))); // Seed for random number generation
    generateRandomPoints(points, numPoints);
    printPoints(points);

    clock_t start = clock();
    double result = tsp(points);
    clock_t end = clock();
    double executionTime = static_cast<double>(end - start) / CLOCKS_PER_SEC;
    double complexity = numPoints * numPoints * pow(2, numPoints);

    std::cout << "Minimum cost of the tour: " << result << std::endl;
    std::cout << "Complexity (O(n^2 * 2^n)): " << complexity << std::endl;
    std::cout << "Execution time: " << executionTime << " seconds\n";

    return 0;
}
