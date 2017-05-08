from mygraph import MyGraph
from path import bidirectional_dijkstra
from util import density
import random
import math
from util import asp_and_lsp_path
import time
from copy import deepcopy

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
@timing
def weiner_new(G,trials=1,needratio=False):
        log = int(math.log1p(len(G))) #
        nodes_len = len(G)
        if trials == 1:
            lenght = len(G)
            trials = lenght*int(math.log1p(lenght))
        n = len(G)
        skipped = 0
        path_number = 0
        for q in range(0,log):
            first_node = int(n*random.random())
            for second_node in range(0,nodes_len):
                if (first_node==second_node):
                    skipped+=1
                    continue
                else:
                    try:
                        node=G[first_node]
                        node2=G[second_node]
                        path = bidirectional_dijkstra(G,first_node,second_node,False)
                        path_number += path
                    except KeyError:
                        continue
        ratioo = n*n/(float(trials)-skipped)
        expected_path = ratioo*float(path_number)
        return expected_path
@timing
def weiner_random_trial(G,trials=1,needratio=False):
    if trials == 1:
        lenght = len(G)
        trials = lenght*int(math.log1p(lenght))
    n = len(G)
    path_number = 0
    for r in range(0,trials):
        first_node = int(n*random.random())
        second_node = int(n*random.random())
        if (first_node==second_node):
            continue
        else:
            try:
                node=G[first_node]
                node2=G[second_node]
                path = bidirectional_dijkstra(G,first_node,second_node,False)
                path_number += path
            except KeyError:
                continue
    ratioo = n*n/float(trials)
    expected_path = ratioo*float(path_number)
    return expected_path
@timing
def weiner_path_number(G,needratio = False):
    path_number = 0.0
    node_len = len(G)
    for x in range(0,node_len):
        # print '{0}\r'.format(x)
        for y in range(x, node_len):
            if (x==y):
                continue
            else:
                try:
                    node=G[x]
                    node2=G[y]
                    path = bidirectional_dijkstra(G,x,y,False)
                    path_number += path
                except KeyError:
                    continue
    if needratio:
        ratio = node_len/path_number
        return path_number,ratio
    else:
        return path_number*2
def vitality_distr(G):
    node_len = len(G)
    vitality_dis = [0]*node_len
    weiner_full = weiner_path_number(G)
    for x in range(0,node_len):
        a = deepcopy(G)
        a.delete_node(x)
        weiner_single = weiner_path_number(a)
        vit = weiner_full-weiner_single
        if vit<-100:
            vit = None
        vitality_dis[x] = (vit),x
        print x
    sorted_vitality = sorted(vitality_dis, key=lambda tup: tup[0])
    return sorted_vitality

def betweenness_centrality(G,trials = 100):
    node_len = len(G)
    betweenness_centrality_distr = [0]*node_len
    avarage_shortest_path, longest_shortest_path_lenght, longest_shortest_path = asp_and_lsp_path(G)
    diameter = longest_shortest_path_lenght
    if (trials == 100):
        trials = math.log1p(node_len)*math.log1p(node_len)
    for node in range(0,node_len):
        for justdoit in range(0,trials):
            first_node = int(node_len*random.random())
            second_node = int(node_len*random.random())
            node_to_delete = node
            if (first_node==second_node) or (second_node==node_to_delete) or (node_to_delete==first_node):
                continue
            else:
                a = deepcopy(G)
                a.delete_node(node_to_delete)
                try:
                    pathdel = bidirectional_dijkstra(a,first_node,second_node,False)
                    if (pathdel==100000):
                        pathdel = diameter
                except KeyError:
                    pathdel = diameter
                path = bidirectional_dijkstra(G,first_node,second_node,False)
                difference = pathdel-path
                betweenness_centrality_distr[node] += difference
        betweenness_centrality_distr[node] = betweenness_centrality_distr[node],node
        # print betweenness_centrality_distr[node]
    sorted_bcd = sorted(betweenness_centrality_distr, key=lambda tup: tup[0])
    return sorted_bcd
@timing
def closeness_centr(G):
    node_len = len(G)
    closeness_centrality_distr = [0]*node_len
    avarage_shortest_path, longest_shortest_path_lenght, longest_shortest_path = asp_and_lsp_path(G)
    diameter = longest_shortest_path_lenght
    for node in range(0,node_len):
        for second_node in range(0,node_len):
            if (node==second_node):
                continue
            else:
                try:
                    path = bidirectional_dijkstra(G,node,second_node,False)
                    if (path==100000):
                        path = diameter
                except KeyError:
                    path = diameter
                closeness_centrality_distr[node] += path
        closeness_centrality_distr[node] = (1/float(closeness_centrality_distr[node])),node
        # print betweenness_centrality_distr[node]
    sorted_bcd = sorted(closeness_centrality_distr, key=lambda tup: tup[0])
    return sorted_bcd
@timing
def degree_centr(G):
    node_len = len(G)
    degree_centr = [0]*node_len
    for node in range(0,node_len):
        nbrs = list(G[node])
        degree = len(nbrs)
        degree_centr[node] = degree
        degree_centr[node] = (degree_centr[node],node)
        # print betweenness_centrality_distr[node]
    sorted_return = sorted(degree_centr, key=lambda tup: tup[0])
    return sorted_return
