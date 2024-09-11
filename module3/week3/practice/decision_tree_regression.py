from sklearn.datasets import fetch_openml
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load dataset
machine_cpu = fetch_openml(name='machine_cpu')
machine_data = machine_cpu.data
machine_labels = machine_cpu.target

# Split the data 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    machine_data, machine_labels, test_size=0.2, random_state=42)

# Define the model
dt_regressor = DecisionTreeRegressor()

# Train the model
tree_regressor = dt_regressor.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = tree_regressor.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
