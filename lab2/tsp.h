// tsp.h
#ifndef TSP_H
#define TSP_H

#include <vector>

struct Point {
    int x, y;
};

double distance(const Point& p1, const Point& p2);
double tsp(const std::vector<Point>& points);

#endif // TSP_H
