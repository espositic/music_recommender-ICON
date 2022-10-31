import pandas as pd
import preprocessing

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split


def various_classification():
    dataframe = pd.read_csv('../dataset/spotify_features.csv')
    features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
                "mode", "speechiness", "tempo", "time_signature", "valence"]

    dataframe = preprocessing.preprocessing_for_classification(dataframe)

    # Destiniamo l'80% del dataset per il training set.
    training = dataframe.sample(frac=0.8, random_state=420)
    X_train = training[features]
    y_train = training['popularity']
    X_test = dataframe.drop(training.index)[features]

    # Il restante 20% per il test set.
    X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)

    logistic_regression(X_train, y_train, X_valid, y_valid)
    random_forest_classifier(X_train, y_train, X_valid, y_valid)
    k_neighbors_classifier(X_train, y_train, X_valid, y_valid)
    decision_tree_classifier(X_train, y_train, X_valid, y_valid)


def logistic_regression(X_train, y_train, X_valid, y_valid):
    LR_Model = LogisticRegression()
    LR_Model.fit(X_train, y_train)
    LR_Predict = LR_Model.predict(X_valid)
    LR_Accuracy = accuracy_score(y_valid, LR_Predict)
    print("Logistic Regression.")
    print("Accuracy: " + str(LR_Accuracy))

    LR_AUC = roc_auc_score(y_valid, LR_Predict)
    print("AUC: " + str(LR_AUC))


def random_forest_classifier(X_train, y_train, X_valid, y_valid):
    RFC_Model = RandomForestClassifier()
    RFC_Model.fit(X_train, y_train)
    RFC_Predict = RFC_Model.predict(X_valid)
    RFC_Accuracy = accuracy_score(y_valid, RFC_Predict)
    print("Random Forest Classifier.")
    print("Accuracy: " + str(RFC_Accuracy))

    RFC_AUC = roc_auc_score(y_valid, RFC_Predict)
    print("AUC: " + str(RFC_AUC))


def k_neighbors_classifier(X_train, y_train, X_valid, y_valid):
    KNN_Model = KNeighborsClassifier()
    KNN_Model.fit(X_train, y_train)
    KNN_Predict = KNN_Model.predict(X_valid)
    KNN_Accuracy = accuracy_score(y_valid, KNN_Predict)
    print("K Neighbor Classifier.")
    print("Accuracy: " + str(KNN_Accuracy))

    KNN_AUC = roc_auc_score(y_valid, KNN_Predict)
    print("AUC: " + str(KNN_AUC))


def decision_tree_classifier(X_train, y_train, X_valid, y_valid):
    DT_Model = DecisionTreeClassifier()
    DT_Model.fit(X_train, y_train)
    DT_Predict = DT_Model.predict(X_valid)
    DT_Accuracy = accuracy_score(y_valid, DT_Predict)
    print("Decision Tree Classifier.")
    print("Accuracy: " + str(DT_Accuracy))

    DT_AUC = roc_auc_score(y_valid, DT_Predict)
    print("AUC: " + str(DT_AUC))

