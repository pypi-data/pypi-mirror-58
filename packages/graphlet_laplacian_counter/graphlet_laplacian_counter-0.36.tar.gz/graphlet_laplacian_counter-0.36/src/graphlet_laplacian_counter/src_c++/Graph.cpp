//
// Created by Sam Windels on 17/12/2019.
//

#include <cstdlib>
#include <cstdio>
#include <memory>
#include <string>
#include <set>
#include <iostream>
#include "Graph.h"


void die(char *msg) {
    fprintf(stderr, "ERROR: %s\n", msg);
    exit(1);
}

bool Graph::connect(int i, int j) {
    return this->adjmat[i][(j)/8] |= 1<<((j)%8);
}

bool Graph::connected(int i, int j) {
    return this->adjmat[i][(j)/8] & (1<<((j)%8));
}

void Graph::init_from_edgelist(FILE *f) {

    int i;

    std::vector<int> src_nodes, dst_nodes;
    int src = -1, dst = -1;
    int V = -1;
    int E_undir = 0;
    while (fscanf(f, "%d %d", &src, &dst) != EOF) {
        if (src > V) V = src;
        if (dst > V) V = dst;
        src_nodes.push_back(src);
        dst_nodes.push_back(dst);
        E_undir++;
    }
    V = V + 1; //expecting a nodelist from 0-n
    this->init_from_edgelist_helper(V,E_undir,src_nodes, dst_nodes);
}

void Graph::init_from_edgelist_helper(int V, int E_undir, std::vector<int>& src_nodes, std::vector<int>& dst_nodes){

    int i;
    adjmat = new char *[V];
    for (i = 0; i < V; i++) {
        /* calloc zeroes the memory for us */
        adjmat[i] = (char *) calloc(V / 8 + 1, sizeof(char));
        if (!adjmat[i]) {
            perror("calloc");
            exit(1);
        }

        this->connect(i, i); /* optimization hack */

    }

    //initialize nodes_2_edges
    for (i = 0; i < V; i++) {
        this->node_2_edges.push_back(std::vector<int>());
    }

    int src, dst;
    for (i = 0; i < E_undir; i++) {
        src = src_nodes[i];
        dst = dst_nodes[i];

        if (src == dst) continue; /* ignore self-loops */

        if (!this->connected(src, dst) and !this->connected(dst, src) ) {
            this->node_2_edges[src].push_back(dst);
            this->node_2_edges[dst].push_back(src);

            this->connect(src, dst);
            this->connect(dst, src);

        }
    }
}

void Graph::init_from_leda(FILE *f) {

    int V, E_undir, i;

    fscanf(f, "LEDA.GRAPH\n");
    fscanf(f, "%*s\n");
    fscanf(f, "%*s\n");

    do { if( fscanf(f, "%d\n", &V) < 0 ) V = -1; }
    while(V < 0);

    char **node_names = new char*[V];

    char buf[101];
    for(i = 0; i < V; i++)
    {
        if(fscanf(f, "|{ %100[^}] }|\n", buf) < 1) die( (char *)"Invalid input file");
        node_names[i] = strdup(buf);
        assert(node_names[i] != NULL);
    }

    fscanf(f, "%d", &E_undir);

    assert(E_undir >= 0);


    adjmat = new char*[V];
    for(i = 0; i < V; i++)
    {
        /* calloc zeroes the memory for us */
        adjmat[i] = (char *) calloc(V/8+1, sizeof(char));
        if(!adjmat[i]) { perror("calloc"); exit(1); }

        this->connect(i,i); /* optimization hack */

    }


    //initialize nodes_2_edges
    for(i = 0; i < V; i++)
    {
        this->node_2_edges.push_back(std::vector<int>());
    }


    /* add data to linked list for intermediate storage */
    for(i = 0; i < E_undir; i++) {
        int src = -1, dst = -1;
        fscanf(f, "%d %d %*d %*s", &src, &dst);
        src -= 1; /* LEDA graph files are 1-indexed */
        dst -= 1;

        if (src < 0 || dst < 0) {
            fprintf(stderr, "Error: node numbers must be greater than zero.\n");
            exit(1);
        }

        if (src == dst) continue; /* ignore self-loops */

        if (!this->connected(src, dst) and !this->connected(dst, src))
        {

            this->node_2_edges[src].push_back(dst);
            this->node_2_edges[dst].push_back(src);

            this->connect(src, dst);
            this->connect(dst, src);

        }
    }
}

std::vector<int> Graph::get_neighbours(int node) {
    return this->node_2_edges[node];
}

int Graph::degree(int node) {
    return this->node_2_edges[node].size();
}

int Graph::get_V() {
    return this->node_2_edges.size();
}


Graph::Graph(std::string inputFile) {

    int stringSize= inputFile.size();
    std::string suffix = (3 > 0 && stringSize > 3) ? inputFile.substr(stringSize- 3) : "";

    FILE *f= fopen( inputFile.c_str(), "r");
    if (f== NULL) {
        perror ("Error opening network file");
        exit(1);};

    if (suffix.compare(std::string(".gw")) ==0){
        this->init_from_leda(f);
    }
    else{
        this->init_from_edgelist(f);
    }
}

Graph::Graph(std::vector<int>& src_nodes, std::vector<int>& dst_nodes) {

    int E_undir = src_nodes.size();
    int V = -1;
    for(std::vector<int>::iterator node= src_nodes.begin(); node != src_nodes.end(); ++node) {
       if (*node>V) V = *node;
    }
    for(std::vector<int>::iterator node= dst_nodes.begin(); node != dst_nodes.end(); ++node) {
        if (*node>V) V = *node;
    }

    V = V + 1; //expecting a nodelist from [0,..., (V-1)]
    this->init_from_edgelist_helper(V,E_undir,src_nodes, dst_nodes);

}

std::vector<int> Graph::get_neighbours_k_distance(int node, int distance) {
    std::set<int> neighbors = std::set<int>();
    std::vector<int> distance_nodes_visited = std::vector<int>();

    for (unsigned int i = 0; i<get_V(); i++){
       distance_nodes_visited.push_back(-1);
    }

    std::vector<int>::iterator neighbor_it;
    int neighbor;
    for (neighbor_it = this->node_2_edges[node].begin(); neighbor_it<this->node_2_edges[node].end(); neighbor_it++){
        neighbor = *neighbor_it;
        if (distance>0 and distance > distance_nodes_visited[neighbor]) {
            this->get_neighbours_k_distance(neighbor, distance-1, neighbors, distance_nodes_visited);
        }
        distance_nodes_visited[neighbor]=distance;
        neighbors.insert(neighbor);
    }
    std::vector<int> neighbors_vector =  std::vector<int> (neighbors.begin(), neighbors.end());
    std::sort(neighbors_vector.begin(), neighbors_vector.end());
    return neighbors_vector;

}


void Graph::get_neighbours_k_distance(int node, int distance, std::set<int>& neighbors, std::vector<int>& distance_nodes_visited ) {

    std::vector<int>::iterator neighbor_it;
    int neighbor;
    for (neighbor_it = this->node_2_edges[node].begin(); neighbor_it<this->node_2_edges[node].end(); neighbor_it++){
        //std::cout<<"hit"<<std::endl;
        neighbor = *neighbor_it;
        //std::cout<<node<<' '<<neighbor<<std::endl;
        if (distance>0 and distance > distance_nodes_visited[neighbor]) {
            this->get_neighbours_k_distance(neighbor, distance-1, neighbors, distance_nodes_visited);
        }
        distance_nodes_visited[neighbor]=distance;
        neighbors.insert(neighbor);
    }
}

