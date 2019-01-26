"""
Mesh module that will define the mesh.
"""


class Mesh(object):
    """define a mesh that will handle degrees-of-freedom (dof), element lengths
    etc."""

    def __init__(self, length, loads, reactions, dof):
        self._nodes = self.__get_nodes(length, loads, reactions)
        self._lengths = self.__get_lengths()
        self._num_elements = len(self.lengths)
        self._dof = dof * self.num_elements + dof

    @property
    def nodes(self):
        return self._nodes

    @property
    def dof(self):
        return self._dof

    @property
    def lengths(self):
        return self._lengths

    @property
    def num_elements(self):
        return self._num_elements

    def __get_lengths(self):
        # Calculate the lengths of each element
        lengths = []
        for k in range(len(self.nodes) - 1):
            lengths.append(self.nodes[k + 1] - self.nodes[k])
        return lengths

    def __get_nodes(self, length, loads, reactions):
        nodes = [0]  # ensure first node is always at zero (0)
        for param in loads + reactions:
            nodes.append(param.location)
        nodes.append(length)  # ensure last node is at the end of the beam
        nodes = list(set(nodes))   # remove duplicates
        nodes.sort()
        return nodes

    def __str__(self):
        s = ('MESH PARAMETERS\n'
            f'Number of elements: {self.num_elements}\n'
            f'Node locations: {self.nodes}\n'
            f'Element Lengths: {self.lengths}\n'
            f'Total degrees of freedom: {self.dof}\n')
        return s