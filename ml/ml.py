# Tutorial:
# https://365datascience.com/tutorials/python-tutorials/predictive-model-python/

from sklearn.metrics import classification_report
from sklearn import metrics
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# We’ll build a binary logistic model step-by-step to predict floods
# based on the monthly rainfall index for each year in Kerala, India.

# Step 1: Read the Dataset
df = pd.read_csv('kerala.csv')

#   SUBDIVISION  YEAR   JAN   FEB   MAR    APR    MAY     JUN     JUL    AUG    SEP    OCT    NOV    DEC   ANNUAL RAINFALL FLOODS
# 0      KERALA  1901  28.7  44.7  51.6  160.0  174.7   824.6   743.0  357.5  197.7  266.9  350.8   48.4            3248.6    YES
# 1      KERALA  1902   6.7   2.6  57.3   83.9  134.5   390.9  1205.0  315.8  491.6  358.4  158.3  121.5            3326.6    YES
# 2      KERALA  1903   3.2  18.6   3.1   83.6  249.7   558.6  1022.5  420.2  341.8  354.1  157.0   59.0            3271.2    YES
# 3      KERALA  1904  23.7   3.0  32.2   71.5  235.7  1098.2   725.5  351.8  222.7  328.1   33.9    3.3            3129.7    YES
# 4      KERALA  1905   1.2  22.3   9.4  105.9  263.3   850.2   520.5  293.6  217.2  383.5   74.4    0.2            2741.6     NO
print(df.head(5))

# Step 2: Explore the Dataset
df.info()
print(df.shape)
print(df.describe())
print(df.corr(numeric_only=True))

df['FLOODS'].replace(['YES', 'NO'], [1, 0], inplace=True)
print(df.head(5))

# Step 3: Feature Selection
X = df.iloc[:, 1:14]   # all features
Y = df.iloc[:, -1]   # target output (floods)

# Use the SelectKBest library to run a chi-squared statistical test and select the top 3 features that are most related to floods.
best_features = SelectKBest(score_func=chi2, k=3)
fit = best_features.fit(X, Y)

# Now we create data frames for the features and the score of each feature:
df_scores = pd.DataFrame(fit.scores_)
df_columns = pd.DataFrame(X.columns)

# Finally, we’ll combine all the features and their corresponding scores in one data frame:
features_scores = pd.concat([df_columns, df_scores], axis=1)
features_scores.columns = ['Features', 'Score']

# Here, we notice that the top 3 features that are most related to the target output are:
# 'SEP' which is the rainfall index in September
# 'JUN' is the rainfall index in June
# 'JUL' is the rainfall index in July
print(features_scores)
print(features_scores.sort_values(by='Score'))

# Step 4: Build the Model
X = df[['SEP', 'JUN', 'JUL']]  # the top 3 features
Y = df[['FLOODS']]  # the target output

# Second, split the dataset into train and test:
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.4, random_state=100)

# Third, create a logistic regression body:
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Finally, we predict the likelihood of a flood using the logistic regression body we created:
y_pred = logreg.predict(X_test)
print(X_test)  # test dataset
print(y_pred)  # predicted values


print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print('Recall: ', metrics.recall_score(y_test, y_pred, zero_division=1))
print("Precision:", metrics.precision_score(y_test, y_pred, zero_division=1))
print("CL Report:", metrics.classification_report(
    y_test, y_pred, zero_division=1))
