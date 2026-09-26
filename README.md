# NHANES Body Fat Prediction

Machine learning project predicting body fat percentage using NHANES 2011–2012 data.

## Overview

This project uses data from the National Health and Nutrition Examination Survey (NHANES) to analyze factors associated with body fat percentage and develop machine learning models for prediction.

The project includes:

- Data integration and preprocessing
- Exploratory Data Analysis (EDA)
- Feature analysis
- Regression modelling
- Model comparison
- Feature importance analysis
- Model evaluation

## Objective

The main objective is to predict body fat percentage using demographic, anthropometric, physical activity, and dietary variables.

## Dataset

The analysis uses NHANES 2011–2012 data.

The following datasets were used:

- DEMO_G — Demographic information
- BMX_G — Body measurements
- PAQ_G — Physical activity
- DR1TOT_G — Dietary intake
- DXX_G — Whole-body DXA body composition

The datasets were merged using the participant identifier `SEQN`.

## Machine Learning Models

The following regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Decision Tree
4. Random Forest
5. Gradient Boosting

## Evaluation Metrics

Model performance was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## Key Result

The Random Forest model achieved:

| Metric | Score |
|---|---:|
| MAE | 2.699 |
| RMSE | 3.417 |
| R² | 0.852 |

The model explained approximately 85.2% of the variation in body fat percentage in the test dataset.

## Key Predictors

The Random Forest model identified the following variables as important predictors:

| Feature | Importance |
|---|---:|
| Sex | 0.4505 |
| Waist Circumference | 0.2340 |
| BMI | 0.1982 |

Feature importance represents the contribution of variables to model predictions and should not be interpreted as causal evidence.

## Project Workflow

```text
NHANES Data
      ↓
Data Integration
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Exploratory Data Analysis
      ↓
Data Preprocessing
      ↓
Train-Test Split
      ↓
Model Development
      ↓
Model Evaluation
      ↓
Feature Importance
      ↓
Interpretation
