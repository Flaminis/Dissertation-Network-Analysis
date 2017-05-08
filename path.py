from mygraph import MyGraph
from heapq import heappush, heappop
from itertools import count
import networkx as nx
def bidirectional_dijkstra(G, source, target, needpath, weight='weight'):
    # efficent shortest path
    if source == target:
        if needpath:
            return 0
        else:
            return (0, [source])
    hpush = heappush
    hpop = heappop
    # Init:   Forward             Backward
    distances  = [{},{}]  # dictionary of final distances
    paths  = [{source: [source]}, {target: [target]}]  # dictionary of paths
    fringe = [[],[]]  # heap of (distance, node) tuples for
                      # extracting next node to expand
    seen   = [{source: 0},{target: 0}]  # dictionary of distances to
                                                # nodes seen
    c = count()
    # initialize fringe heap
    hpush(fringe[0], (0, next(c), source))
    hpush(fringe[1], (0, next(c), target))
    # neighs for extracting correct neighbor information

    neighs = [G.nbrs_iterator, G.nbrs_iterator]
    # variables to hold shortest discovered path
    #finaldist = 1e30000
    finalpath = []
    dir = 1
    while fringe[0] and fringe[1]:
        # choose direction
        # dir == 0 is forward direction and dir == 1 is back
        dir = 1 - dir
        # extract closest to expand
        (dist, _, v) = hpop(fringe[dir])
        if v in distances[dir]:
            # Shortest path to v has already been found
            continue
        # update distance
        distances[dir][v] = dist  # equal to seen[dir][v]
        if v in distances[1 - dir]:
            # if we have scanned v in both directions we are done
            # we have now discovered the shortest path
            if needpath:
                return (finaldist, finalpath)
            else:
                return finaldist
        for w in neighs[dir](v):
            if(dir == 0):  # forward
                minweight = G[v][w]['weight']
                vwLength = distances[dir][v] + minweight  # G[v][w].get(weight,1)
            else:  # back, must remember to change v,w->w,v
                minweight = G[w][v].get(weight, 1)
                vwLength = distances[dir][v] + minweight  # G[w][v].get(weight,1)

            if w in distances[dir]:
                if vwLength < distances[dir][w]:
                    raise ValueError(
                        "Contradictory paths found: negative weights?")
            elif w not in seen[dir] or vwLength < seen[dir][w]:
                # relaxing
                seen[dir][w] = vwLength
                hpush(fringe[dir], (vwLength, next(c), w))
                paths[dir][w] = paths[dir][v] + [w]
                if w in seen[0] and w in seen[1]:
                    # see if this path is better than than the already
                    # discovered shortest path
                    totaldist = seen[0][w] + seen[1][w]
                    if finalpath == [] or finaldist > totaldist:
                        finaldist = totaldist
                        revpath = paths[1][w][:]
                        revpath.reverse()
                        finalpath = paths[0][w] + revpath[1:]
    return 100000
