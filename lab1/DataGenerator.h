#ifndef DATAGENERATOR_H
#define DATAGENERATOR_H

#include <vector>
#include <string>

class DataGenerator {
public:
    DataGenerator();
    void generateFiles(int numFiles, int numNumbers, const std::string& baseFilename);
    std::vector<int> readFile(const std::string& filename);
    void deleteFiles(int numFiles, const std::string& baseFilename);
};

#endif // DATAGENERATOR_H
