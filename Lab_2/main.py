##################################
#### Created by Andrea Bena' #####
##################################

import numpy
import matplotlib.pyplot as plt

folder_path = "Datasets/iris/iris.csv"


def reshape_to_col(row):
    return row.reshape(row.size, 1)


def load(file_path):
    labels_values = {
        "Iris-setosa": 0,
        "Iris-versicolor": 1,
        "Iris-virginica": 2
    }
    labels_set = []
    dataset = []

    with open(file_path, 'r') as f:
        for line in f:
            try:
                *data, label = line.split(',')[0:5]
                value = labels_values[label.strip()]
                labels_set.append(value)
                dataset.append(reshape_to_col(numpy.array(list(float(i) for i in data))))
            except IOError:
                pass

    return numpy.hstack(dataset), numpy.array(labels_set, dtype=numpy.int32)


def plot_hist(dataset, label):
    data_0 = dataset[:, label == 0]
    data_1 = dataset[:, label == 1]
    data_2 = dataset[:, label == 2]

    h_fea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
    }

    for dIdx in range(len(h_fea)):
        plt.figure()
        plt.xlabel(h_fea[dIdx])
        plt.hist(data_0[dIdx, :], bins=10, density=True, alpha=0.4, label='Setosa')
        plt.hist(data_1[dIdx, :], bins=10, density=True, alpha=0.4, label='Versicolor')
        plt.hist(data_2[dIdx, :], bins=10, density=True, alpha=0.4, label='Virginica')

        plt.legend()
        plt.tight_layout()  # Use with non-default font size to keep axis label inside the figure
        plt.savefig('../hist_%d.pdf' % dIdx)
    plt.show()


def plot_scatter(dataset, label):
    data_0 = dataset[:, label == 0]
    data_1 = dataset[:, label == 1]
    data_2 = dataset[:, label == 2]

    h_fea = {
        0: 'Sepal length',
        1: 'Sepal width',
        2: 'Petal length',
        3: 'Petal width'
    }

    for dIdx1 in range(4):
        for dIdx2 in range(4):
            if dIdx1 == dIdx2:
                continue
            plt.figure()
            plt.xlabel(h_fea[dIdx1])
            plt.ylabel(h_fea[dIdx2])
            plt.scatter(data_0[dIdx1, :], data_0[dIdx2, :], label='Setosa')
            plt.scatter(data_1[dIdx1, :], data_1[dIdx2, :], label='Versicolor')
            plt.scatter(data_2[dIdx1, :], data_2[dIdx2, :], label='Virginica')

            plt.legend()
            plt.tight_layout()  # Use with non-default font size to keep axis label inside the figure
            # plt.savefig('./scatter_%d_%d.pdf' % (dIdx1, dIdx2))
        plt.show()


def load2():
    # The dataset is already available in the sklearn library (pay attention that the library represents samples as row
    # vectors, not column vectors - we need to transpose the data matrix)
    import sklearn.datasets
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']


if __name__ == '__main__':
    values, labels = load(folder_path)
    # values, labels = load2()

    # Change default font size - comment to use default values
    plt.rc('font', size=16)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)

    plot_hist(values, labels)
    plot_scatter(values, labels)
