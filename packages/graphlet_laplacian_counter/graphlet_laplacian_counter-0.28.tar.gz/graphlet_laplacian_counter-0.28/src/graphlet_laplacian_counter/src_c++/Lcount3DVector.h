//
// Created by windels on 06/02/18.
//

#ifndef NCOUNT2_LCOUNT3DVECTOR_H
#define NCOUNT2_LCOUNT3DVECTOR_H

#include "Lcount3D.h"
#include <iostream>
#include <vector>




class Lcount3DVector : public Lcount3D {

public:
    Lcount3DVector( int nrOfOrbits, int nrOfNodes) {
        allocateMemory(nrOfOrbits,nrOfNodes,nrOfNodes);
        this->nrOfNodes=nrOfNodes;
        this->nrOfOrbits=nrOfOrbits;

    }

    void addCount(int orbit, int centerNodeIndex, int neighbourNodeIndex ){
        vector3D[orbit][centerNodeIndex][centerNodeIndex]++;
        vector3D[orbit][centerNodeIndex][neighbourNodeIndex]++;
    }

    void addCount(int orbit, int centerNodeIndex, std::vector<int> neighbours ) {
        vector3D[orbit][centerNodeIndex][centerNodeIndex]+= (int64) neighbours.size();
        for (int  i=0; i<neighbours.size(); i++ ){
            vector3D[orbit][centerNodeIndex][neighbours[i]]++;
        }
    }

    void addCount(int orbit, int centerNodeIndex,int* neighbours, int nrOfNeighbours ) {
        vector3D.at(orbit).at(centerNodeIndex).at(centerNodeIndex)+= (int64) nrOfNeighbours;
        for (int  i=0; i<nrOfNeighbours; i++ ){
            vector3D[orbit][centerNodeIndex][neighbours[i]]++;
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
            //assert(vector3D[orbit][node][node]% orbitOvercount[orbit]==0);
            if (vector3D.at(orbit).at(node).at(node)% orbitOvercount[orbit]!=0){
                std::cout<<'\n'<<vector3D.at(orbit).at(node).at(node)<<std::endl;

            }
            gdv[orbit] = vector3D.at(orbit).at(node).at(node)/orbitOvercount[orbit];
            std::cout<<  vector3D.at(orbit).at(node).at(node)/orbitOvercount[orbit]<< ' ';
        }
        std::cout<<std::endl;
        return gdv;
    }

    int64 getCount(int orbit, int row, int col){
        return vector3D.at(orbit).at(row).at(col);
    }


    void applyOvercountCorrection(){
        return;
    }


    void  getOverCountCorrectedRow(int orbit, int row,std::vector<double>& correctedRow){

            for ( int col =0; col<this->getNrOfNodes();col++) {
                correctedRow.push_back( (double) vector3D.at(orbit).at(row).at(col) / (double) orbitOvercount[orbit]);
        }

    }


    void getOverCountCorrectedRowOverOrbits(std::vector<unsigned int> orbits ,int row,std::vector<double>& correctedRow){

        for( int i =0; i<orbits.size(); i++) {
            for (int col = 0; col < this->getNrOfNodes(); col++) {
                if (i==0)
                {
                    correctedRow.push_back( (double) vector3D[orbits.at(i)][row][col] / (double) orbitOvercount[orbits.at(i)]);
                }
                else{
                    correctedRow.at(col)+= (double) vector3D[orbits.at(i)][row][col] / (double) orbitOvercount[orbits.at(i)];
                }
            }
        }
    }


    void getGraphletSizeCorrectedRowOverOrbits(std::vector<unsigned int> orbits ,int row,std::vector<double>& correctedRow){
    //only correct for graphlet size, not for orbit count overlap

        for( int i =0; i<orbits.size(); i++) {
            for (int col = 0; col < this->getNrOfNodes(); col++) {
                if (i==0)
                {
                    correctedRow.push_back((double)vector3D[orbits.at(i)][row][col] / (double) graphlet_size_overcount[orbits.at(i)]  );
                }
                else{
                    correctedRow.at(col)+= (double)vector3D[orbits.at(i)][row][col] / (double) graphlet_size_overcount[orbits.at(i)];
                }
            }
        }
    }


    std::vector<std::vector<std::vector<double> > >  getGraphletLaplacians(){


        std::vector<std::vector<unsigned int> > graphletToOrbits{ { 0},{ 1,2 },{ 3 },{4,5},{6,7},{8},{9,10,11},{12,13},{14} };
        std::vector<std::vector<std::vector<double> > > graphlet_laplacians;

        for (unsigned int graphlet=0; graphlet<9;graphlet++) {
            graphlet_laplacians.push_back(std::vector<std::vector<double> > ());
            std::vector<unsigned int> orbits = graphletToOrbits.at(graphlet);
            std::vector<double> correctedRow = std::vector<double>();

            for (int row = 0; row < this->getNrOfNodes(); row++) {
                correctedRow.clear();
                this->getOverCountCorrectedRowOverOrbits(orbits, row, correctedRow);

                for (int col= 0; col < this->getNrOfNodes(); col++) {
                    if (col != row) {correctedRow[col] *= -1;}
                }
                graphlet_laplacians[graphlet].push_back(correctedRow);
            }
        }
        return graphlet_laplacians;
    }


    std::vector<std::vector<std::vector<double> > >  getGraphletSizeCorrectedGraphletLaplacians(){

        std::vector<std::vector<unsigned int> > graphletToOrbits{ { 0},{ 1,2 },{ 3 },{4,5},{6,7},{8},{9,10,11},{12,13},{14} };

        std::vector<std::vector<std::vector<double> > > graphlet_laplacians;

        for (unsigned int graphlet=0; graphlet<9;graphlet++) {
            graphlet_laplacians.push_back(std::vector<std::vector<double> > ());
            std::vector<unsigned int> orbits = graphletToOrbits.at(graphlet);
            std::vector<double> summedRow = std::vector<double>();

            for (int row = 0; row < this->getNrOfNodes(); row++) {
                summedRow.clear();
                this->getGraphletSizeCorrectedRowOverOrbits(orbits, row, summedRow);

                for (int col = 0; col < this->getNrOfNodes(); col++) {
                    if (col != row) {summedRow[col] *= -1;}
                }
                graphlet_laplacians[graphlet].push_back(summedRow);
            }
        }
        return graphlet_laplacians;
    }



private:
    std::vector<std::vector<std::vector<int64> > > vector3D;

    void allocateMemory(int x, int y, int z){
        for(int i = 0; i < x; ++i)
            {
                this->vector3D.push_back(std::vector<std::vector<int64> >());
                for(int j(0); j < y; ++j)
                {
                    this->vector3D.at(i).push_back(std::vector<int64 >());
                    for(int k(0); k < z; ++k)
                    {
                        this->vector3D.at(i).at(j).push_back(0.);
                    }
                }
            }
        }

};


#endif //NCOUNT2_LCOUNT3DVECTOR_H
