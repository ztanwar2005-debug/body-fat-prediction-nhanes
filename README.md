# Predicting Body Fat Percentage Using Machine Learning

## Overview

This project develops and compares machine learning regression models for predicting total body fat percentage using demographic, anthropometric, physical-activity, sedentary-behaviour and dietary variables from NHANES 2011–2012.

The workflow covers data acquisition, merging, cleaning, exploratory data analysis, feature preparation, supervised regression, model evaluation and feature-importance analysis.

## Research Question

Can total body fat percentage be predicted from demographic, anthropometric, physical-activity and dietary variables?

## Dataset

**National Health and Nutrition Examination Survey (NHANES), 2011–2012**  
National Center for Health Statistics (NCHS), Centers for Disease Control and Prevention (CDC).

Files used:

- `DEMO_G` — demographics
- `BMX_G` — body measures
- `PAQ_G` — physical activity
- `DR1TOT_G` — dietary intake
- `DXX_G` — DXA body composition

All files were merged using `SEQN`.

### Dataset size

- Merged: **5,692 observations × 350 variables**
- Final modelling dataset: **3,564 observations × 17 variables**

## Target Variable

`DXDTOPF` — total body fat percentage.

## Predictor Variables

- `RIDAGEYR` — age
- `RIAGENDR` — sex
- `BMXHT` — height
- `BMXWT` — weight
- `BMXBMI` — BMI
- `BMXWAIST` — waist circumference
- `PAQ650`, `PAQ665`, `PAQ710`, `PAQ715` — selected physical-activity/sedentary variables
- `PAD680` — sedentary minutes
- `DR1TKCAL` — energy intake
- `DR1TPROT` — protein intake
- `DR1TCARB` — carbohydrate intake
- `DR1TTFAT` — total fat intake

`SEQN` was used for merging and identification but excluded from modelling.

## Data Preprocessing

1. Load the five NHANES XPT files.
2. Merge using `SEQN`.
3. Select variables relevant to the research question.
4. Examine missing values.
5. Treat specified questionnaire non-response codes as missing for the selected questionnaire variables.
6. Remove incomplete rows from the modelling dataset.
7. Separate predictors and target.
8. Split the data into training and testing sets using an 80:20 split.
9. One-hot encode the categorical sex variable.

## Models

- Linear Regression
- Ridge Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression

## Model Evaluation

Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R²

## Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 2.916 | 3.740 | 0.822 |
| Ridge Regression | 2.916 | 3.740 | 0.822 |
| Decision Tree | 2.968 | 3.799 | 0.816 |
| **Random Forest** | **2.699** | **3.417** | **0.852** |
| Gradient Boosting | 2.721 | 3.440 | 0.849 |

Random Forest achieved the strongest test-set performance among the five models.

### Best-model performance

- MAE: **2.699**
- RMSE: **3.417**
- R²: **0.852**

The R² value indicates that approximately 85.2% of the observed variation in body fat percentage in the held-out test set was explained by the Random Forest model.

## Feature Importance

The Random Forest model identified these as the most influential predictors in this analysis:

| Feature | Importance |
|---|---:|
| Sex | 0.4505 |
| Waist circumference | 0.2340 |
| BMI | 0.1982 |
| Age | 0.0304 |
| Height | 0.0172 |
| Weight | 0.0115 |

Feature importance reflects contribution to model predictions and should not be interpreted as causal evidence.

## Limitations

- One NHANES survey cycle (2011–2012) was used.
- Rows with missing values in the selected modelling variables were excluded.
- The analysis is predictive/observational and does not establish causal relationships.
- Model performance can vary with a different train-test split.
- The selected feature set does not include every possible determinant of body fat percentage.

## Future Scope

- Combine multiple NHANES cycles.
- Apply k-fold cross-validation.
- Tune model hyperparameters.
- Explore additional algorithms.
- Test alternative missing-data strategies.
- Validate the final model on an independent dataset.

## Repository Structure

```text
body-fat-ml-nhanes/
├── README.md
├── requirements.txt
├── model_results.csv
├── feature_importance.csv
├── notebook/
│   └── body_fat_prediction_nhanes.ipynb
├── src/
│   └── body_fat_prediction.py
├── data/
│   ├── README.md
│   ├── DEMO_G.xpt
│   ├── BMX_G.xpt
│   ├── PAQ_G.xpt
│   ├── DR1TOT_G.xpt
│   └── DXX_G.xpt
└── figures/
    ├── body_fat_distribution.png
    ├── bmi_vs_body_fat.png
    ├── body_fat_by_sex.png
    ├── waist_vs_body_fat.png
    ├── correlation_heatmap.png
    ├── feature_importance.png
    ├── actual_vs_predicted.png
    ├── model_error_comparison.png
    └── model_r2_comparison.png
```

## Tools

Python · Pandas · NumPy · Matplotlib · Scikit-learn · Jupyter/Google Colab

## Data Source

Official NHANES portal: https://www.cdc.gov/nchs/nhanes/
