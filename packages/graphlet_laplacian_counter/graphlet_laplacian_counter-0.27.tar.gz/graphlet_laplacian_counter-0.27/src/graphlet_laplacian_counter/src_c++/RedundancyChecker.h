//
// Created by windels on 24/01/18.
//

// template reference: https://stackoverflow.com/questions/495021/why-can-templates-only-be-implemented-in-the-header-file

//reduncancy rules unweighted network: https://media.nature.com/original/nature-assets/srep/2014/140401/srep04547/extref/srep04547-s1.pdf
//Yaveroğlu, Ö. N., Malod-Dognin, N., Davis, D., Levnajic, Z., Janjic, V., Karapandza, R., ... & Pržulj, N. (2014).
// Revealing the hidden language of complex networks. Scientific reports, 4.



#ifndef NCOUNT_REDUNDANCYCHECKER_H
#define NCOUNT_REDUNDANCYCHECKER_H

#include <iostream>
#include <string>
#include "Lcount3DArray.h"
typedef long long int64; // sadly, long long is not standard in C++ ... yet

#define DEGREE(x) (edges_for[x + 1] - edges_for[x])


////TODO put these over count corrections on the correct place
//    /* times counted per graphlet type */
const int overcount[] = {2, 6, 2, 6, 8, 4, 12, 24, 2, 2, 24, 2, 4, 4, 10, 4,
                         4, 8, 8, 12, 14, 12, 12, 20, 28, 36, 48, 72, 120};
//
// graphlet types corresponding to each node type
const int ntype2gtype[] = {0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9,
                           9,  9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 15, 15, 15, 15,
                           16, 16, 16, 16, 17, 17, 18, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22, 22,
                           22, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 26, 27, 27, 28};



class RedundancyChecker{

public:


    void sanityCheckSumOfRows(Lcount3D &lcount ){
        for (int orbit =0; orbit <lcount.getNrOfOrbits(); orbit++){
            for (int row =0; row < lcount.getNrOfNodes(); row++){
              if (lcount.getOffDiagonalSum(orbit, row)!=lcount.getCount(orbit,row,row) ){
                  std::cout<< "sanity check failed on orbit :" << orbit <<std::endl;
                  break;
              }
            }
        }
    }



    void checkRedundanciesLcount(Lcount3D& lcount ){
        for(int node =0; node<lcount.getNrOfNodes(); node++){
            checkRedundancyConstraints4Nodes(lcount.getGDV(node));
        }
    }

    void debugRedundanciesLcount(Lcount3D& lcount, int64 **ncount, int **edges_for){

        for(int node =0; node<10; node++){
            int64* ncountGDV= getGdvFromNcount(ncount,node,edges_for);
            printGDV(ncountGDV);
            delete ncountGDV;
            int64* gdv= lcount.getGDV(node);
            checkRedundancyConstraints4Nodes(gdv);
            //checkRedundancyConstraints5Nodes(gdv);
            delete gdv;
        }
    }

    void printGDV(int64 gdv[]){
        for(int k = 0; k < 15; k++) {
            std::cout<<gdv[k]<<' ';
        }
        std::cout<<std::endl;

    }

    int64* getGdvFromNcount(int64 **ncount, int j, int **edges_for){

        int64 *gdv= new int64[73];

        gdv[0]=DEGREE(j);
//        std::cout<<gdv[0]<<' ';
        for(int k = 0; k < 72; k++) {
            assert(ncount[k][j]%overcount[ntype2gtype[k]] == 0);
            gdv[k+1]=ncount[k][j]/overcount[ntype2gtype[k]];
//            std::cout<<gdv[k+1]<<' ';
        }
//        std::cout<<std::endl;
        return gdv;

    }


    void checkRedundanciesNcount(int64 **ncount, int V, int **edges_for){
        for(int j = 0; j < V; j++)
        {
            int64* gdv = getGdvFromNcount( ncount, j, edges_for);
            checkRedundancyConstraints4Nodes(gdv);
            checkRedundancyConstraints5Nodes(gdv);
        }
    }

    void checkRedundancyConstraints4Nodes(int64 gdv[]){


            if (!this->redundancyCheck1(gdv)){
                std::cout<<"redundancy check 1 failed on node "<<std::endl;
            }

            if (!redundancyCheck2(gdv)){
                std::cout<<"redundancy check 2 failed on node "<<std::endl;
            }

            if (!redundancyCheck3(gdv)){
                std::cout<<"redundancy check 3 failed on node "<<std::endl;
            }

            if (!redundancyCheck4(gdv)){
                std::cout<<"redundancy check 4 failed on node "<<std::endl;
            }
        }

    void checkRedundancyConstraints5Nodes(int64 gdv[]){


        if (!this->redundancyCheck5(gdv)){
            std::cout<<"redundancy check 5 failed on node "<<std::endl;
        }

        if (!redundancyCheck6(gdv)){
            std::cout<<"redundancy check 6 failed on node "<<std::endl;
        }

        if (!redundancyCheck7(gdv)){
            std::cout<<"redundancy check 7 failed on node "<<std::endl;
        }

        if (!redundancyCheck8(gdv)){
            std::cout<<"redundancy check 8 failed on node "<<std::endl;
        }

        if (!this->redundancyCheck9(gdv)){
            std::cout<<"redundancy check 9 failed on node "<<std::endl;
        }

        if (!redundancyCheck10(gdv)){
            std::cout<<"redundancy check 10 failed on node "<<std::endl;
        }

        if (!redundancyCheck11(gdv)){
            std::cout<<"redundancy check 11 failed on node "<<std::endl;
        }

        if (!redundancyCheck12(gdv)){
            std::cout<<"redundancy check 12 failed on node "<<std::endl;
        }

        if (!this->redundancyCheck13(gdv)){
            std::cout<<"redundancy check 13 failed on node "<<std::endl;
        }

        if (!redundancyCheck14(gdv)){
            std::cout<<"redundancy check 14 failed on node "<<std::endl;
        }

        if (!redundancyCheck15(gdv)){
            std::cout<<"redundancy check 15 failed on node "<<std::endl;
        }

//        if (!redundancyCheck16(gdv)){
//            std::cout<<"redundancy check 16 failed on node "<<std::endl;
//        }

        if (!redundancyCheck17(gdv)){
            std::cout<<"redundancy check 17 failed on node "<<std::endl;
        }


    }



//
//    int64 fact(int64 N){
//        if(N==0) return (int64)1;
//        if(N>0) return N*fact(N-1);
//    };
//
//
//    int64 choose(int64 N, int64 K){
//        if(N<K) return 0;
//        return(fact(N)/(fact(K)*fact(N-K)));
//    };


    // Returns value of Binomial Coefficient C(n, k)
    int64 choose(int64 n, int64 k)
    {


        // Base Cases
        if (k==0 || k==n)
            return 1;

        if (k<0)
            return 0;


        // Recur
//        return  choose(n-1, k-1) + choose(n-1, k);

        //product def http://math.wikia.com/wiki/Binomial_coefficient
        double  coefficient=1;
        for (int j =1; j<=k;j++){
            coefficient*=(double) (n-j+1)/j;
        }
        //std::cout<<"coef "<<coefficient<<std::endl;
        return (int64)coefficient;

    }


    // ----------------------------------------------------------------------------------------------------------------
    // 4 ORBITS

    //1) choose(C0 2)=C2+C3

    bool redundancyCheck1(int64 gdv[]){
//        std::cout<<gdv[0]<<' '<<gdv[2]<<' '<<gdv[3]<<std::endl;
//        std::cout<<choose(gdv[0], (int64) 2)<<' '<<(gdv[2]+gdv[3])<<std::endl;
//        std::cout<<gdv[0]<<' '<<gdv[2]<<' '<<gdv[3]<<std::endl;
        return this->choose(gdv[0], (int64) 2)==(gdv[2]+gdv[3]);
    }

    //2) choose(C2 1) choose(C0-2 1) = 3C7 +2C11+C13
    bool redundancyCheck2(int64 gdv[]){
        return (this->choose(gdv[2], (int64) 1) * this->choose(gdv[0]-2,(int64)1))==(3*gdv[7]+2*gdv[11]+gdv[13]);
    }

    //3) choose(C1 1) choose(C0-1 1) = C5 +2C8 +C10+2C12
    bool redundancyCheck3(int64 gdv[]){
        return (this->choose(gdv[1], (int64) 1) * this->choose(gdv[0]-1,(int64)1))==(gdv[5]+2*gdv[8]+gdv[10]+2*gdv[12]);
    }

    //4) choose(C3 1) Choose(C0-2 1) = C11 + 2C13 + 3C14

    bool redundancyCheck4(int64 gdv[]){
        return (this->choose(gdv[3], (int64) 1) * this->choose(gdv[0]-2,(int64)1))==(gdv[11]+2*gdv[13]+3*gdv[14]);
    }

    // ----------------------------------------------------------------------------------------------------------------
    // 5 ORBITS

    //5) choose(C4 1) Choose(C0-1 1) = C16 +C29+2C34+2C36+2C46+C51+2C52+C59

    bool redundancyCheck5(int64 gdv[]){
        return (this->choose(gdv[4], (int64) 1) * this->choose(gdv[0]-1,(int64) 1))==(gdv[16]+gdv[29]+2*gdv[34]+2*gdv[36]+2*gdv[46]+gdv[51]+2*gdv[52]+gdv[59]);
    }

    //6)

    bool redundancyCheck6(int64 gdv[]){
        return (this->choose(gdv[5], (int64) 1) * this->choose(gdv[0]-2,(int64) 1))==(2*gdv[21]+gdv[26]+2*gdv[30]+2*gdv[38]+2*gdv[47]+gdv[48]+gdv[553]+gdv[60]);
    }

    //7)

    bool redundancyCheck7(int64 gdv[]){
        return (this->choose(gdv[6], (int64) 1) * this->choose(gdv[0]-1,(int64) 1))==(gdv[20]+gdv[32]+gdv[37]+gdv[40]+2*gdv[49]+2*gdv[54]);
    }

    //8)

    bool redundancyCheck8(int64 gdv[]){
        return (this->choose(gdv[7], (int64) 1) * this->choose(gdv[0]-3,(int64) 1))==(4*gdv[23]+2*gdv[33]+gdv[42]+gdv[55]);
    }

    //9)


    bool redundancyCheck9(int64 gdv[]){
        return (this->choose(gdv[8], (int64) 1) * this->choose(gdv[0]-2,(int64) 1))==(gdv[38]+3*gdv[50]+gdv[53]+2*gdv[63]+gdv[64]+gdv[68]);
    }


    bool redundancyCheck10(int64 gdv[]){
        return (this->choose(gdv[9], (int64) 1) * this->choose(gdv[0]-1,(int64) 1))==(gdv[28]+gdv[43]+gdv[51]+gdv[59]+2*gdv[62]+2*gdv[65]);
    }


    bool redundancyCheck11(int64 gdv[]){
        return (this->choose(gdv[10], (int64) 1) * this->choose(gdv[0]-2,(int64) 1))==(gdv[26]+2*gdv[41]+gdv[48]+gdv[53]+2*gdv[57]+2*gdv[64]+2*gdv[66]);
    }


    bool redundancyCheck12(int64 gdv[]){
        return (this->choose(gdv[11], (int64) 1) * this->choose(gdv[0]-3,(int64) 1))==(2*gdv[33]+2*gdv[42]+4*gdv[44]+3*gdv[58]+2*gdv[61]+gdv[67]);
    }


    bool redundancyCheck13(int64 gdv[]){
        return (this->choose(gdv[12], (int64) 1) * this->choose(gdv[0]-2,(int64) 1))==(gdv[47]+gdv[60]+gdv[63]+gdv[66]+2*gdv[68]+3*gdv[70]);
    }


    bool redundancyCheck14(int64 gdv[]){
        return (this->choose(gdv[13], (int64) 1) * this->choose(gdv[0]-3,(int64) 1))==(gdv[42]+3*gdv[55]+2*gdv[61]+2*gdv[67]+4*gdv[69]+2*gdv[71]);
    }


    bool redundancyCheck15(int64 gdv[]){
        return (this->choose(gdv[1], (int64) 2))==(gdv[6]+gdv[8]+gdv[9]+gdv[12]+gdv[17]+gdv[25]+gdv[34]+gdv[37]+gdv[40]+2*gdv[49]+gdv[51]+gdv[52]+2*gdv[54]+gdv[59]+2*gdv[62]+2*gdv[65]);
    }

    //16 ) choose(C3 2) C13 + 3C14 +C44+C61+C67 +2C69 + 2C71+3C72


    bool redundancyCheck16(int64 gdv[]){
        return (this->choose(gdv[3], (int64) 2))==(gdv[13]+3*gdv[14]+gdv[44]+gdv[61]+gdv[67]+2*gdv[69]+2*gdv[71]+3*gdv[72]);
    }


    bool redundancyCheck17(int64 gdv[]){
        return (this->choose(gdv[2], (int64) 1) * this->choose(gdv[3],(int64) 1))==(2*gdv[11]+2*gdv[13]+gdv[33]+2*gdv[42]+3*gdv[55]+3*gdv[58]+gdv[61]+2*gdv[67]+gdv[71]);
    }

};

#endif //NCOUNT_REDUNDANCYCHECKER_H
