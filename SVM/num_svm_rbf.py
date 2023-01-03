from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
from sklearn.svm import SVC
import time

start = time.time()

df = pd.read_csv("normalized_numerical_data.csv")
X = df.drop(["gender"], axis=1)
y = df["gender"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=400)

rbf_svm = SVC(C=50, gamma=0.1,kernel='rbf')
rbf_svm.fit(X_train, y_train)

y_hat_test = rbf_svm.decision_function(X_test)
y_pred = rbf_svm.predict(X_test)
y_decision_test = (y_hat_test>=0)
R_test = (y_decision_test == y_test)
Accuracy_test = np.sum(R_test) / len(y_decision_test)
#FeatImportance = poly_svm.feature_importances_
# 0.0036274
# 0.0634853
# 0.0464139
# 0.29232
# 0.189607
# 0.148448
# 0.256099

# Output = X_test
# Output.insert(7, "gender", y_test)
# Output.insert(8, "gender_predicted", y_hat_test)
# Output.to_csv('SVMRbfNumericalResults.csv')

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

end = time.time()
print("Numerical-SVM-RBF Runtime (sec.):", end - start)

#               precision    recall  f1-score   support

#            0       0.97      0.99      0.98       503
#            1       0.99      0.97      0.98       498

#     accuracy                           0.98      1001
#    macro avg       0.98      0.98      0.98      1001
# weighted avg       0.98      0.98      0.98      1001