from apps_class import AppList
from clustering import Clustering
import numpy as np
from visualizer import Visualizer


def main():
    numexe = 100
    numclusters = 3

    viz = Visualizer()
    clustering = Clustering()
    appList = AppList()
    appList.get_data("AppStore/AppleStore.csv", numexe + 1)

    titles = [
        "Clusters after PCA (2D), kmeans, without normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (3D), kmeans, without normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (2D), AHC, without normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (3D), AHC, without normalization, clusters #: " + str(numclusters),
        "Clusters before PCA (2D), kmeans, without normalization, clusters #: " + str(numclusters),
        "Clusters before PCA (2D), AHC, without normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (2D), kmeans, with normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (3D), kmeans, with normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (2D), AHC, with normalization, clusters #: " + str(numclusters),
        "Clusters after PCA (3D), AHC, with normalization, clusters #: " + str(numclusters),
        "Clusters before PCA (2D), kmeans, with normalization, clusters #: " + str(numclusters),
        "Clusters before PCA (2D), AHC, with normalization, clusters #: " + str(numclusters)
        ]

    arr = np.asarray(appList.retrieve_table(False))
    viz.reduce_dim(2, numexe, arr[1:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[0])
    viz.reduce_dim(3, numexe, arr[1:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[1])
    viz.reduce_dim(2, numexe, arr[1:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[2] + ", Dendrogram"), titles[2])
    viz.reduce_dim(3, numexe, arr[1:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[3] + ", Dendrogram"), titles[3])
    viz.visualize(2, numexe, arr[2:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[4])
    viz.visualize(2, numexe, arr[2:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[5] + ", Dendrogram"), titles[5])

    arr = np.asarray(appList.retrieve_table(True))
    viz.reduce_dim(2, numexe, arr[1:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[6])
    viz.reduce_dim(3, numexe, arr[1:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[7])
    viz.reduce_dim(2, numexe, arr[1:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[8] + ", Dendrogram"), titles[8])
    viz.reduce_dim(3, numexe, arr[1:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[9] + ", Dendrogram"), titles[9])
    viz.visualize(2, numexe, arr[2:], clustering.kmeans_fit(numclusters, (arr[1:]).T), titles[10])
    viz.visualize(2, numexe, arr[2:], clustering.ahc_fit(numclusters, (arr[1:]).T, titles[11] + ", Dendrogram"), titles[11])


if __name__ == "__main__":
    main()
