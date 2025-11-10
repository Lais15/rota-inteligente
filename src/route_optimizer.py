import pandas as pd
from src.graph_builder import build_graph
from src.clustering import cluster_points
from src.astar import astar
from src.visualize import plot_graph

def run():
    G = build_graph("data/map_graph.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    coords = deliveries[['lat', 'lon']].values

    labels, centers = cluster_points(coords, k=2)
    deliveries['cluster'] = labels

    positions = {'A': (1,1), 'B': (2,1), 'C': (3,2), 'D': (4,3), 'E': (1.5,3.5)}
    path, cost = astar(G, 'A', 'E', positions)
    print(f"Menor caminho entre A e E: {path} (Custo {cost})")

    plot_graph(G, positions, path, "docs/diagram.png")

if __name__ == "__main__":
    run()
