from mygraph import MyGraph
from path import bidirectional_dijkstra
import random
import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
@timing
def clustering_possility(G,trials=1000):
    n = len(G)
    triangles = 0
    closed_triangles = 0
    for repeat in range(0, trials):
        random_node = G[int(n*random.random())]
        nbrs_of_node = list(random_node)
        if len(nbrs_of_node)<2:
            continue
        else:
            found = False
            while not found:
                first_nbr = nbrs_of_node[int(len(nbrs_of_node)*random.random())]
                second_nbr = nbrs_of_node[int(len(nbrs_of_node)*random.random())]
                if (first_nbr!=second_nbr):
                    found = True
                    triangles += 1
                    first_node = G[first_nbr]
                    second_node = G[second_nbr]
                    first_node_nbrs = list(first_node)
                    if second_nbr in first_node_nbrs:
                        closed_triangles += 1
    ratio = (closed_triangles/float(triangles))
    return ratio
@timing
def clustering_coof_full(G):
    nodes_num = len(G)
    triangles = 0
    closed_triangles = 0
    for node_n in range(0,nodes_num):
        node = G[node_n]
        nbrs_of_node = list(node)
        nbrs_count = len(nbrs_of_node)
        opa = 0.0
        if len(nbrs_of_node)<0:
            continue
        else:
            # maxnum = nodes_num*(nodes_num-1)
            # opa += nbrs_count/float(maxnum)
            # print nbrs_of_node
            for x in range(0,nbrs_count):
                for y in range(x,nbrs_count):
                    if (x==y):
                        continue
                    else:
                        triangles += 1
                        first_node = nbrs_of_node[x]
                        second_node = nbrs_of_node[y]
                        first_node_nbrs = list(G[first_node])
                        if second_node in first_node_nbrs:
                            closed_triangles += 1
    # ratio = opa/float(nodes_num)
    ratio = (closed_triangles/float(triangles))
    return ratio


    return
@timing
def asp_and_lsp_path(G):
    nodecount = len(G.nodes)
    avarage_lenght = []
    longest_len = 0
    record_path = []
    iterations = 0
    for source in range(0, nodecount):
        for target in range(source, nodecount): #change 0 changed to source more efficency
            if target == source:
                continue
            else:
                iterations += 1
                length, path = bidirectional_dijkstra(G, source, target, True)
                avarage_lenght.append(length)
                if length>=longest_len:
                    longest_len = length
                    record_path.append(path)
    for p in record_path:
        if len(p)!=longest_len:
            record_path.remove(p)
    asp = (sum(avarage_lenght)/float(len(avarage_lenght)))
    print("iterations made",iterations)
    return (asp, longest_len, record_path)
@timing
def degree_avarage(G):
    # input : MyGraph
    # output avarage degree and degree degree_distribution array
    nodecount = len(G.nodes)
    avrg_degree = 0
    degree_distribution = [0]*nodecount
    for node in range(1,nodecount):
        nbrs_node = list(G[node])
        degree = len(nbrs_node)
        avrg_degree += degree
        degree_distribution[degree] += 1
    avrg_degree = avrg_degree/float(nodecount)
    maxval = 0
    for d in range(1,len(degree_distribution)):
        if (degree_distribution[d]>0):
            maxval = d
    return avrg_degree, degree_distribution[:maxval+1]
@timing
def density(G, returnedges=False):
    # input MyGraph
    # output how many edged there are compare to how many edges there could potentially be
    nodecount = len(G.nodes)
    edges = 0
    maxedges = nodecount*(nodecount-1)
    for node in range(0,nodecount):
        nbrs = list(G[node])
        nbrs_count = len(nbrs)
        edges += nbrs_count
    edges = edges/2
    ratio = edges/float(maxedges)
    if returnedges:
        return ratio*2, edges
    else:
        return ratio*2
