import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def clustering(dataFrame, songs):
    """sse={}
    DF = dataFrame(songs.drop(['track_name', 'artist_name'], axis = 1))
    for k in range(1, 30,3):
        kmeans = KMeans(n_clusters=k, max_iter=100).fit(DF)
        DF["clusters"] = kmeans.labels_
        sse[k] = kmeans.inertia_
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.title("Elbow method")
    plt.xlabel("Number of cluster")
    plt.show()"""
    DF = pd.DataFrame(songs.drop(['track_name', 'artist_name'], axis=1))
    kmeans = KMeans(n_clusters=17)
    songs['Cluster'] = kmeans.fit_predict(DF)