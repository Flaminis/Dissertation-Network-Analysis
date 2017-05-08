import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
    # Yerbol Kopzhassar 14000825
class MyGraph(object):
    """
    My class for graphs with no directions
    """
    node_fac = dict
    adj_fac = dict
    edge_fac = dict

    def __init__(self, **attr):
        self.node_fac = nf = self.node_fac
        self.adj_fac = self.adj_fac
        self.edge_fac = self.edge_fac

        self.additional = {}
        self.nodes = nf()
        self.adjacent = nf()
        self.edges = self.adjacent

    def __iter__(self):
        return iter(self.nodes)

    def __contains__(self, node):
        try:
            return node in self.nodes
        except TypeError:
            print('No Such Node')
            return False


    @property
    def label(self):
        return self.additional.get('label', '')

    @label.setter
    def label(self, l):
        self.attributes['label'] = l

    def __str__(self):
        return self.label

    def __getitem__(self,node_id):
        return self.adjacent[node_id]

    def __len__(self):
        return len(self.nodes)
    def description(self):
        edges = 0
        for node in range(0,len(self)):
            nbrs = list(self[node])
            nbrs_count = len(nbrs)
            edges += nbrs_count
        edges = edges/2
        print "This Graph contains %d nodes and %d edges" % (len(self.nodes),edges)
    def add_single_node(self, node, **attr):
            if node not in self.nodes:
                self.adjacent[node] = self.adj_fac()
                self.nodes[node] = attr.copy()
            else:
                self.nodes[node] = attr.update()

    def delete_node(self, node):
        adjacent = self.adjacent
        try:
            neighbors = list(adjacent[node])
            del self.nodes[node]
        except KeyError:
            print('no such key for node')
            print node
        for edges in neighbors:
            del adjacent[edges][node] # kill connections for the nodes
        del adjacent[node]

    def nodes(self, data=False):
        # ex: Graph.nodes(data=True) // esli est' infa add info
        return list(iter(self.node.items()))

    def nodes_len(self):
        return len(self.nodes)

    def node_exists(self):
        try:
            return node in self.nodes
        except TypeError:
            return False
    def add_single_edge(self, source_node, target_node, **attr):
        # if does nodes did not exist before create them
        if source_node not in self.nodes:
            self.adjacent[source_node] = self.adj_fac()
            self.nodes[source_node] = {}
        if target_node not in self.nodes:
            self.adjacent[target_node] = self.adj_fac()
            self.nodes[target_node] = {}
        # add eachother as nbrs
        enode = self.adjacent[source_node].get(target_node, self.edge_fac())
        enode.update(attr)
        self.adjacent[source_node][target_node] = enode
        self.adjacent[target_node][source_node] = enode
    # def edge_iterator(self,nodebunch=None,data=False,default=None):
    #     uzhe_bilo = {}
    #     if nodebunch is None:
    #         node
    def edge_exists(self,source,target):
        try:
            return source in self.adjacent[target]
        except KeyError:
            return False
    def neighbors_of(self, node):
        try:
            return list(self.adjacent[node])
        except KeyError:
            raise NetworkXError("this node is not on this graph VIUVIU ERROR HIHIIH %s" % (node,))
    def nbrs_iterator(self,node):
        try:
            return iter(self.adjacent[node])
        except KeyError:
            raise NetworkXError("no such node %s in the graph" % (node,))
