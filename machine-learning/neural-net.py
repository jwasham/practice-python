from sklearn import metrics
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.contrib import learn
import logging


def main():
    logging.getLogger().setLevel(logging.INFO)

    iris = learn.datasets.load_iris()

    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

    # Build a neural network with 3 hidden layers: 10, 20, 10 units respectively
    classifier = learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3, feature_columns=feature_columns)

    classifier.fit(X_train, y_train, steps=2000)

    score = metrics.accuracy_score(y_test, classifier.predict(X_test))

    print("Accuracy: {0:f}".format(score))


if __name__ == '__main__':
    main()
