import networkx as nx

from database.DAO import DAO
from model.aeroporto import Aeroporto


class Model:
    def __init__(self):
        self._lista_aeroporti = DAO.getAllAeroporti()
        self._idMapAeroporti={}
        for i in self._lista_aeroporti:
            self._idMapAeroporti[i.ID]=i


    def build_graph(self,x):
        grafo=nx.Graph()
        elenco_edges=DAO.getEdges(x)
        for edge in elenco_edges:
            aeroportoP=self._idMapAeroporti[edge[0]]
            aeroportoA=self._idMapAeroporti[edge[1]]
            distanza_media=edge[2]
            grafo.add_edge(aeroportoP,aeroportoA, weight=distanza_media)

        return len(grafo.nodes), len(grafo.edges), grafo
