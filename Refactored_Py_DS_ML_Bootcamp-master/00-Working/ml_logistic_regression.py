import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

cf.go_offline()


train = pd.read_csv(
    "D:\\Projects\\Study\\Refactored_Py_DS_ML_Bootcamp-master\\13-Logistic-Regression\\titanic_train.csv"
)
print(train.head())

# Exploratory Data Analysis
# You can check what data is missing with a heatmap
sns.heatmap(train.isnull())
plt.show()
# You can see the cabin and age columns are missing a lot of data.
# The age column still has enough data to fill in the missing values by extrapolating from the other data.
# The cabin column is missing too much data to do anything useful with it.

sns.set_style("whitegrid")
# breaks down survivors by class
sns.countplot(x="Survived", data=train, hue="Pclass")
plt.show()

# Shows age distribution of passengers
sns.displot(train["Age"].dropna(), kde=False, bins=30)
plt.show()

# Shows number of family members on board
sns.countplot(data=train, x="SibSp")
plt.show()

# Shows average age of passengers by class
sns.boxplot(x="Pclass", y="Age", data=train)
plt.show()


# for data that is missing some entries, you can imputate the missing data
# For the missing Age data, we will extrapolate the average age for each class
def impute_age(cols):
    # cols is a list of the columns in the dataframe
    Age = cols[0]
    Pclass = cols[1]

    # if the age is null, return the average age for the class
    if pd.isnull(Age):
        if Pclass == 1:
            return train[train["Pclass"] == 1]["Age"].mean()
        elif Pclass == 2:
            return train[train["Pclass"] == 2]["Age"].mean()
        else:
            return train[train["Pclass"] == 3]["Age"].mean()
    # if the age is not null, return the age
    else:
        return Age


# Applying the imputation function to the dataframe
# pull both the age and class columns and apply the imputation function to them onto the age col in the dataframe
train["Age"] = train[["Age", "Pclass"]].apply(impute_age, axis=1)


# Printing heatmap to show that the age column is now filled in
sns.heatmap(data=train.isnull())
plt.show()

# Since the cabin column is missing too much data, we will drop it
train.drop("Cabin", axis=1, inplace=True)

# Some other columns are missing a few entries, so we will drop those rows
train.dropna(inplace=True)


# Converting categorical features into dummy variables
# This is necessary because the machine learning algorithm will not be able to use the categorical data, only numerical data

# This will create a new column for each unique value in the categorical column (Female & Male)
# When we drop the first column, that leaves a single column with a bool value for each row.
# The machine learning algorithm can use this data to know weather a person is male/female based on the binary value.
sex = pd.get_dummies(train["Sex"], drop_first=True)
# Same with the embarked column, because the categorical data is not numerical, we need to convert it to numerical data by creating a new column for each unique value
# Because the data cannot be extrapolated from the bool values, we will not drop the first column.
embark = pd.get_dummies(train["Embarked"])

# Now we can drop the categorical columns and add the new numerical columns
train = pd.concat([train, sex, embark], axis=1)
# And with this we drop the categorical cols, leaving only numerical data for the machine learning algorithm
train.drop(["Sex", "Embarked", "Name", "Ticket"], axis=1, inplace=True)
# setting True/False values to 0 or 1
train["male"] = train["male"].astype(int)
train["C"] = train["C"].astype(int)
train["Q"] = train["Q"].astype(int)
train["S"] = train["S"].astype(int)

print(train.head())
