#for final output it takes time when you use VScode 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset and drop irrelevant columns
data = pd.read_csv('./dataset/uber.csv')
data.drop(columns=['Unnamed: 0', 'key', 'pickup_datetime', 'passenger_count'], inplace=True)  # Remove unnecessary columns

print('processing...,it will take some time')

# Drop rows with missing values
data.dropna(inplace=True)

# Step 2: Identify and visualize outliers in 'fare_amount'
sns.boxplot(x=data['fare_amount'])
plt.title('Outliers in Fare')
plt.show()

# Step 3: Check correlations (numeric columns only)
numeric_data = data.select_dtypes(include='number')
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.title('Correlation Matrix')
plt.show()

# Step 4: Prepare data for model training
X = data[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']]
y = data['fare_amount']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Train Random Forest Model
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Step 5: Model Evaluation
def evaluate_model(y_true, y_pred):
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    return rmse, r2

# Evaluate Linear Regression Model
lr_rmse, lr_r2 = evaluate_model(y_test, lr_pred)
print(f"Linear Regression - RMSE: {lr_rmse}, R2: {lr_r2}")

# Evaluate Random Forest Model
rf_rmse, rf_r2 = evaluate_model(y_test, rf_pred)
print(f"Random Forest - RMSE: {rf_rmse}, R2: {rf_r2}")
