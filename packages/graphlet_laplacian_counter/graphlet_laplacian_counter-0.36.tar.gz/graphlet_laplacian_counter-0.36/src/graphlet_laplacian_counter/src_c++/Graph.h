//
// Created by Sam Windels on 17/12/2019.
//

#ifndef NCOUNT3_GRAPH_H
#define NCOUNT3_GRAPH_H

#include <vector>
#include <set>

class Graph{
public:
    bool connect(int i, int j);
    bool connected(int i, int j);

    Graph(std::string inputfile);
    Graph(std::vector<int>& src_nodes, std::vector<int>& dst_nodes);
    std::vector<int> get_neighbours(int node);
    int degree(int node);
    int get_V();
    std::vector<int> get_neighbours_k_distance(int node, int distance);

private:

    //used to check if nodes are connected (log(1) time)
    char **adjmat;

    void init_from_leda(FILE *f);
    void init_from_edgelist(FILE *f);

    //used to iterate ove a nodes neighbours (log(1) time)
    std::vector<std::vector<int> > node_2_edges;
    void init_from_edgelist_helper(int V, int E_undir, std::vector<int>& src_nodes, std::vector<int>& dst_nodes);
    void get_neighbours_k_distance(int node, int distance, std::set<int>& neighbors, std::vector<int>& distance_nodes_visited );

};
#endif //NCOUNT3_GRAPH_H
