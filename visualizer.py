from sklearn.decomposition import PCA as sklearnPCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


class Visualizer:

    @staticmethod
    def reduce_dim(desired, size, table, labels, title="", show=False):
        sklearn_pca = sklearnPCA(n_components=desired)
        sklearn_transf = sklearn_pca.fit_transform(table.T)
        if desired == 2:
            plt.scatter(sklearn_transf[0:size, 0], sklearn_transf[0:size, 1], c=labels)
            plt.title(title)
            plt.savefig("images/" + title + ".png")
        elif desired == 3:
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')
            plt.rcParams['legend.fontsize'] = 10
            ax.scatter(sklearn_transf[0:size, 0], sklearn_transf[0:size, 1], sklearn_transf[0:size, 2], c = labels)
            plt.title(title)
            plt.savefig("images/" + title + ".png")

        if show:
            plt.show()
        else:
            plt.close()

        return sklearn_transf

    @staticmethod
    def visualize(desired, size, table, labels, title="", show=False):
        if desired == 2:
            plt.scatter(table.T[0:size, 0], table.T[0:size, 1], c=labels)
            plt.title(title)
            plt.savefig("images/" + title + ".png")
        elif desired == 3:
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')
            plt.rcParams['legend.fontsize'] = 10
            ax.scatter(table.T[0:size, 0], table.T[0:size, 1], table.T[0:size, 2], c = labels)
            plt.title(title)
            plt.savefig("images/" + title + ".png")

        if show:
            plt.show()
        else:
            plt.close()