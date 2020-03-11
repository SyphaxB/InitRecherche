from dblp_parser_graph import *
import matplotlib.pyplot as plt
from networkx import nx
import re

dblp_path = 'resources/output.xml' # Chemin de la resource en format .xml
G = nx.DiGraph() #DiGraph = Objet pour définir un graphe orienté avec boucles.
n, e = parse_article_to_graph(dblp_path) #Méthode du DBLPParser, prend en entrée le fichier XML pour renvoyer des noeuds (nodes) et des arcs (edges).

#add_*_from : Méthode de Networkx => Il s'agit d'ajouter des élements (noeuds, arêtes/arcs) au graphe (DiGraph())
#path = '/home/halcyon/Téléchargements/dblp-data/dblp.xml'
#print(parse_article(path , include_key=False))


G.add_nodes_from(n)
G.add_edges_from(e)



#for u, v in G.edges():
#    print("Source : %s / Destination : %s" % (u, v))

#print(list(G.nodes.data()))

#for u, v, action in G.edges(data='action'):
#    if action is not None:
#        print("(%s) [%s] (%s)" % (u, action, v))


color_map = []



for n in G.nodes():
    if G.nodes[n]['parti'] == 'author':
        color_map.append('red')
    else:
        color_map.append('blue')


options = {
    'node_color': color_map,
    'line_color': 'grey',
    'linewidths': 0,
    'width': 0.1,
}


d = dict(G.degree)


noeuds_poids = []
noeuds_noms = []

for n, v in d.items() :
    noeuds_poids.append(v)
    noeuds_noms.append(n)

articles_noms = []
auteurs_noms = []
#pattern = 'tr/'
#for n in noeuds_noms :
#        result = re.match(pattern, n)
#        articles_noms.append(n)
#        if result :
#        else :
#            auteurs_noms.append(n)

#Afficher la liste des publications de chaque auteur
for n in auteurs_noms :
    print("Voisins de {} : {}".format(n, list(G.neighbors(n))))



pos = nx.spring_layout(G)
#nx.draw(G, pos, font_size=16, with_labels=False,**options)
nx.draw(G, pos, nodelist=noeuds_noms, node_size=[v * 100 for v in noeuds_poids], **options)
for p in pos:  # raise text positions
    pos[p][1] += 0.07
nx.draw_networkx_labels(G, pos)
plt.show()
