from sklearn import tree

TEXTURE_BUMPY = 0
TEXTURE_SMOOTH = 1

LABEL_APPLE = 0
LABEL_ORANGE = 1

LABELS = {
    LABEL_APPLE: 'apple',
    LABEL_ORANGE: 'orange',
}


def classify(to_classify):
    features = [
        [90, TEXTURE_BUMPY],
        [140, TEXTURE_SMOOTH],
        [130, TEXTURE_SMOOTH],
        [150, TEXTURE_BUMPY],
        [170, TEXTURE_BUMPY],
    ]
    labels = [
        LABEL_ORANGE,
        LABEL_APPLE,
        LABEL_APPLE,
        LABEL_ORANGE,
        LABEL_ORANGE
    ]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    return clf.predict(to_classify)


def main():
    to_classify = [
        [160, TEXTURE_BUMPY],
        [145, TEXTURE_BUMPY],
        [120, TEXTURE_SMOOTH],
        [100, TEXTURE_BUMPY],
    ]

    decisions = classify(to_classify)

    for decision in decisions:
        print("It's a(n):", LABELS[decision])


if __name__ == '__main__':
    main()
