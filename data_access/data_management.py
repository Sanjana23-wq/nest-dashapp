

import sys
import os
import io
import pandas as pd
import joblib
import xgboost
# Set the console encoding to UTF-8
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import os
import sys
import xgboost as xgb
import numpy as np
from sklearn.datasets import make_regression
# from sklearn.model_selection import train_test_split
from lime.lime_tabular import LimeTabularExplainer
# Add the desired path to sys.path
sys.path.append(os.path.join("e:", "dashappnest", "venv", "lib", "site-packages"))

# Verify by printing the updated sys.path
print(sys.path)
def get_lime(nct_id):
    column_dict=joblib.load("E:\Dashappnest\Datasets\column_rename_dict.pkl")
    print(column_dict)
    # Load your train and test datasets 
    train_data = pd.read_csv('E:/Dashappnest/Datasets/train_small_model_input.csv')
    test_data = pd.read_csv('E:/Dashappnest/Datasets/test_small_model_input.csv')

    print('Test data:')
    print(test_data.head())
    print('Train data:')
    print(train_data.head())
    #rename columns 
    train_data.rename(columns=column_dict, inplace=True)
    test_data.rename(columns=column_dict, inplace=True)

    print("Columns in train_data after renaming:", train_data.columns)
    print("Columns in test_data after renaming:", test_data.columns)

    print("Original columns in train_data:")
    print(train_data.columns)

    print("Original columns in test_data:")
    print(test_data.columns)

    # Drop columns with all NaN values (optional, only if needed)
    train_data = train_data.dropna(axis=1, how='all')
    test_data = test_data.dropna(axis=1, how='all')

    y=train_data['time_taken_for_enrollment']
    train_data=train_data.drop(columns=['zip','time_taken_for_enrollment','nct_id'])
    test_instance = test_data[test_data['nct_id']==nct_id]
    test_instance=test_instance.drop(columns=['nct_id'])
    print(test_instance.shape)
    test_data=test_data.drop(columns=['nct_id'])



    # Verify the renamed columns
    print("Columns in train_data after renaming:")
    print(train_data.columns)

    print("Columns in test_data after renaming:")
    print(test_data.columns)

    model=joblib.load("E:/Dashappnest/Datasets/xgb_trained.pkl")
    print(model)


    predictions=model.predict(test_instance)
    print(predictions)



    train_data_np = train_data.to_numpy() 

    new_to_old_column=joblib.load("E:/Dashappnest/Datasets/new_to_old_column.pkl")
    train_data.rename(columns=new_to_old_column, inplace=True)

    # Initialize the LIME explainer
    explainer = LimeTabularExplainer(
        training_data=train_data_np,  # Training data for the explainer
        mode="regression",  # Regression mode, since you're using XGBoost for regression
        training_labels=y,  # Target values (regression targets)
        feature_names=train_data.columns.tolist(),  # Feature names
        verbose=True,
        random_state=42
    )
    print("lime loaded")
    # Explain the prediction for the selected test instance
    explanation = explainer.explain_instance(test_instance, model.predict)
    print('explained')
    # Get the explanation as a list of feature contributions
    local_explanation = explanation.as_list()


    return local_explanation



