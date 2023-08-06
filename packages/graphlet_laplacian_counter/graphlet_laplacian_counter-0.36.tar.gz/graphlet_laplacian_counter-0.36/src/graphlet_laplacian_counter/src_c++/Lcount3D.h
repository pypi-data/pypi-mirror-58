//
// Created by windels on 19/02/18.
//

#ifndef NCOUNT2_LCOUNT3D_H
#define NCOUNT2_LCOUNT3D_H

#include <vector>


//typedef long long int64; // sadly, long long is not standard in C++ ... yet
//old overcount before lcount correction
//    const int orbitOvercount[73] = {1,2,2,6,2,2,6,6,8,4,4,4,12,12,24,2,2,2,2,2,2,2,24,24,2,2,2,4,4,4,4,4,4,4,10,4,4,4,4,
//                                    4,4,4,4,8,8,8,8,8,8,12,12,14,14,14,12,12,12,12,12,20,20,20,28,28,28,36,36,36,48,48,72,72,120};


//used to corrects for overcount because of graphlet size AND overlap breadth first search
static const int orbitOvercount[73]={1, 4, 4, 12, 6, 6, 18, 18, 24, 12, 12, 12, 36, 36, 72, 8, 8, 8, 8, 8, 8, 8, 96, 96, 8, 8, 8, 16, 16, 16, 16, 16, 16, 16, 40, 16, 16, 16, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32, 32, 48, 48, 56, 56, 56, 48, 48, 48, 48, 48, 80, 80, 80, 112, 112, 112, 144, 144, 144, 192, 192, 288, 288, 480};

//used to correct for graphlet size only and not correct for count overlap due to breadth first search(i.e. when counting only one node)
static const int graphlet_size_overcount[73]={1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4};

typedef long long int64; // sadly, long long is not standard in C++ ... yet

class Lcount3D {



protected:
    int nrOfNodes;
    int nrOfOrbits;
public:

    Lcount3D(){};

    virtual void addCount(int orbit, int centerNodeIndex, int neighbourNodeIndex )=0;
    virtual void  addCount(int orbit, int centerNodeIndex,int* neighbours, int nrOfNeighbours )=0;
    virtual void addCount(int orbit, int centerNodeIndex, std::vector<int> neighbours )=0;

    virtual void getOverCountCorrectedRow(int orbit, int row, std::vector<double>& correctedRow)=0;
    virtual int64 getOffDiagonalSum(int orbit, int row)=0;
    virtual int64 getCount(int orbit, int row, int col)=0;
    virtual int64* getGDV(int node)=0;
    virtual void applyOvercountCorrection()=0;
    virtual void  getOverCountCorrectedRowOverOrbits(std::vector<unsigned int> orbits ,int row,std::vector<double>& correctedRow)=0;






    int getNrOfNodes(){
        return this->nrOfNodes;
    }

    int getNrOfOrbits() const {
        return nrOfOrbits;
    }

};

#endif //NCOUNT2_LCOUNT3D_H
