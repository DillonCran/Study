import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


df = pd.read_csv(
    "D:\\Projects\\Refactored_Py_DS_ML_Bootcamp-master\\11-Linear-Regression\\USA_Housing.csv"
)

# Model Evaluation
# These are not useful for linear regression
"""
TP = "True Positive"
TN = "True Negative"
FP = "False Positive"
FN = "False Negative"

Accuracy = (TP + TN) / (TP + TN + FP + FN)  # correct predictions/total predictions
Precision = TP / (TP + FP)  # matches/total predicted
Recall = TP / (TP + FN)  # matches/total actual
F1_score = 2 * (Precision * Recall) / (Precision + Recall)
"""

# Linear Regression test train split
# Mean Absolute Error (MAE) is the mean of the absolute value of the errors:
# take difference between actual and predicted values, take absolute value of that difference, and take the mean of those absolute values
# Mean Squared Error (MSE) is the mean of the squared errors:
# take difference between actual and predicted values, square that difference, and take the mean of those squared values
# Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors:
# take difference between actual and predicted values, square that difference, and take the mean of those squared values, then take the square root of that mean
# R^2 is the explained variation / total variation
# R^2 = 1 - (sum of squared residuals / sum of squared total)


# Machine learning

df.head()
df.info()

# sns.pairplot(df)
# plt.show()

# sns.displot(df["Price"], bins=50, kde=True)
# plt.show()

# df.corr()

df.columns
x = df[
    [
        "Avg. Area Income",
        "Avg. Area House Age",
        "Avg. Area Number of Rooms",
        "Avg. Area Number of Bedrooms",
        "Area Population",
    ]
]

y = df["Price"]

# This is how you use the linear regression train/test/split
# test_size is the percentage of the data that you want to be allocated to the test size
# random_state is the seed used by the random number generator
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4, random_state=101
)

# Create an instance of a LinearRegression() model named lm
lm = LinearRegression()
# Train/fit lm on the training data
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)

# Create a dataframe from the coefficients
dfs = pd.DataFrame(lm.coef_, x.columns, columns=["Coeff"])
dfs.head()

# Predictions from our model
# Pass in the X_test data and predict the y_test data
predicts = lm.predict(X_test)
plt.scatter(y_test, predicts)
plt.show()

# Residual Histogram
# You can also take the difference between the actual values and the predicted values in order to get residual values (errors)
# You can plot a histogram of these residuals to see if they are normally distributed
sns.displot((y_test - predicts), bins=50, kde=True)
plt.show()

# Regression Evaluation Metrics
# after importing metrics from sklearn, you can use these metrics to evaluate your model
# Mean Absolute Error (MAE) is the mean of the absolute value of the errors:
# take difference between actual and predicted values, take absolute value of that difference, and take the mean of those absolute values
metrics.mean_absolute_error(y_test, predicts)
# Mean Squared Error (MSE) is the mean of the squared errors:
# take difference between actual and predicted values, square that difference, and take the mean of those squared values
metrics.mean_squared_error(y_test, predicts)
# Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors:
# take difference between actual and predicted values, square that difference, and take the mean of those squared values, then take the square root of that mean
np.sqrt(metrics.mean_squared_error(y_test, predicts))

# R^2 is the explained variation / total variation
# R^2 = 1 - (sum of squared residuals / sum of squared total)
metrics.explained_variance_score(y_test, predicts)
