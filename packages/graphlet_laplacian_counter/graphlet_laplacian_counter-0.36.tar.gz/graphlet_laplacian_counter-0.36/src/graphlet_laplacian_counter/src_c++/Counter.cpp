#include "Counter.h"
#include "RedundancyChecker.h"
#include "Graph.h"
#include "Writer.h"

#include <memory>
#include <iostream>
#include <cstdio>
#include <vector>




char const *cnames[] = {"P3_A [end]", "P3_B [mid]", "C3_A", "P4_A [end]",
                  "P4_B [mid]", "CLAW_A [outer]", "CLAW_B [center]", "C4_A", "FLOW_A [stem]",
                  "FLOW_B [petals]", "FLOW_C [center]", "DIAM_A [deg2]", "DIAM_B [deg3]",
                  "K4_A", "P5_A", "P5_B", "P5_C", "X10_A", "X10_B", "X10_C", "X10_D", "X11_A",
                  "X11_B", "X12_A", "X12_B", "X12_C", "X13_A", "X13_B", "X13_C", "X13_D",
                  "X14_A", "X14_B", "X14_C", "C5_A", "X16_A", "X16_B", "X16_C", "X16_D",
                  "X17_A", "X17_B", "X17_C", "X17_D", "X18_A", "X18_B", "X19_A", "X19_B",
                  "X19_C", "X19_D", "X20_A", "X20_B", "X21_A", "X21_B", "X21_C", "X22_A",
                  "X22_B", "X23_A", "X23_B", "X23_C", "X24_A", "X24_B", "X24_C", "X25_A",
                  "X25_B", "X25_C", "X26_A", "X26_B", "X26_C", "X27_A", "X27_B", "X28_A",
                  "X28_B", "K5_A"};

std::vector<std::vector<std::vector<double> > > Counter::count_from_vectors_single_node(std::vector<int> src_nodes, std::vector<int> dst_nodes, int node){

    Graph g = Graph(src_nodes, dst_nodes);
    int nr_of_orbits = 15;

    Lcount3DVector lcount3DVector = Lcount3DVector(nr_of_orbits, g.get_V());
    Lcount3D &laplacians = lcount3DVector;

    bool five_nodes = false;
    std::vector<int> nodes_to_run = g.get_neighbours_k_distance(node,3);
    //std::vector<int> nodes_to_run = std::vector<int>();
    //nodes_to_run.push_back(node);
    std::cout<<"SIZE: "<< nodes_to_run.size()<<'/'<<g.get_V()<<std::endl;
    this->count_subroutine(g,laplacians,five_nodes, nodes_to_run);
    return lcount3DVector.getGraphletLaplacians();
}





std::vector<std::vector<std::vector<double> > > Counter::count_from_vectors(std::vector<int> src_nodes, std::vector<int> dst_nodes){

    Graph g = Graph(src_nodes, dst_nodes);
    int nr_of_orbits = 15;

    Lcount3DVector lcount3DVector = Lcount3DVector(nr_of_orbits, g.get_V());
    Lcount3D &laplacians = lcount3DVector;

    bool five_nodes = false;
    this->count_subroutine(g,laplacians,five_nodes);
    //return std::vector<std::vector<std::vector<int64> > >();
    return lcount3DVector.getGraphletLaplacians();
}


Lcount3D& Counter::count(Graph& g, bool five_nodes, std::string output_prefix) {


    int nrOfOrbits = 15;
    if (five_nodes){
        nrOfOrbits=73;
    }

    //Lcount3DArray lcount3DArray =Lcount3DArray (nrOfOrbits,V);
    //laplacians = lcount3DArray;

    Lcount3DVector lcount3DVector = Lcount3DVector(nrOfOrbits, g.get_V());
    //laplacians = lcount3DVector;

    //Lcount3DSparse lcount3DSparse = Lcount3DSparse(nrOfOrbits,V);
    //laplacians = lcount3DSparse

    Lcount3D &laplacians = lcount3DVector;
    this->count_subroutine(g,laplacians,five_nodes);

    Writer writer = Writer();
    //FILE *out, char const *outname, std::string outputPrefix,
    writer.write_graphlet_laplacian_edgelist(laplacians,output_prefix);
}

Lcount3D& Counter::count_subroutine(Graph& g, Lcount3D &laplacians, bool five_nodes, std::vector<int> nodes_to_run){


    int V = g.get_V();

    int64 gcount[29] = {};
    int64 *ncount[72]{};
    /* allocate space for node type counts */

    for(int i = 0; i < 72; i++)
    {
        ncount[i] = (int64 *) calloc(V, sizeof(int64));
        if(!ncount[i]) { perror("calloc"); exit(1); }
    }

    /* start counting */

    if (nodes_to_run.size()==0) {
        nodes_to_run = std::vector<int>();
        for (int i = 0; i < V; i++) {
            nodes_to_run.push_back(i);
        }
    }
    int a, b, c, d, e, x;
    std::vector<int>::iterator pb, pc, pd, pe;
    for(std::vector<int>::iterator it=nodes_to_run.begin(); it<nodes_to_run.end(); it++)
    {
        a = *it;
        if (a%100==0.0)
            std::cout<<"node: "<<a+1<<'/'<<V<< std::endl;
#if PROGRESS_INFO
        fprintf(stderr, "\rnode # %5d (%.1f%%) [%d min elapsed]", a,
              100.0 * (float) a / V, (time(0) - start_time) / 60);
#endif

        std::vector<int> neighbours_a = g.get_neighbours(a);
        for(pb = neighbours_a.begin(); pb != neighbours_a.end(); ++pb) {
            b = *pb;
            if(b == a) continue;

            laplacians.addCount(0,a,b);

            std::vector<int> neighbours_b = g.get_neighbours(b);
            for(pc = neighbours_b.begin(); pc != neighbours_b.end(); ++pc) {
                c = *pc;
                if(c == a || c == b) continue;

                /* count adjacent edges */
                int deg3_a = 0, deg3_b = 0, deg3_c = 0;

                // The "!!" is a double negation, which maps any non-zero integer to 1
                x = !!g.connected(a,b); deg3_a += x; deg3_b += x;
                x = !!g.connected(a,c); deg3_a += x; deg3_c += x;
                x = !!g.connected(b,c); deg3_b += x; deg3_c += x;


                if(deg3_a == 1)
                {
                    gcount[0]++; /* path */
                    ncount[P3_A][a]++; ncount[P3_B][b]++; ncount[P3_A][c]++;
                    laplacians.addCount(P3_A+1, a,{ b,c} );

                    laplacians.addCount(P3_B+1, b,{ a,c} );

                    laplacians.addCount(P3_A+1, c,{ a,b} );


                    // look for claws
                    if(g.degree(b) > 2) {
                        for(pd = neighbours_b.begin(); pd != neighbours_b.end(); ++pd) {
                            d = *pd;
                            if (g.connected(a, d) + g.connected(c, d) == 0) {
                                // look for X11
                                if (g.degree(b) > 3 and five_nodes){
                                    for(pe = neighbours_b.begin(); pe != neighbours_b.end(); ++pe) {
                                        e = *pe;
                                        if (g.connected(a, e) + g.connected(c, e) + g.connected(d, e) == 0) {
                                            gcount[10]++; /* X11 */
                                            ncount[X11_A][a]++;
                                            ncount[X11_B][b]++;
                                            ncount[X11_A][c]++;
                                            ncount[X11_A][d]++;
                                            ncount[X11_A][e]++;
                                        }
                                    }
                                }

                                gcount[3]++; /* Claw! */
                                ncount[CLAW_A][a]++;
                                ncount[CLAW_B][b]++;
                                ncount[CLAW_A][c]++;
                                ncount[CLAW_A][d]++;


                                laplacians.addCount(CLAW_A + 1, a, {b, c, d});
                                laplacians.addCount(CLAW_B + 1, b, {a, c, d});
                                laplacians.addCount(CLAW_A + 1, c, {a, b, d});
                                laplacians.addCount(CLAW_A + 1, d, {a, b, c});
                            }
                        }
                    }
                }
                else
                {
                    gcount[1]++; /* triangle */
                    ncount[C3_A][a]++; ncount[C3_A][b]++; ncount[C3_A][c]++;
                    laplacians.addCount(C3_A+1,a,{b,c});
                    laplacians.addCount(C3_A+1,b,{a,c});
                    laplacians.addCount(C3_A+1,c,{a,b});

                }

                std::vector<int> neighbours_c = g.get_neighbours(c);
                for(pd = neighbours_c.begin(); pd != neighbours_c.end(); ++pd) {
                    d = *pd;
                    if(d == a || d == b || d == c) continue;

                    /* classify most 4-node graphlets (excluding some claws) */

                    int deg4_a = deg3_a, deg4_b = deg3_b, deg4_c = deg3_c, deg4_d = 0;

                    x = !!g.connected(a,d); deg4_d += x; deg4_a += x;
                    x = !!g.connected(b,d); deg4_d += x; deg4_b += x;
                    x = !!g.connected(c,d); deg4_d += x; deg4_c += x;

                    int num_edges = deg4_a + deg4_b + deg4_c + deg4_d;

                    if(num_edges == 6)
                    {
                        gcount[2]++; /* P4 */
                        ncount[P4_A][a]++; ncount[P4_B][b]++; ncount[P4_B][c]++;
                        ncount[P4_A][d]++;


                        laplacians.addCount(P4_A+1,a,{b,c,d});;
                        laplacians.addCount(P4_B+1,b,{a,c,d});
                        laplacians.addCount(P4_B+1,c,{a,b,d});
                        laplacians.addCount(P4_A+1,d,{a,b,c});
                        if (five_nodes) {
                            for(pe = neighbours_b.begin(); pe != neighbours_b.end(); ++pe) {
                                e = *pe;
                                if (g.connected(a, e) + g.connected(c, e) + g.connected(d, e) == 0) {
                                    gcount[9]++; /* X10 */
                                    ncount[X10_B][a]++;
                                    ncount[X10_D][b]++;
                                    ncount[X10_C][c]++;
                                    ncount[X10_A][d]++;
                                    ncount[X10_B][e]++;

                                    laplacians.addCount(X10_B + 1, a, {b, d, d, e});
                                    laplacians.addCount(X10_D + 1, b, {a, c, d, e});
                                    laplacians.addCount(X10_C + 1, c, {a, b, d, e});
                                    laplacians.addCount(X10_A + 1, d, {a, b, c, e});
                                    laplacians.addCount(X10_B + 1, e, {a, b, c, d});
                                }
                            }
                        }
                    }
                    else if(num_edges == 10)
                    {
                        gcount[6]++; /* Diamond */
                        ncount[deg4_a == 3 ? DIAM_B : DIAM_A][a]++;
                        ncount[deg4_b == 3 ? DIAM_B : DIAM_A][b]++;
                        ncount[deg4_c == 3 ? DIAM_B : DIAM_A][c]++;
                        ncount[deg4_d == 3 ? DIAM_B : DIAM_A][d]++;

                        laplacians.addCount(deg4_a == 3 ? DIAM_B+1 : DIAM_A+1,a,{b,c,d});
                        laplacians.addCount(deg4_b == 3 ? DIAM_B+1 : DIAM_A+1,b,{a,c,d});
                        laplacians.addCount(deg4_c == 3 ? DIAM_B+1 : DIAM_A+1,c,{a,b,d});
                        laplacians.addCount(deg4_d == 3 ? DIAM_B+1 : DIAM_A+1,d,{a,b,c});
                    }
                    else if(num_edges == 12)
                    {
                        gcount[7]++; /* K4 */
                        ncount[K4_A][a]++; ncount[K4_A][b]++; ncount[K4_A][c]++;
                        ncount[K4_A][d]++;

                        laplacians.addCount(K4_A+1,a,{b,c,d});
                        laplacians.addCount(K4_A+1,b,{a,c,d});
                        laplacians.addCount(K4_A+1,c,{a,b,d});
                        laplacians.addCount(K4_A+1,d,{a,b,c});

                    }
                    else if(num_edges == 8) /* C4 or Flower */
                    {
                        if(deg4_b == 3 || deg4_c == 3)
                        {
                            gcount[5]++; /* Flower */
                            if(deg4_b == 3)
                            {
                                ncount[FLOW_A][a]++; ncount[FLOW_C][b]++;
                                ncount[FLOW_B][c]++; ncount[FLOW_B][d]++;

                                laplacians.addCount(FLOW_A+1,a,{b,c,d});
                                laplacians.addCount(FLOW_C+1,b,{a,c,d});
                                laplacians.addCount(FLOW_B+1,c,{a,b,d});
                                laplacians.addCount(FLOW_B+1,d,{a,b,c});
                                // only do this for half the cases, to reduce overcount

                                if (five_nodes) {
                                    for(pe = neighbours_b.begin(); pe != neighbours_b.end(); ++pe) {
                                        e = *pe;
                                        if (g.connected(a, e) + g.connected(c, e) + g.connected(d, e) == 0) {
                                            gcount[13]++; /* X14 */
                                            ncount[X14_A][a]++;
                                            ncount[X14_C][b]++;
                                            ncount[X14_B][c]++;
                                            ncount[X14_B][d]++;
                                            ncount[X14_A][e]++;
                                            laplacians.addCount(X14_A+1,a,{b,c,d,e});
                                            laplacians.addCount(X14_C+1,b,{a,c,d,e});
                                            laplacians.addCount(X14_B+1,c,{a,b,d,e});
                                            laplacians.addCount(X14_B+1,d,{a,b,c,e});
                                            laplacians.addCount(X14_A+1,e,{a,b,c,d});
                                        }
                                    }
                                }
                            }
                            else
                            {
                                ncount[FLOW_B][a]++; ncount[FLOW_B][b]++;
                                ncount[FLOW_C][c]++; ncount[FLOW_A][d]++;
                                laplacians.addCount(FLOW_B+1,a,{b,c,d});
                                laplacians.addCount(FLOW_B+1,b,{a,c,d});
                                laplacians.addCount(FLOW_C+1,c,{a,b,d});
                                laplacians.addCount(FLOW_A+1,d,{a,b,c});
                            }
                        }
                        else
                        {
                            gcount[4]++; /* C4 */
                            ncount[C4_A][a]++; ncount[C4_A][b]++; ncount[C4_A][c]++;
                            ncount[C4_A][d]++;
                            laplacians.addCount(C4_A+1,a,{b,c,d});
                            laplacians.addCount(C4_A+1,b,{a,c,d});
                            laplacians.addCount(C4_A+1,c,{a,b,d});
                            laplacians.addCount(C4_A+1,d,{a,b,c});
                        }
                    }

                    /* classify most 5-node graphlets */

                    if (five_nodes) {
                        std::vector<int> neighbours_d = g.get_neighbours(d);
                        for(pe = neighbours_d.begin(); pe != neighbours_d.end(); ++pe)
                        {
                            e = *pe;
                            if (e == a || e == b || e == c || e == d) continue;

                            int deg5_a = deg4_a, deg5_b = deg4_b, deg5_c = deg4_c,
                                    deg5_d = deg4_d, deg5_e = 0;

                            x = !!g.connected(e, a);
                            deg5_e += x;
                            deg5_a += x;
                            x = !!g.connected(e, b);
                            deg5_e += x;
                            deg5_b += x;
                            x = !!g.connected(e, c);
                            deg5_e += x;
                            deg5_c += x;
                            x = !!g.connected(e, d);
                            deg5_e += x;
                            deg5_d += x;

                            /* add degrees of node and neighbors to find each ndeg */

                            int ndeg_a = deg5_a, ndeg_b = deg5_b, ndeg_c = deg5_c,
                                    ndeg_d = deg5_d, ndeg_e = deg5_e;
                            if (g.connected(a, b)) {
                                ndeg_a += deg5_b;
                                ndeg_b += deg5_a;
                            }
                            if (g.connected(a, c)) {
                                ndeg_a += deg5_c;
                                ndeg_c += deg5_a;
                            }
                            if (g.connected(a, d)) {
                                ndeg_a += deg5_d;
                                ndeg_d += deg5_a;
                            }
                            if (g.connected(a, e)) {
                                ndeg_a += deg5_e;
                                ndeg_e += deg5_a;
                            }
                            if (g.connected(b, c)) {
                                ndeg_b += deg5_c;
                                ndeg_c += deg5_b;
                            }
                            if (g.connected(b, d)) {
                                ndeg_b += deg5_d;
                                ndeg_d += deg5_b;
                            }
                            if (g.connected(b, e)) {
                                ndeg_b += deg5_e;
                                ndeg_e += deg5_b;
                            }
                            if (g.connected(c, d)) {
                                ndeg_c += deg5_d;
                                ndeg_d += deg5_c;
                            }
                            if (g.connected(c, e)) {
                                ndeg_c += deg5_e;
                                ndeg_e += deg5_c;
                            }
                            if (g.connected(d, e)) {
                                ndeg_d += deg5_e;
                                ndeg_e += deg5_d;
                            }

                            // note that (x%4 + y%4) is not the same as (x+y)%4
                            int hash = (ndeg_a % 4 + ndeg_b % 4 + ndeg_c % 4 + ndeg_d % 4
                                        + ndeg_e % 4);
                            int deg_total = deg5_a + deg5_b + deg5_c + deg5_d + deg5_e;
                            int gtype = gtable[deg_total / 2 - 4][hash / 2];


                            /* not caught by table */


                            if (deg_total == 14 && hash == 6)
                                gtype = (ndeg_a > 12 || ndeg_a == 5) ? 22 : 24;

                            assert(gtype > 7 && gtype < 29);

                            gcount[gtype]++;

                            ncount[(int) ntable[gtype][ndeg_a]][a]++;
                            laplacians.addCount((int) ntable[gtype][ndeg_a] + 1, a, {b, c, d, e});
                            ncount[(int) ntable[gtype][ndeg_b]][b]++;
                            laplacians.addCount((int) ntable[gtype][ndeg_b] + 1, b, {a, c, d, e});
                            ncount[(int) ntable[gtype][ndeg_c]][c]++;
                            laplacians.addCount((int) ntable[gtype][ndeg_c] + 1, c, {a, b, d, e});
                            ncount[(int) ntable[gtype][ndeg_d]][d]++;
                            laplacians.addCount((int) ntable[gtype][ndeg_d] + 1, d, {a, b, c, e});
                            ncount[(int) ntable[gtype][ndeg_e]][e]++;
                            laplacians.addCount((int) ntable[gtype][ndeg_e] + 1, e, {a, b, c, d});
                        }
                    }
                }
            }
        }
    }

#if PROGRESS_INFO
    fprintf(stderr, "\nCounting complete.\n");
#endif

    /* output */
    /*char temp[PATH_MAX];
    FILE *gr_out = NULL, *ndump = NULL;

    int errors = 0;

    if(out != stdout)
    {
        sprintf(temp, "%s.gr_freq", outname);
        gr_out = fopen(temp, "w");
        sprintf(temp, "%s.ndump2", outname);
        ndump = fopen(temp, "w");
    }*/

    /* print graphlet counts */
    /*for(int i = 0; i < 29; i++)
    {
	assert(gcount[i] % overcount[i] == 0);https://networkx.github.io/documentation/networkx-1.10/test.html
        fprintf(out, "%d\t%lld\n", i+1, gcount[i]/overcount[i]);
        if(gr_out)
            fprintf(gr_out, "%d\t%lld\n", i+1, gcount[i]/overcount[i]);
    }*/

    /* print node class counts */
//    for(i = 0; i < 72; i++)
//    {
//        FILE *n_out;
//        if(out == stdout) n_out = stdout;
//        else
//        {
//            sprintf(temp, "%s.cl_%02d_freq", outname, i+1);
//            n_out = fopen(temp, "w");
//            if(!n_out) { perror(temp); exit(1); }
//        }
//
//        std::map<const int64, int64> ndist;
//
//        int overc, gtype;
//        int64 ndeg;
//
//        gtype = ntype2gtype[i];
//        overc = overcount[gtype];
//        for(j = 0; j < V; j++)
//        {
//            ndeg = ncount[i][j];
//            if(ndeg > 0)
//	    {
//		assert(ndeg % overc == 0);
//                ndist[ndeg / overc]++;
//	    }
//        }
//
//        int64 total = 0;
//
//        /* fprintf(n_out, "# Class %s\n", cnames[i]); */
//        std::map<const int64, int64>::iterator iter; //Oleksii
//        for(iter = ndist.begin(); iter != ndist.end(); ++iter)
//        {
//            fprintf(n_out, "%lld\t%lld\n", iter->first, iter->second);
//            total += iter->first * iter->second;
//        }
//
//        if(ndist.size() == 0)
//            fprintf(n_out, "0\t0\n");
//
//        /* make sure there aren't fewer or more nodes per graphlet */
//        int64 check_count = gcount[gtype]/overc * klaplacians[i];
//        if(check_count != total)
//        {
//            fprintf(stderr,"Sanity failure at %d (%s):"
//                           " %lld expected, found %lld\n",
//                    i+1, cnames[i], check_count, total);
//            errors++;
//        }
//
//        if(n_out != stdout) fclose(n_out);
//    }

    /* dump degree distribution to cl_00_freq */
    std::map<const int, int> ddist;

//    FILE *n_out;
//    if(out == stdout) n_out = stdout;
//    else
//    {
//        sprintf(temp, "%s.cl_00_freq", outname);
//        n_out = fopen(temp, "w");
//        if(!n_out) { perror(temp); exit(1); }
//    }
//
//    for(i = 0; i < V; i++)
//        ddist[ DEGREE(i) ]++;
//
//    std::map<const int, int>::iterator iter;//Oleksii
//    for(iter = ddist.begin(); iter != ddist.end(); ++iter)
//        fprintf(n_out, "%d\t%d\n", iter->first, iter->second);
//    if(n_out != stdout) fclose(n_out);


    /* RedundancyChecker checker; */
//    if(ndump)
//    {
//        for(int j = 0; j < V; j++)
//        {
//            fprintf(ndump, "%s %d", node_names[j], DEGREE(j));
//            //std::cout<<j<<' ';
//
//            std::cout<<DEGREE(j)<< ' ';
//            for(int i = 0; i < 72; i++)
//            {
//                    int64 a= ncount[i][j];
//                    assert(ncount[i][j]%overcount[ntype2gtype[i]] == 0);
//                    fprintf(ndump, " %lld", ncount[i][j]/overcount[ntype2gtype[i]]);
//                    std::cout<<  ncount[i][j]/overcount[ntype2gtype[i]]<< ' ';
//
//            }
//            std::cout<<std::endl;
//
//            int64 gdv[73]={0};
//            gdv[0]= DEGREE(j);
//
//            std::cout<< gdv[0]<< ' ';
//            for(int k = 0; k < 72; k++) {
//                gdv[k+1]=ncount[k][j]/overcount[ntype2gtype[k]];
//                std::cout<< gdv[k+1]<< ' ';
//            }
//            std::cout<<std::endl;
//
//            checker.checkRedundancyConstraints4Nodes(gdv);
//            //checker.checkRedundancyConstraints5Nodes(gdv);
//
//            fprintf(ndump, "\n");
//        }
//    }

    //if(errors) exit(1);
    RedundancyChecker checker  = RedundancyChecker();
    checker.sanityCheckSumOfRows(laplacians);
    //checker.checkRedundanciesLcount(laplacians);
    //checker.checkRedundanciesNcount(ncount,V,edges_for);
    //checker.debugRedundancieslaplacians(laplacians,ncount,edges_for);
    /* checker.sanityCheckSumOfRows(laplacians); */

    return laplacians;
}




