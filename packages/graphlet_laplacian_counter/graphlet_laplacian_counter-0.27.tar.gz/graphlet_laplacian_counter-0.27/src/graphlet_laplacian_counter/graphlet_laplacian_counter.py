from array import array
import numpy as np
import networkx as nx
import cppyy
import os
run_dir =os.path.dirname(os.path.abspath(__file__))
cppyy.include(run_dir + '/src_c++/Counter.cpp')
cppyy.include(run_dir + '/src_c++/Graph.cpp')


class GrahpletLaplacianCounter(object):

    """Python wrapper for C++ Graphlet Laplacian counter """

    def __init__(self):
        from cppyy.gbl import count_from_vectors, count_from_vectors_single_node
        self.__count_from_vectors = count_from_vectors
        self.__count_from_vectors_single_node = count_from_vectors_single_node

    def count_from_adj_matrix(self, A, node=None):
        """returns all graphlet laplacians matrices for up to 4 node graphlets.
        If a node is given, the laplacians are computed only for that single node.

        """
        nodes_src, nodes_dst = np.nonzero(A)
        nodes_src = nodes_src.tolist()
        nodes_dst = nodes_dst.tolist()
        if node is None:
            return np.asanyarray(self.__count_from_vectors(nodes_src,nodes_dst))
        else:
            GL_s = np.asanyarray(self.__count_from_vectors_single_node(nodes_src,nodes_dst,node))
            for i, L in enumerate(GL_s):
                L_row = L[node,:]
                L[:,node]= L_row.T 
                GL_s[i]=L
            return GL_s



def main():
    # G = nx.read_edgelist(run_dir+'/src_c++/PPI_exp_950.edgelist')
    G = nx.read_edgelist('../PPI_exp_950.edgelist')
    A = nx.to_numpy_matrix(G)

    counter =  GrahpletLaplacianCounter()
    GL_s = counter.count_from_adj_matrix(A,0)
    pass

if __name__ == "__main__":
    main()

