import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


class Clustering:

    @staticmethod
    def kmeans_fit(nclusters, table):
        # create kmeans object
        kmeans = KMeans(n_clusters=nclusters)
        # fit kmeans object to data
        kmeans.fit(table)
        # print location of clusters learned by kmeans object
        print(kmeans.cluster_centers_)
        # save new clusters for chart
        y_km = kmeans.fit_predict(table)

        return y_km

    @staticmethod
    def ahc_fit(nclusters, table, title="", show=False):
        # create dendrogram
        dendrog = sch.dendrogram((sch.linkage(table, method='ward')))
        plt.title(title)
        plt.savefig("images/" + title + ".png")
        if show:
            plt.show()
        else:
            plt.close()
        # create clusters
        hc = AgglomerativeClustering(n_clusters=nclusters, affinity='euclidean', linkage='ward')
        # save clusters for chart
        y_hc = hc.fit_predict(table)

        return y_hc