from pythonalgos.graph.edge import Edge

""" Module that contains the definition of a vertex in the context of a directed graph
"""

class Vertex():
    """ Class to represent details about a vertex in the context of a directed graph, 
    being the indegree, outdegree and the tails that are its successors. It inherits from the 
    generic Vertex class
    """

    def __init__(self, label, **attrs):
        """ Initialises the vertex by adding some specifics

        Args:
            label(str): the label of the vertex
            **attrs: additional attributes that define the vertex
        """
        
        self._label = label
        self._edges = list()
        self._indegree = 0
        self._attrs = attrs

    def add_edge(self, head_vertex):
        """ This method adds an edge to the set of edges maintained by the vertex

        Args: 
            head_vertex: the head vertex to be added

        """

        self._edges.append(Edge(self, head_vertex))

    def set_attr(self, attr, value):
        self._attrs[attr] = value

    def get_attr(self, attr):
        return self._attrs.get(attr)

    def get_attrs(self):
        return self._attrs

    def get_label(self):
        return self._label

    def increase_indegree(self):
        """ This method increases the indegree for the incumbent vertex """
        self._indegree += 1

    def decrease_indegree(self):
        """ This method decreases the indegree for the incumbent vertex """
        
        self._indegree -= 1

    def get_heads(self):
        return [e.get_head() for e in self._edges]

    def get_edges(self):
        return self._edges

    def get_indegree(self):
        return self._indegree

    def get_outdegree(self):
        return len(self._edges)

    def __str__(self):
        return  "outdegree: {}".format(self.get_outdegree()) + \
                ", indegree: {}".format(self.get_indegree()) + \
                ", heads: " + ",".join([str(tail.get_label()) for tail in self.get_heads()])

    
