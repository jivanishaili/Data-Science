import os
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

MODEL_FILE = "model.pkl"
PIPELELINE_FILE = "pipeline.pkl"

def build_pipeline (num_attribs, cat_attribs):
        # For Numerical pipeline
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    
    # For Categorical pipeline
    cat_pipeline = Pipeline([
        # ("ordinal", OrdinalEncoder())  # Use this if you prefer ordinal encoding
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    
    # construct the Full pipeline
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", cat_pipeline, cat_attribs),
    ])

    return full_pipeline

if not os.path.exists(MODEL_FILE):
    # lets train the model
    housing = pd.read_csv("housing.csv")
 
    # 2. Create a stratified test set based on income category
    housing["income_cat"] = pd.cut(
        housing["median_income"],
        bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
        labels=[1, 2, 3, 4, 5]
    )
    
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        housing.loc[test_index].drop("income_cat", axis=1).to_csv("input.csv",index=False)
        housing=housing.loc[train_index].drop("income_cat", axis=1)
       
    housing_labels = housing["median_house_value"].copy()
    housing_features = housing.drop("median_house_value", axis=1)
    
    num_attribs = housing_features.drop("ocean_proximity", axis=1).columns.tolist()
    cat_attribs = ["ocean_proximity"]
    
    preprocessor = build_pipeline(num_attribs, cat_attribs)
    housing_prepared = preprocessor.fit_transform(housing_features)
    
    model = RandomForestRegressor(random_state=42)
    model.fit(housing_prepared, housing_labels)
    
    joblib.dump(model, MODEL_FILE)
    joblib.dump(preprocessor, PIPELELINE_FILE)
    print("Model is trained. congrats!")
else:
    # Lets do inference
    model = joblib.load(MODEL_FILE)
    preprocessor = joblib.load(PIPELELINE_FILE)
    
    input_data = pd.read_csv('input.csv')
    transformed_input = preprocessor.transform(input_data)
    predictions = model.predict(transformed_input)
    input_data['median_house_value'] = predictions
    
    input_data.to_csv('output.csv', index=False)
    print("Inference complete. Results saved to output.csv")