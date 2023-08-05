import pandas as pd

class ClassificationModels:
    """"""

    def __init__(self, X, y):
        if all(data is None for data in [X,y]):
            raise TypeError('dataset expected but not passed')
            return
        if(self.__check_dataset(X, y)):
            self._X = X
            self._y = y
            self._scoresAll = {}
            self._rocAucAll = {}
            self._precisionAll = {}
            self._f1All = {}
            self._accuracyAll = {}
            self._recallAll = {}
        else:
            raise TypeError('Dataset does not pass requirements. Kindly read in the help section of what dataset to pass. ')
            return

    def __check_dataset(self, X, y):
        return True

    def compare_models(self, test_size = 0.3):

        """  """

        # Imports
        from sklearn.model_selection import train_test_split
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import StandardScaler
        from sklearn.datasets import make_moons, make_circles, make_classification
        from sklearn.neural_network import MLPClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.svm import SVC
        from sklearn.gaussian_process import GaussianProcessClassifier
        from sklearn.gaussian_process.kernels import RBF
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
        from sklearn.naive_bayes import GaussianNB
        from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_curve, roc_auc_score


        __X_train, __X_test, __y_train, __y_test = train_test_split(self._X, self._y, test_size=test_size, random_state=42)

        __names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
        "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
        "Naive Bayes", "QDA"]

        __classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis()]

        for name, clf in zip(__names, __classifiers):
            clf.fit(__X_train, __y_train)
            __y_pred = clf.predict(__X_test)
            self._scoresAll[name] = clf.score(__X_test, __y_test)
            self._rocAucAll[name] = roc_auc_score(__y_test, __y_pred)
            self._precisionAll[name] = precision_score(__y_test, __y_pred)
            self._f1All[name] = f1_score(__y_test, __y_pred)
            self._accuracyAll[name] = accuracy_score(__y_test, __y_pred)
            self._recallAll[name] = recall_score(__y_test, __y_pred)

            print(name,  ': ', self._scoresAll[name])
