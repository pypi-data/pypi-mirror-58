#include "Counter.h"
#include "RedundancyChecker.h"
#include "Writer.h"
#include "InputParser.h"
#include "Graph.h"


int main(int argc, char **argv) {


    InputParser input(argc, argv);
//    std::cout<<" argc: "<<argc<<std::endl;
//    std::cout<<"argv: "<<argv<<std::endl;
    if(input.cmdOptionExists("-h") || input.cmdOptionExists("--help") || argc==1){
        std::cout<<"Hello baby!!!"<<std::endl;
        std::cout<<"-i input network file in leda format (.gw file extension)"<<std::endl;
        std::cout<<"-o prefix for the graphlet laplacian output files. A suffix will be appended : <prefix>_<orbitNumber>.csv"<<std::endl;
        std::cout<<"-5nodes count up to 5 nodes in a graphlet. 4 nodes considered by default"<<std::endl;
        std::cout<<"If no output prefix is given, the Graphlet Laplacian files are outputed in same directory as the input network."<<std::endl;
        std::cout<<"(Make sure the output directory exists, this code does not make directories. )"<<std::endl;
    }

    //todo , fix this ugly mess and figure out how to set a debug flag at compile time
    std::string inputFile = input.getCmdOption("-i");
    if (!inputFile.empty()){
        std::cout<<inputFile<<std::endl;
    } else {
        //inputFile= "./test/networks_for_integration_tests/ER_100_0.05.leda";
        //inputFile= "./scratch/graphlet_laplacian_4nodes.gw";
        inputFile ="../test/PPI_exp_950.edgelist";
        //inputFile ="../PPI_exp.gw";
    }

    std::string outputPrefix = input.getCmdOption("-o");
    if (!outputPrefix.empty()){
        std::cout<<"Output file prefix: "<< outputPrefix<<std::endl;
    } else {
        outputPrefix = inputFile.substr( 0,inputFile.find_last_of('.'));
        std::cout<<"No output prefix was given, using: "<< outputPrefix<<std::endl;
    }

    bool five_nodes;
    std::string nodes = input.getCmdOption("-nodes");
    if (!nodes.empty()){
        std::cout<<"counting 5 nodes"<<std::endl;
        five_nodes=true;

    } else {
        std::cout<<"No output prefix was given, using: "<< outputPrefix<<std::endl;
        five_nodes=false;
    }


    five_nodes=false;
    FILE *out = fopen("./test.txt", "w");
    char const *outname = "test.txt";
    five_nodes=false;
    Graph g = Graph(inputFile);


    //allocate space for graphlet laplacian
    int nrOfOrbits = 15;
    if (five_nodes){
        nrOfOrbits=73;
    }



    Counter counter = Counter();
    std::cout<<g.get_neighbours_k_distance(1,9).size()<<std::endl;
    return 0;
    Lcount3D& laplacians = counter.count(g,  five_nodes, outputPrefix);

    return 0;
}
