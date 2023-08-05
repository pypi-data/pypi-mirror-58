//
// Created by windels on 07/02/18.
//

#ifndef NCOUNT2_WRITER_H
#define NCOUNT2_WRITER_H


#include "Lcount3D.h"
#include <iostream>
#include <fstream>
#include <vector>

class Writer {


public:

    void write_orbit_laplacian(Lcount3D &lcount, std::string outputPrefix) {

        std::cout<<"outputting Graphlet Laplacian Counts"<<std::endl;
        for (int orbit = 0; orbit < lcount.getNrOfOrbits(); orbit++) {
            std::string outname = outputPrefix+'_'+std::to_string( orbit)+".csv";
            std::cout<<outname<<std::endl;
            std::ofstream myfile(outname);
            if (myfile.is_open()) {
                std::vector<double> correctedRow = std::vector<double>();
                for (int row = 0; row < lcount.getNrOfNodes(); row++) {
                    correctedRow.clear();
                    lcount.getOverCountCorrectedRow(orbit, row,correctedRow);
                    for (int col = 0; col < lcount.getNrOfNodes(); col++) {
                        if (col == row) {
                            myfile << correctedRow.at(row) << ' ';
                        } else {
                            myfile << '-' << correctedRow.at(col) << ' ';
                        }
                    }
                    myfile << '\n';
                }
                myfile.close();
            } else {
                std::cout << "Unable to open output file";
                exit(1);
            }
        }
    }

    void write_graphlet_laplacian_edgelist(Lcount3D &lcount, std::string outputPrefix){

        std::cout<<"outputting Graphlet Laplacian Counts as edgelist"<<std::endl;
        std::vector<std::vector<unsigned int> > graphletToOrbits{ { 0},{ 1,2 },{ 3 },{4,5},{6,7},{8},{9,10,11},{12,13},{14} };


        for (unsigned int graphlet=0; graphlet<9;graphlet++) {
            std::string outname = outputPrefix + '_' + std::to_string(graphlet) + "_none.edgelist";
            std::cout << outname << std::endl;
            std::ofstream myfile(outname);
            if (myfile.is_open()) {
                std::vector<unsigned int> orbits = graphletToOrbits.at(graphlet);
                std::vector<double> correctedRow = std::vector<double>();
                for (int row = 0; row < lcount.getNrOfNodes(); row++) {
                    correctedRow.clear();
                    lcount.getOverCountCorrectedRowOverOrbits(orbits, row, correctedRow);
                    for (int col = row; col < lcount.getNrOfNodes(); col++) {

                        if (correctedRow.at(col) != 0.0)
                            if (col == row) {
                                myfile << row << ' ' << col << ' ' << correctedRow.at(col) << std::endl;
                            } else {
                                myfile << row << ' ' << col << " -" << correctedRow.at(col) << std::endl;
                            }
                    }
                }
                myfile.close();
            } else {
                std::cout << "Unable to open output file";
                exit(1);
            }
        }
    }
};


#endif //NCOUNT2_WRITER_H
