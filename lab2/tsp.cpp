// tsp.cpp
#include "tsp.h"
#include <cmath>
#include <limits>
#include <omp.h>

double distance(const Point& p1, const Point& p2) {
    return std::sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}

double tsp(const std::vector<Point>& points) {
    int n = points.size();
    std::vector<std::vector<double>> dp(1 << n, std::vector<double>(n, std::numeric_limits<double>::infinity()));
    dp[1][0] = 0;  // Start from the first point

    for (int mask = 0; mask < (1 << n); ++mask) {
        #pragma omp parallel for
        for (int u = 0; u < n; ++u) {
            if (mask & (1 << u)) {
                for (int v = 0; v < n; ++v) {
                    if (!(mask & (1 << v))) {
                        int new_mask = mask | (1 << v);
                        dp[new_mask][v] = std::min(dp[new_mask][v], dp[mask][u] + distance(points[u], points[v]));
                    }
                }
            }
        }
    }

    // Return to the starting point
    double result = std::numeric_limits<double>::infinity();
    for (int v = 1; v < n; ++v) {
        result = std::min(result, dp[(1 << n) - 1][v] + distance(points[v], points[0]));
    }
    return result;
}
