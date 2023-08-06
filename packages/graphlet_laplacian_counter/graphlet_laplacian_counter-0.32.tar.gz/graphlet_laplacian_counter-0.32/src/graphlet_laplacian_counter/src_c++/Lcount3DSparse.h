//
// Created by windels on 21/02/18.
//

#ifndef NCOUNT2_LCOUNT3DSPARSE_H_H
#define NCOUNT2_LCOUNT3DSPARSE_H_H

#include <map>
#include <vector>
#include "Lcount3D.h"

typedef long long int64; // sadly, long long is not standard in C++ ... yet





class Lcount3DSparse : public Lcount3D {
    typedef std::map<int, int64> map_t;

public:
    Lcount3DSparse(int nrOfOrbits, int nrOfNodes) {
        this->nrOfNodes = nrOfNodes;
        this->nrOfOrbits = nrOfOrbits;
        for( int i =0; i<this->nrOfOrbits; i++){
            std::vector<map_t> row = std::vector<map_t>();
            for( int j =0; j<this->nrOfNodes;j++){
                row.push_back( map_t());
            }
            matrix.push_back( row );
        }

    }
    void applyOvercountCorrection(){
        return;
    }

    int64 getOffDiagonalSum(int orbit, int row){
        int64 sum =0;
        for (int col =0; col < this->nrOfNodes; col++){
            if (col != row){
                sum += this->getCount(orbit,row,col);
            }
        }
        return sum;
    }

    int64* getGDV(int node){

        int64* gdv =new int64[this->nrOfNodes];
        for(int orbit = 0; orbit < this->nrOfOrbits; orbit++)
        {
            //assert(array3D[orbit][node][node]% orbitOvercount[orbit]==0);
            if (matrix[orbit][node][node]% orbitOvercount[orbit]!=0){
//                std::cout<<'\n'<<matrix[orbit][node][node]<<std::endl;
                int a =1;

            }
            gdv[orbit]=matrix[orbit][node][node]/orbitOvercount[orbit];
            std::cout<<matrix[orbit][node][node]/orbitOvercount[orbit]<< ' ';
        }
        std::cout<<std::endl;
        return gdv;
    }

    int64 getCount(int orbit, int row, int col){
        return matrix[orbit][row][col];
    }
    void addCount(int orbit, int centerNodeIndex, int neighbourNodeIndex ){
        //matrix.at(orbit).at(centerNodeIndex)[neighbourNodeIndex]++;
        matrix[orbit][centerNodeIndex][centerNodeIndex]++;
        if ( matrix.at(orbit).at(centerNodeIndex).find(neighbourNodeIndex) == matrix.at(orbit).at(centerNodeIndex).end() ) {
            matrix.at(orbit).at(centerNodeIndex)[neighbourNodeIndex]=1;
        } else {
            matrix.at(orbit).at(centerNodeIndex)[neighbourNodeIndex]++;
        }
    };

    void addCount(int orbit, int centerNodeIndex, std::vector<int> neighbours ){
        matrix.at(orbit).at(centerNodeIndex)[centerNodeIndex]+= (int64) neighbours.size();
        for (int  i=0; i<neighbours.size(); i++ ){
            matrix.at(orbit).at(centerNodeIndex)[neighbours.at(i)]++;
        }
    }

    void addCount(int orbit, int centerNodeIndex,int* neighbours, int nrOfNeighbours ) {
        matrix.at(orbit).at(centerNodeIndex).at(centerNodeIndex)+= (int64) nrOfNeighbours;
        for (int  i=0; i<nrOfNeighbours; i++ ){
            matrix.at(orbit).at(centerNodeIndex).at(neighbours[i])++;
        }
    }

    void  getOverCountCorrectedRow(int orbit, int row, std::vector<double>& correctedRow){
        for ( int col =0; col<this->getNrOfNodes();col++) {

            correctedRow.push_back((double) matrix.at(orbit).at(row)[col] / (double)orbitOvercount[orbit]);
        }
    };

    void getOverCountCorrectedRowOverOrbits(std::vector<unsigned int> orbits ,int row,std::vector<int64>& correctedRow){

//        for( int i =0; i<orbits.size(), i++) {
//            for (int col = 0; col < this->getNrOfNodes(); col++) {
//                if (i==0)
//                {
//                    correctedRow.push_back(
//                            (double) array3D[orbits.at(i)][row][col] / (double) orbitOvercount[orbits.at(i)]);
//                }
//                else{
//                    correctedRow.at(col)+=(double) array3D[orbits.at(i)][row][col] / (double) orbitOvercount[orbits.at(i)];
//                }
//            }
//        }
        return ;
    }

private:
    std::vector<std::vector<map_t>> matrix;

};

#endif //NCOUNT2_LCOUNT3DSPARSE_H_H
