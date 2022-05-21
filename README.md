# Rainfall_Prediction 
This app predicts if tomorrow is going to rain or not. 
This prediction is done with the help of various inputs entered by the user such as: Location, Humidity, Temprature, Pressure, etc.
It can be a great tool if you have to carry an umbrella if are in Australia.

## Data Collection
[Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package?datasetId=6012&sortBy=voteCount)

## Life Cycle of the Project
1. Exploratory Data Analysis
    - Bivariate Analysis(Distplot)
    - Numerical Features & Categorical Features
    - Correlation
    - Outlier Detection(Boxplot)
2. Handeling Missing Values
    - Random Sample Imputation for numerical features
    - Mode Imputation for categorical features 
3. Feature Engineering
    - One Hot Encoding 
    - Label Encoding
4. Treating Outliers
    - InterQuantile Range(a= 1.5)
5. Handeling the Imbalanced Data
    - SMOTE
6. Model Training
    - Logistic Regression
    - CatBoost Classifier
    - Random Forest Classifier
    - XGBoost Classifier
    - K Neighbors Classifier
7. Evaluation Metrics
    - Accuracy Score
    - Confusion Matrix
    - Classification Report
    - AUC Curve

## Model Metrics
Algorithm  | Accuracy | AUC
------------- | ------------- | ------
CatBoost Classifier  | 0.86 | 0.89
Random Forest Classifier  | 0.84 | 0.88
LogisticRegression | 0.77 | 0.85
KNeighborsClassifier | 0.75 | 0.79
XGBClassifier | 0.86 | 0.88



The final metrics used is AUC.
And the model is **CatBoost Classifier** since it hast the highest **AUC score of 89%**

## Limitations and Improvements
1. The models can be hyperparameter tuned with the use of Grid Search or Random Search.
2. Feature transformation like Standardization, Log Transformation, etc
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Rainfall_Prediction
```

Create conda environment

```bash
  conda env create rainfall-prediction
```

Activate conda environment

```bash
  conda activate rainfall-prediction
```

Install dependencies

```bash
  conda list --export > requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

