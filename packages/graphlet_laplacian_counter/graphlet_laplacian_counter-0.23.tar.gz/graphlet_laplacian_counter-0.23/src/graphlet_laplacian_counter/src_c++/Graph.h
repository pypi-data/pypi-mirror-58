//
// Created by Sam Windels on 17/12/2019.
//

#ifndef NCOUNT3_GRAPH_H
#define NCOUNT3_GRAPH_H

#include <vector>

class Graph{
public:
    bool connect(int i, int j);
    bool connected(int i, int j);

    Graph(std::string inputfile);
    Graph(std::vector<int>& src_nodes, std::vector<int>& dst_nodes);
    std::vector<int> get_neighbours(int node);
    int degree(int node);
    int get_V();
    /*template<typename FUNCTION>
    inline void for_each(int* x, int y, FUNCTION&& f) {
        for (x = this->edges_for[y]; x != edges_for[y + 1]; x++) {
            std::forward<FUNCTION>(f)(x);
        }
    };*/

    /*inline void for_each(int* x, int y) {
        for (x = this->edges_for[y]; x != edges_for[y + 1]; x++) {
            std::forward<int*>(x);
        }
    };*/


    #define for_each(x,y) for(x = this->edges_for[y]; x != this->edges_for[y+1]; x++)

    /*template<typename FUNCTION>
    inline void loop(int n, FUNCTION&& f) {
        for (int i = 0; i < n; ++i) {
            std::forward<FUNCTION>(f)(i);
        }
    }*/

private:

    //used to check if nodes are connected (log(1) time)
    char **adjmat;

    void init_from_leda(FILE *f);
    void init_from_edgelist(FILE *f);

    //used to iterate ove a nodes neighbours (log(1) time)
    std::vector<std::vector<int> > node_2_edges;
    void init_from_edgelist_helper(int V, int E_undir, std::vector<int>& src_nodes, std::vector<int>& dst_nodes);


};
#endif //NCOUNT3_GRAPH_H
