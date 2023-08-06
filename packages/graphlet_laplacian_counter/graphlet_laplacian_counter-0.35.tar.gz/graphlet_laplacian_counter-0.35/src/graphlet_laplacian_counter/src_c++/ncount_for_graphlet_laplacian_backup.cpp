#include "Counter.h"
#include "RedundancyChecker.h"

#include <memory>
#include <iostream>
#include <string>
#include <cstdio>






template<typename ... Args>
std::string string_format( const std::string& format, Args ... args )
{
    size_t size = snprintf( nullptr, 0, format.c_str(), args ... ) + 1; // Extra space for '\0'
    std::unique_ptr<char[]> buf( new char[ size ] );
    snprintf( buf.get(), size, format.c_str(), args ... );
    return std::string( buf.get(), buf.get() + size - 1 ); // We don't want the '\0' inside
}


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


void die(char *msg) {
    fprintf(stderr, "ERROR: %s\n", msg);
    exit(1);
}

void count(FILE *f, FILE *out, char const *outname, std::string outputPrefix, bool fiveNodes)
{


    int V, E, E_undir, i, j;
    time_t start_time = time(0);

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
    E = E_undir * 2;

    assert(E_undir >= 0);

    struct temp_data **heads = new temp_data*[V]; //Oleksii
    struct temp_data *links = new temp_data[E]; //Oleksii
    for(i = 0; i < V; i++)
        heads[i] = NULL;

    struct temp_data *link;

#if HUGE_GRAPHS
    /* Use a map (sparse associated array) for the adjacency matrix */
    /* Use int64 as the index, with high 32 bits encoding row, low 32 bits encoding column */
    #define Connect(i,j) (adjmat[((int64)(i))<<32 | j] = 1)
    #define Connected(i,j) (adjmat[((int64)(i))<<32 | j])
    std::map<const int64, char> adjmat;
    for(i = 0; i < V; i++)
        Connect(i,i); /* optimization hack */
#else
    /* allocate some space for the adjacency matrix */
    char **adjmat = new char*[V]; //Oleksii
    /* Use a bit vector to store each row of the adjancency matrix, so
     * that each edge takes up only one bit.
     */
    #define Connect(i,j) (adjmat[i][(j)/8] |= 1<<((j)%8))
    #define Connected(i,j) (adjmat[i][(j)/8] & (1<<((j)%8)))
    for(i = 0; i < V; i++)
    {
        /* calloc zeroes the memory for us */
        adjmat[i] = (char *) calloc(V/8+1, sizeof(char));
        if(!adjmat[i]) { perror("calloc"); exit(1); }

        Connect(i,i); /* optimization hack */
    }
#endif
    /* First stores edges in linked lists by node (vertex) so we know how many
     * edges there are for each node, then copy to an array for efficiency.
     */

    /* add data to linked list for intermediate storage */
    for(i = 0; i < E_undir; i++)
    {
        int src = -1, dst = -1;
        fscanf(f, "%d %d %*d %*s", &src, &dst);
        src -= 1; /* LEDA graph files are 1-indexed */
        dst -= 1;

        if(src < 0 || dst < 0)
        {
            fprintf(stderr,"Error: node numbers must be greater than zero.\n");
            exit(1);
        }

        if(src == dst) continue; /* ignore self-loops */

        /* See if edge is already in list */
        int bad = 0;
        for(link = heads[src]; link; link = link->next)
        {
            if(link->dst == dst)
            {
                bad = 1; /* don't allow parallel edges */
                break;
            }
        }
        if(bad) continue;

        struct temp_data *ntemp1 = &links[i*2];
        struct temp_data *ntemp2 = &links[i*2+1];

        /* Add to front of node's linked list */
        ntemp1->next = heads[src]; ntemp1->dst = dst;
        ntemp2->next = heads[dst]; ntemp2->dst = src;
        heads[src] = ntemp1;
        heads[dst] = ntemp2;

        //add undirected edges
        Connect(src, dst);
        Connect(dst, src);
    }

    /* The edges[] array stores edges by node sequentially, so the last edge
       of node n is followed by the first edge of n+1. edges_for[] stores 
       a pointer to the first edge of a node. */

    int **edges_for = new int*[V+1]; //Oleksii
    int *edges = new int[E*2+1]; //Oleksii

    int *edge_last = &edges[0];

    for(i = 0; i < V; i++)
    {
        edges_for[i] = edge_last;
        for(link = heads[i]; link; link = link->next)
        {
            *edge_last = link->dst;
            edge_last++;
        }
    }
    edges_for[i] = edge_last;

    int64 gcount[29] = {};
    int64 *ncount[72];

    /* allocate space for node type counts */
    for(i = 0; i < 72; i++)
    {
        ncount[i] = (int64 *) calloc(V, sizeof(int64));
        if(!ncount[i]) { perror("calloc"); exit(1); }
    }


    //allocate space for graphlet laplacian
    int nrOfOrbits = 15;
    if (fiveNodes){
        nrOfOrbits=73;
    }
    //Lcount3DArray lcount3DArray =Lcount3DArray (nrOfOrbits,V);
    //Lcount3D &lcount = lcount3DArray;

    Lcount3DVector lcount3DVector= Lcount3DVector(nrOfOrbits,V);
    Lcount3D &lcount = lcount3DVector;

    //Lcount3DSparse lcount3DSparse = Lcount3DSparse(nrOfOrbits,V);
    //Lcount3D &lcount = lcount3DSparse;


    /* start counting */

    int *pb, *pc, *pd, *pe;
    int a, b, c, d, e, x;

    for(a = 0; a < V; a++)
    {
        if (a%100==0.0)
            std::cout<<"node: "<<a+1<<'/'<<V<< std::endl;
#if PROGRESS_INFO
      fprintf(stderr, "\rnode # %5d (%.1f%%) [%d min elapsed]", a, 
              100.0 * (float) a / V, (time(0) - start_time) / 60);
#endif

      foreach_adj(pb, a)// loop over all neighbours of a
      {
        b = *pb;
//          if (a==22){
//              std::cout<<b<<std::endl;
//          }
        if(b == a) continue;

        lcount.addCount(0,a,b);
        foreach_adj(pc, b) // loop over all neighbours of b
        {
          c = *pc;
          if(c == a || c == b) continue;

          /* count adjacent edges */
          int deg3_a = 0, deg3_b = 0, deg3_c = 0;

	  // The "!!" is a double negation, which maps any non-zero integer to 1
          x = !!Connected(a,b); deg3_a += x; deg3_b += x;
          x = !!Connected(a,c); deg3_a += x; deg3_c += x;
          x = !!Connected(b,c); deg3_b += x; deg3_c += x;


          if(deg3_a == 1)
          {
            gcount[0]++; /* path */
            ncount[P3_A][a]++; ncount[P3_B][b]++; ncount[P3_A][c]++;
              lcount.addCount(P3_A+1, a,{ b,c} );

              lcount.addCount(P3_B+1, b,{ a,c} );

              lcount.addCount(P3_A+1, c,{ a,b} );


            // look for claws
            if(DEGREE(b) > 2)
            foreach_adj(pd, b)
            {
                d = *pd;
                if(Connected(a,d) + Connected(c,d) == 0)
                {
                    // look for X11
                    if(DEGREE(b) > 3 and fiveNodes)
                    foreach_adj(pe, b)
                    {
                        e = *pe;
                        if(Connected(a,e) + Connected(c,e) + Connected(d,e) == 0)
                        {
                            gcount[10]++; /* X11 */
                            ncount[X11_A][a]++; ncount[X11_B][b]++;
                            ncount[X11_A][c]++; ncount[X11_A][d]++;
                            ncount[X11_A][e]++;
                        }
                    }

                    gcount[3]++; /* Claw! */
                    ncount[CLAW_A][a]++; ncount[CLAW_B][b]++;
                    ncount[CLAW_A][c]++; ncount[CLAW_A][d]++;


                    lcount.addCount(CLAW_A+1, a,{ b,c,d} );
                    lcount.addCount(CLAW_B+1, b,{ a,c,d} );
                    lcount.addCount(CLAW_A+1,c,{a,b,d});
                    lcount.addCount(CLAW_A+1,d,{a,b,c});
                }
            }
          }
          else
          {
            gcount[1]++; /* triangle */
            ncount[C3_A][a]++; ncount[C3_A][b]++; ncount[C3_A][c]++;
            lcount.addCount(C3_A+1,a,{b,c});
            lcount.addCount(C3_A+1,b,{a,c});
            lcount.addCount(C3_A+1,c,{a,b});

          }

          foreach_adj(pd, c)
          {
            d = *pd;
            if(d == a || d == b || d == c) continue;

            /* classify most 4-node graphlets (excluding some claws) */

            int deg4_a = deg3_a, deg4_b = deg3_b, deg4_c = deg3_c, deg4_d = 0;

            x = !!Connected(a,d); deg4_d += x; deg4_a += x;
            x = !!Connected(b,d); deg4_d += x; deg4_b += x;
            x = !!Connected(c,d); deg4_d += x; deg4_c += x;

            int num_edges = deg4_a + deg4_b + deg4_c + deg4_d;

            if(num_edges == 6)
            {
                gcount[2]++; /* P4 */
              ncount[P4_A][a]++; ncount[P4_B][b]++; ncount[P4_B][c]++;
              ncount[P4_A][d]++;


                lcount.addCount(P4_A+1,a,{b,c,d});;
                lcount.addCount(P4_B+1,b,{a,c,d});
                lcount.addCount(P4_B+1,c,{a,b,d});
                lcount.addCount(P4_A+1,d,{a,b,c});
                if (fiveNodes) {
                    foreach_adj(pe, b) /* look for X10 */
                    {
                        e = *pe;
                        if (Connected(a, e) + Connected(c, e) + Connected(d, e) == 0) {
                            gcount[9]++; /* X10 */
                            ncount[X10_B][a]++;
                            ncount[X10_D][b]++;
                            ncount[X10_C][c]++;
                            ncount[X10_A][d]++;
                            ncount[X10_B][e]++;

                            lcount.addCount(X10_B + 1, a, {b, d, d, e});
                            lcount.addCount(X10_D + 1, b, {a, c, d, e});
                            lcount.addCount(X10_C + 1, c, {a, b, d, e});
                            lcount.addCount(X10_A + 1, d, {a, b, c, e});
                            lcount.addCount(X10_B + 1, e, {a, b, c, d});
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

                lcount.addCount(deg4_a == 3 ? DIAM_B+1 : DIAM_A+1,a,{b,c,d});
                lcount.addCount(deg4_b == 3 ? DIAM_B+1 : DIAM_A+1,b,{a,c,d});
                lcount.addCount(deg4_c == 3 ? DIAM_B+1 : DIAM_A+1,c,{a,b,d});
                lcount.addCount(deg4_d == 3 ? DIAM_B+1 : DIAM_A+1,d,{a,b,c});
            }
            else if(num_edges == 12)
            {
              gcount[7]++; /* K4 */
              ncount[K4_A][a]++; ncount[K4_A][b]++; ncount[K4_A][c]++;
              ncount[K4_A][d]++;

                lcount.addCount(K4_A+1,a,{b,c,d});
                lcount.addCount(K4_A+1,b,{a,c,d});
                lcount.addCount(K4_A+1,c,{a,b,d});
                lcount.addCount(K4_A+1,d,{a,b,c});

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

                    lcount.addCount(FLOW_A+1,a,{b,c,d});
                    lcount.addCount(FLOW_C+1,b,{a,c,d});
                    lcount.addCount(FLOW_B+1,c,{a,b,d});
                    lcount.addCount(FLOW_B+1,d,{a,b,c});
                    // only do this for half the cases, to reduce overcount

                    if (fiveNodes) {
                        foreach_adj(pe, b) {
                            e = *pe;
                            if (Connected(a, e) + Connected(c, e) + Connected(d, e) == 0) {
                                gcount[13]++; /* X14 */
                                ncount[X14_A][a]++;
                                ncount[X14_C][b]++;
                                ncount[X14_B][c]++;
                                ncount[X14_B][d]++;
                                ncount[X14_A][e]++;
                                lcount.addCount(X14_A+1,a,{b,c,d,e});
                                lcount.addCount(X14_C+1,b,{a,c,d,e});
                                lcount.addCount(X14_B+1,c,{a,b,d,e});
                                lcount.addCount(X14_B+1,d,{a,b,c,e});
                                lcount.addCount(X14_A+1,e,{a,b,c,d});
                            }
                        }
                    }
                }
                else
                {
                    ncount[FLOW_B][a]++; ncount[FLOW_B][b]++;
                    ncount[FLOW_C][c]++; ncount[FLOW_A][d]++;
                    lcount.addCount(FLOW_B+1,a,{b,c,d});
                    lcount.addCount(FLOW_B+1,b,{a,c,d});
                    lcount.addCount(FLOW_C+1,c,{a,b,d});
                    lcount.addCount(FLOW_A+1,d,{a,b,c});
                }
              }
              else
              {
                gcount[4]++; /* C4 */
                ncount[C4_A][a]++; ncount[C4_A][b]++; ncount[C4_A][c]++;
                ncount[C4_A][d]++;
                  lcount.addCount(C4_A+1,a,{b,c,d});
                  lcount.addCount(C4_A+1,b,{a,c,d});
                  lcount.addCount(C4_A+1,c,{a,b,d});
                  lcount.addCount(C4_A+1,d,{a,b,c});
              }
            }

            /* classify most 5-node graphlets */

              if (fiveNodes) {
                  foreach_adj(pe, d) {
                      e = *pe;
                      if (e == a || e == b || e == c || e == d) continue;

                      int deg5_a = deg4_a, deg5_b = deg4_b, deg5_c = deg4_c,
                              deg5_d = deg4_d, deg5_e = 0;

                      x = !!Connected(e, a);
                      deg5_e += x;
                      deg5_a += x;
                      x = !!Connected(e, b);
                      deg5_e += x;
                      deg5_b += x;
                      x = !!Connected(e, c);
                      deg5_e += x;
                      deg5_c += x;
                      x = !!Connected(e, d);
                      deg5_e += x;
                      deg5_d += x;

                      /* add degrees of node and neighbors to find each ndeg */

                      int ndeg_a = deg5_a, ndeg_b = deg5_b, ndeg_c = deg5_c,
                              ndeg_d = deg5_d, ndeg_e = deg5_e;
                      if (Connected(a, b)) {
                          ndeg_a += deg5_b;
                          ndeg_b += deg5_a;
                      }
                      if (Connected(a, c)) {
                          ndeg_a += deg5_c;
                          ndeg_c += deg5_a;
                      }
                      if (Connected(a, d)) {
                          ndeg_a += deg5_d;
                          ndeg_d += deg5_a;
                      }
                      if (Connected(a, e)) {
                          ndeg_a += deg5_e;
                          ndeg_e += deg5_a;
                      }
                      if (Connected(b, c)) {
                          ndeg_b += deg5_c;
                          ndeg_c += deg5_b;
                      }
                      if (Connected(b, d)) {
                          ndeg_b += deg5_d;
                          ndeg_d += deg5_b;
                      }
                      if (Connected(b, e)) {
                          ndeg_b += deg5_e;
                          ndeg_e += deg5_b;
                      }
                      if (Connected(c, d)) {
                          ndeg_c += deg5_d;
                          ndeg_d += deg5_c;
                      }
                      if (Connected(c, e)) {
                          ndeg_c += deg5_e;
                          ndeg_e += deg5_c;
                      }
                      if (Connected(d, e)) {
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
                      lcount.addCount((int) ntable[gtype][ndeg_a] + 1, a, {b, c, d, e});
                      ncount[(int) ntable[gtype][ndeg_b]][b]++;
                      lcount.addCount((int) ntable[gtype][ndeg_b] + 1, b, {a, c, d, e});
                      ncount[(int) ntable[gtype][ndeg_c]][c]++;
                      lcount.addCount((int) ntable[gtype][ndeg_c] + 1, c, {a, b, d, e});
                      ncount[(int) ntable[gtype][ndeg_d]][d]++;
                      lcount.addCount((int) ntable[gtype][ndeg_d] + 1, d, {a, b, c, e});
                      ncount[(int) ntable[gtype][ndeg_e]][e]++;
                      lcount.addCount((int) ntable[gtype][ndeg_e] + 1, e, {a, b, c, d});
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
    char temp[PATH_MAX];
    FILE *gr_out = NULL, *ndump = NULL;

    int errors = 0;

    if(out != stdout)
    {
        sprintf(temp, "%s.gr_freq", outname);
        gr_out = fopen(temp, "w");
        sprintf(temp, "%s.ndump2", outname);
        ndump = fopen(temp, "w");
    }

    /* print graphlet counts */
    for(i = 0; i < 29; i++)
    {
	assert(gcount[i] % overcount[i] == 0);https://networkx.github.io/documentation/networkx-1.10/test.html
        fprintf(out, "%d\t%lld\n", i+1, gcount[i]/overcount[i]);
        if(gr_out)
            fprintf(gr_out, "%d\t%lld\n", i+1, gcount[i]/overcount[i]);
    }

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
//        int64 check_count = gcount[gtype]/overc * klcount[i];
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

    if(errors) exit(1);
   // Writer writer = Writer();
 //writer.writeGraphletLaplacian(lcount,outputPrefix);
    /* checker.checkRedundanciesLcount(lcount); */
    //checker.checkRedundanciesNcount(ncount,V,edges_for);
    //checker.debugRedundanciesLcount(lcount,ncount,edges_for);
    /* checker.sanityCheckSumOfRows(lcount); */
}


