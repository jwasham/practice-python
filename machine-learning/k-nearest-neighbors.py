import numpy as np
# from scipy.spatial import distance
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


class KNNClassifier(object):
    def __init__(self):
        self.X_train = None
        self.y_train = None

    def euc_distance(self, a, b):
        return np.linalg.norm(a-b)
        # return distance.euclidean(a, b)

    def closest(self, row):
        """
        Returns the label corresponding to the single closest training example.
        This is a k=1 nearest neighbor(s) implementation.
        :param row:
        :return:
        """
        dist = [self.euc_distance(row, trainer) for trainer in self.X_train]
        best_index = dist.index(min(dist))

        return self.y_train[best_index]

    def fit(self, training_data, training_labels):
        self.X_train = training_data
        self.y_train = training_labels

    def predict(self, to_classify):
        predictions = []
        for row in to_classify:
            label = self.closest(row)
            predictions.append(label)

        return predictions

iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

classifier = KNeighborsClassifier()  # k=5 by default
# classifier = KNNClassifier()
classifier.fit(X_train, y_train)

# print(y_train)

results = classifier.predict(X_test)

score = metrics.accuracy_score(y_test, results)

print("Accuracy: {0:f}".format(score))
