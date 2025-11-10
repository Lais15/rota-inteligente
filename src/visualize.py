import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G, pos, path=None, save_path="docs/diagram.png"):
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)
    if path:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color='r')
    plt.title("Diagrama de Rotas – A*")
    plt.savefig(save_path)
    plt.close()
    print(f"✅ Diagrama salvo em {save_path}")
