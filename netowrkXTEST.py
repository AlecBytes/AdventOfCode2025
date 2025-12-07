import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
rows = 10
cols = 10
for i in range(rows):
    for j in range(cols):
        G.add_node((i, j), value='.')

pos = {(i, j): (j, -i) for i in range(rows) for j in range(cols)}
labels = {(i, j): G.nodes[(i, j)]['value'] for i in range(rows) for j in range(cols)}

nx.draw(
    G,
    pos,
    # with_labels=True,
    labels=labels,
    node_size=500,
    font_size=8,
    node_color="green"
)

plt.show()