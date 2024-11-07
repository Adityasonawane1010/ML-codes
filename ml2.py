import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
data = pd.read_csv('dataset/emails.csv')

# Step 2: Inspect dataset (optional but helpful for ensuring correct columns)
# print(data.head())
# print(data.columns)

# Assuming all columns are numerical, and 'spam' column is the target label
# If necessary, update the following to exclude non-feature columns
X = data.drop(columns=['spam','Email No.'])  # Features (all columns except 'spam and Email No.')
y = data['spam']  # Target (spam label)

# Step 3: Handle missing values (if any)
data.isnull().sum()

# Step 4: Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train and evaluate KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict on the test set
knn_predictions = knn.predict(X_test)

# Evaluate KNN performance
knn_accuracy = accuracy_score(y_test, knn_predictions)
print("KNN Accuracy: ", knn_accuracy)
print("KNN Classification Report:")
print(classification_report(y_test, knn_predictions))

# Step 6: Train and evaluate SVM model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Predict on the test set
svm_predictions = svm.predict(X_test)

# Evaluate SVM performance
svm_accuracy = accuracy_score(y_test, svm_predictions)
print("SVM Accuracy: ", svm_accuracy)
print("SVM Classification Report:")
print(classification_report(y_test, svm_predictions))

# Step 7: Visualize the comparison of both models
models = ['KNN', 'SVM']
accuracies = [knn_accuracy, svm_accuracy]

plt.bar(models, accuracies)
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()

# Step 8: Plot Confusion Matrix for KNN
plt.figure(figsize=(6, 6))
sns.heatmap(confusion_matrix(y_test, knn_predictions), annot=True, fmt='d', cmap='Blues')
plt.title('KNN Confusion Matrix')
plt.show()

# Step 9: Plot Confusion Matrix for SVM
plt.figure(figsize=(6, 6))
sns.heatmap(confusion_matrix(y_test, svm_predictions), annot=True, fmt='d', cmap='Blues')
plt.title('SVM Confusion Matrix')
plt.show()
