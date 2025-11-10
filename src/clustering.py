from sklearn.cluster import KMeans

def cluster_points(coords, k=2):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(coords)
    return labels, kmeans.cluster_centers_
