import sys
import numpy as np
from collections import Counter
from .NodeClass import Node

class DecisionTreeClassifier():
    
    def __init__(self, max_depth):
        self.max_depth = max_depth
    
    def fit(self, X, y):
        """Build decision tree classifier."""
        self.n_classes_ = len(set(y))
        self.n_features_ = X.shape[1]
        self.tree_ = self._grow_tree(X, y)
        
    def predict(self, X):
        """Predict class for X"""
        return [self._predict(inputs) for inputs in X]
    
    def _gini(self, y):
        """
        Args:
        labels: vector of class labels

        Returns:
        float: Gini of current node

        """
        #class_population = _class_population(y)
        m = len(y)
        return 1.0 - sum((np.sum(y == c) / m) ** 2 for c in range(self.n_classes_))
    
    def _find_best_split(self, X, y):
        """Find the best split using gini index

        Args:
        X (matrix): input dataframe
        y (vector): classification labels

        Returns:
        int: index of the best feature
        int: index of the best cutoff for the feature

        """
        m = len(y)
        best_idx, best_idx_thr = None, None

        # at least include two elements
        if m <= 1:
            return None, None

        num_obs = [np.sum(y == c) for c in range(self.n_classes_)]
        best_gini = 1.0 - sum((n / m) ** 2 for n in num_obs)

        for idx in range(self.n_features_): # loop through all features
            # sort a feature and get sorted values and corresponding labels
            thresholds, classes = zip(*sorted(zip(X[:, idx], y)))
            num_left = [0] * self.n_classes_
            num_right = num_obs.copy()
            for i in range(1, m): # loop through all values
                c = classes[i-1]
                num_left[c] += 1
                num_right[c] -= 1
                # gini of the left node
                gini_left = 1.0 - sum((num_left[x] / i) ** 2 for x in range(self.n_classes_))

                # gini of the right node
                gini_right = 1.0 - sum((num_right[x] / (m - i)) ** 2 for x in range(self.n_classes_))

                # the gini index of a split is the weighted of gini values
                gini_index = gini_left * i/m + gini_right * (m - i)/m

                if thresholds[i] == thresholds[i - 1]:
                    continue
                if gini_index < best_gini:
                    best_gini = gini_index
                    best_idx = idx
                    best_idx_thr = (thresholds[i] + thresholds[i - 1]) / 2

        return best_idx, best_idx_thr
    
    def _grow_tree(self, X, y, depth=0):
        """
        Recursively find the best split and grow
        """
        #The predicted class is the one with largest population.
        num_samples_per_class = [np.sum(y == i) for i in range(self.n_classes_)]
        predicted_class = np.argmax(num_samples_per_class)
        node = Node(gini = self._gini(y),
                    num_samples = len(y),
                    num_samples_per_class = num_samples_per_class,
                    predicted_class = predicted_class)

        # Split recursively until maximum depth is reached.
        if depth < self.max_depth:
            idx, thr = self._find_best_split(X, y)
            if idx is not None:
                indices_left = X[:, idx] < thr
                X_left, y_left = X[indices_left], y[indices_left]
                X_right, y_right = X[~indices_left], y[~indices_left]

                node.feature_index = idx
                node.threshold = thr
                node.left = self._grow_tree(X_left, y_left, depth + 1)
                node.right = self._grow_tree(X_right, y_right, depth + 1)
        return node
    
    def _predict(self, inputs):
        """Predict class for a single sample."""
        node = self.tree_
        while node.left:
            if inputs[node.feature_index] < node.threshold:
                node = node.left
            else:
                node = node.right
        return node.predicted_class
