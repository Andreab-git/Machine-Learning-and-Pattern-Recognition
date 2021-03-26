import numpy
from scipy import linalg
import matplotlib.pyplot as plt

folder_path = "Datasets/iris/iris.csv"


def v_col(row):
    return row.reshape(row.size, 1)


def v_row(row):
    return row.reshape(1, row.size)


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
                dataset.append(v_col(numpy.array(list(float(i) for i in data))))
            except IOError:
                pass

    return numpy.hstack(dataset), numpy.array(labels_set, dtype=numpy.int32)


def load2():
    # The dataset is already available in the sklearn library (pay attention that the library represents samples as row
    # vectors, not column vectors - we need to transpose the data matrix)
    import sklearn.datasets
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']


if __name__ == '__main__':

    int_to_label = {
        0: 'Iris-setosa',
        1: 'Iris-versicolor',
        2: 'Iris-virginica'
    }

    dataset, labels = load(folder_path)
    dataset_mean = v_col(dataset.mean(axis=1))
    dataset_classes = numpy.array([dataset[:, labels == i] for i in set(labels)])

    SB = 0.0
    for i in range(len(dataset_classes)):
        class_mean = dataset_classes[i].mean(axis=1).reshape((4, 1))  # Reshape because it initially is (4,)
        SB += dataset_classes[i].shape[1] * numpy.dot(class_mean - dataset_mean, (class_mean - dataset_mean).T)
    SB = SB / dataset.shape[1]

    SW = 0.0
    for i in range(len(dataset_classes)):
        class_mean = dataset_classes[i].mean(axis=1).reshape((4, 1))  # Reshape because it initially is (4,)
        SWt = 0.0
        for sample in dataset_classes[i].T:
            sample_reshaped = sample.reshape((4, 1))  # Reshape because it initially is (4,)
            SWt += numpy.dot(sample_reshaped - class_mean, (sample_reshaped - class_mean).T)
        SW += SWt
    SW = SW / dataset.shape[1]

    U, Sigma, _ = linalg.svd(SW)  # _ is needed because of return error if missing. Anyway its value is not used
    Sigma = numpy.diag(Sigma)  # Diag returns a 1-D array, we need a square matrix

    # Method used by professor Cumani seems inconsistent and causes errors
    Sigma = linalg.fractional_matrix_power(Sigma, -0.5)

    P1 = numpy.dot(numpy.dot(U, Sigma), U.T)

    SBT = numpy.dot(numpy.dot(P1, SB), P1.T)

    # highest eigenvalues
    m = 2
    eigs, eigvs = linalg.eigh(SBT)
    eigvs = eigvs[:, ::-1]
    P2 = eigvs = eigvs[:, :m]

    dataset_lda = numpy.dot(numpy.dot(P2.T, P1), dataset)

    print(Sigma)

    for i in range(3):
        to_plot = dataset_lda[:, labels == i]
        plotted = plt.scatter(-to_plot[0, :], -to_plot[1, :])
        plotted.set_label(int_to_label[i])
    plt.legend()
    plt.show()
