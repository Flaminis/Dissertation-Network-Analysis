from reader import load,save_gephi
from mygraph import MyGraph
from memory_profiler import memory_usage
from path import bidirectional_dijkstra
from util import asp_and_lsp_path, clustering_possility, clustering_coof_full, degree_avarage,density
from vitality import weiner_path_number,weiner_random_trial,vitality_distr,weiner_new,betweenness_centrality,closeness_centr,degree_centr
import math
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotit import barplot,distplot,barplotduo
from copy import deepcopy
from vkimporter import vk_graph

def difference_percentage(first, second):
    return (abs(first - second))/second*100.0
graphs = load()
# print graphs
# g = graphs[0]
for g in graphs:
# g = vk_graph()


    g.description()
# save_gephi(g)
    # avarage_shortest_path, longest_shortest_path_lenght, longest_shortest_path = asp_and_lsp_path(g)
    # print 'average shortest path is %f%%' % avarage_shortest_path
    # print 'diameter of the network is %d' % longest_shortest_path_lenght

    # clustering_coof = clustering_possility(g,1000)
    # print 'clustering cooficent is equal to %f' % clustering_coof
    # clustering_coof_fully = clustering_coof_full(g)
    # print clustering_coof_fully
    # print 'difference between absolute and predicted clustering is %f%%' % difference_percentage(clustering_coof_fully,clustering_coof)
    #
    # betweenness_centrality_ok = betweenness_centrality(g,100)
    # print 'betweenness_centrality is calculated for each node and most imporant nodes are highlighted at the end of the list'
    # print betweenness_centrality_ok

    # closeness_centrality = closeness_centr(g)
    # print 'closeness_centrality is calculated for each node and most imporant nodes are highlighted at the end of the list'
    # print closeness_centrality
    # degree_centrality = degree_centr(g)
    # barplotduo(closeness_centrality,name='closeness_centrality')
    # barplotduo(betweenness_centrality_ok,name='betweenness_centrality')
    # barplotduo(degree_centrality,name='degree_centrality')

    avrg_degree, degree_distribution = degree_avarage(g)
    # print 'average degree is %f' % avrg_degree
    # print 'degree degree_distribution is ', degree_distribution
    # #
    barplot(degree_distribution)
    distplot(degree_distribution) 

    # dens, edges = density(g,True)
    # print 'density of this graph is %f' % dens
    # dens = dens*100
    # print 'in percentage the density is %f%%' % dens

    # # weiner_path = weiner_path_number(g)
    # weiner_random = weiner_random_trial(g)
    # weiner_new_new = weiner_new(g)
    # # print 'absolute weiner index is %d calculated' % weiner_path
    # print 'new weiner trials is %d' % weiner_new_new
    # print 'predicted weiner index calculated with nlogn time is %d where n is number of nodes in network' % weiner_random
    # # print 'difference between absolute and predicted is %f%%' % difference_percentage(weiner_path,weiner_random)
    # print 'difference between absolute and new is %f%%' % difference_percentage(weiner_random,weiner_new_new)

    # print vitality_distr(g)










    # mem_usage = memory_usage(load)
    # print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    # print('Maximum memory usage: %s' % max(mem_usage))
    # print('finished!')
