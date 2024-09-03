import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import datasets
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Split train:test = 8:2
X_train, X_test, y_train, y_test = train_test_split(
    diabetes_X, diabetes_y, test_size=0.2, random_state=42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build KNN model
knn_regression = KNeighborsRegressor(n_neighbors=5)
knn_regression.fit(X_train, y_train)

# Predict and Evaluate test set
y_pred = knn_regression.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f'R2 Score of KNN Regressor: {r2:.2f}')

r2_scores = []
for k in range(1, 31):
    knn_regression = KNeighborsRegressor(n_neighbors=k)
    knn_regression.fit(X_train, y_train)
    y_pred = knn_regression.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    r2_scores.append(r2)

sns.lineplot(x=range(1, 31), y=r2_scores, marker='o')
plt.xlabel('K Values')
plt.ylabel('R2 Score')
print(np.argmax(r2_scores), max(r2_scores))
