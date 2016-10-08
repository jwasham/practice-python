import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris


def main():
    iris = load_iris()

    print(iris.feature_names)
    print(iris.target_names)

    # print(iris.data[0])
    # print(iris.target[0])

    test_idx = [0, 50, 100]

    train_target = np.delete(iris.target, test_idx)
    train_data = np.delete(iris.data, test_idx, axis=0)

    test_target = iris.target[test_idx]
    test_data = iris.data[test_idx]

    # print(test_target)
    # print(test_data)

    clf = tree.DecisionTreeClassifier()
    clf.fit(train_data, train_target)

    print('actual:', test_target)
    print('predicted:', clf.predict(test_data))


if __name__ == '__main__':
    main()
