import pandas as pd
import networkx as nx

def build_graph(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['source'], row['target'], weight=row['weight'])
    return G

if __name__ == "__main__":
    G = build_graph("data/map_graph.csv")
    print("Grafo criado com", len(G.nodes), "nós e", len(G.edges), "arestas.")
