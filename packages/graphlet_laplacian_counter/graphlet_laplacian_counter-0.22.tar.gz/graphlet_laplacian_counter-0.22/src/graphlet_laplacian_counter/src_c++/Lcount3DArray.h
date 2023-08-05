//
// Created by windels on 06/02/18.
//

#ifndef NCOUNT2_LCOUNT3DARRAY_H
#define NCOUNT2_LCOUNT3DARRAY_H

#include "Lcount3D.h"
#include <iostream>
#include <vector>




class Lcount3DArray : public Lcount3D {

public:
    Lcount3DArray( int nrOfOrbits, int nrOfNodes) {
        array3D=allocate3DArray(nrOfOrbits,nrOfNodes,nrOfNodes);
        this->nrOfNodes=nrOfNodes;
        this->nrOfOrbits=nrOfOrbits;

    }

    void addCount(int orbit, int centerNodeIndex, int neighbourNodeIndex ){
        array3D[orbit][centerNodeIndex][centerNodeIndex]++;
        array3D[orbit][centerNodeIndex][neighbourNodeIndex]++;
    }

    void addCount(int orbit, int centerNodeIndex, std::vector<int> neighbours ) {
        array3D[orbit][centerNodeIndex][centerNodeIndex]+= (int64) neighbours.size();
        for (int  i=0; i<neighbours.size(); i++ ){
            array3D[orbit][centerNodeIndex][neighbours.at(i)]++;
        }
    }

    void addCount(int orbit, int centerNodeIndex,int* neighbours, int nrOfNeighbours ) {
        array3D[orbit][centerNodeIndex][centerNodeIndex]+= (int64) nrOfNeighbours;
        for (int  i=0; i<nrOfNeighbours; i++ ){
            array3D[orbit][centerNodeIndex][neighbours[i]]++;
        }
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
            if (array3D[orbit][node][node]% orbitOvercount[orbit]!=0){
                std::cout<<'\n'<<array3D[orbit][node][node]<<std::endl;
                int a =1;

            }
            gdv[orbit]=array3D[orbit][node][node]/orbitOvercount[orbit];
            std::cout<<  array3D[orbit][node][node]/orbitOvercount[orbit]<< ' ';
        }
        std::cout<<std::endl;
        return gdv;

    }

    void applyOvercountCorrection(){
        return;
    }

    int64 getCount(int orbit, int row, int col){
        return array3D[orbit][row][col];
    }

    void  getOverCountCorrectedRow(int orbit, int row,std::vector<double>& correctedRow){

//        double * correctedRow =new double [this->nrOfNodes];


            for ( int col =0; col<this->getNrOfNodes();col++) {
//                if (array3D[orbit][row][col] % orbitOvercount[orbit] != 0) {
//                    std::cout << row<<' '<<col<< ' ' <<orbitOvercount[orbit]<<' '<< array3D[orbit][row][col] << std::endl;
//                }
                correctedRow.push_back((double) array3D[orbit][row][col] / (double)orbitOvercount[orbit]);
//std::cout<< array3D[orbit][row][col]<< '\n';
        }

    }

private:

    int64*** array3D;
    //orbit based defenition is not symmetric -> full matrix
    int64*** allocate3DArray(int x, int y, int z){
        int64*** the_array = new int64**[x];
        for(int i(0); i < x; ++i)
        {
            the_array[i] = new int64*[y];
            for(int j(0); j < y; ++j)
            {
                the_array[i][j] = new int64[z];
                for(int k(0); k < z; ++k)
                {
                    the_array[i][j][k]= 0.;
                }
            }
        }
        return the_array;
    }
};


#endif //NCOUNT2_LCOUNT3DARRAY_H
