# -*- coding: utf-8 -*-
from igraph import Graph
from mygraph import MyGraph
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
@timing
def save_gephi(G,name='23.GML',vk=False):
    nodes = len(G)
    output = 'graph\n[\n '
    for node in range(0,nodes):
        output+='node\n[\n '
        output+='id %d\n' % node
        if (node == 0):
            f_name = G.nodes.get(node).get('info')[0].get('first_name')
            s_name = G.nodes.get(node).get('info')[0].get('last_name')
            fullname = f_name+' '+s_name
        else:
            f_name = G.nodes.get(node).get('info').get('first_name')
            s_name = G.nodes.get(node).get('info').get('last_name')
            fullname = f_name+' '+s_name
        output+='label "%s"\n' % fullname
        output+=']\n'
    for x in range(0,nodes):
        for y in range(x,nodes):
            if (x==y):
                continue
            else:
                if G.edge_exists(x,y):
                    output+='edge\n'
                    output+='[\n'
                    output+='source %d\n' % x
                    output+='target %d\n' % y
                    output+='label "weight 1"'
                    output+=']\n'
    output+=']'
    file = open(name,'w')
    file.write(output)
    file.close()
@timing
def load():
    GRAPH_COUNT = 8
    graphs = []
    for graph_num in range(5,6):
            print 'loaded %d' % graph_num
            graphs.append(Graph.Read_GraphML('graph%d.graphml' % graph_num))
    graphs_return = []
    # CHANGE HERE FOR ALL GRAPHS
    # graph = graphs[2]
    for graph in graphs:
        mygraph = MyGraph()
        count = 0
        for vertex in graph.vs:
            mygraph.add_single_node(count, graphmlid = vertex["id"])
            edges = graph.es.select(_source=count)
            for edge in edges:
                source, target = edge.tuple
                mygraph.add_single_edge(source,target, weight = 1)
            count += 1
        graphs_return.append(mygraph)
    print graphs_return
    return graphs_return
