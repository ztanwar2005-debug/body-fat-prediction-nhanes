import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load NHANES 2011–2012 source files
demo = pd.read_sas("data/DEMO_G.xpt")
bmx = pd.read_sas("data/BMX_G.xpt")
paq = pd.read_sas("data/PAQ_G.xpt")
dxx = pd.read_sas("data/DXX_G.xpt")
diet = pd.read_sas("data/DR1TOT_G.xpt")

# Merge all components on participant ID
df = (
    demo.merge(bmx, on="SEQN", how="inner")
        .merge(paq, on="SEQN", how="inner")
        .merge(dxx, on="SEQN", how="inner")
        .merge(diet, on="SEQN", how="inner")
)

print("Merged shape:", df.shape)

selected_vars = [
    "SEQN","RIDAGEYR","RIAGENDR","BMXHT","BMXWT","BMXBMI","BMXWAIST",
    "PAQ650","PAQ665","PAD680","PAQ710","PAQ715",
    "DR1TKCAL","DR1TPROT","DR1TCARB","DR1TTFAT","DXDTOPF"
]

ml_df = df[selected_vars].copy()

# Selected questionnaire variables: convert specified non-response codes to missing
paq_vars = ["PAQ650", "PAQ665", "PAQ710", "PAQ715"]
for col in paq_vars:
    ml_df[col] = ml_df[col].replace(
        [7, 9, 77, 99, 777, 999, 7777, 9999], pd.NA
    )

# Complete-case dataset for modelling
ml_clean = ml_df.dropna().copy()
print("Final modelling shape:", ml_clean.shape)

# Predictors and target
X = ml_clean.drop(columns=["SEQN", "DXDTOPF"])
y = ml_clean["DXDTOPF"]

# 80:20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# One-hot encode sex
X_train = pd.get_dummies(X_train, columns=["RIAGENDR"], drop_first=True)
X_test = pd.get_dummies(X_test, columns=["RIAGENDR"], drop_first=True)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    ),
    "Gradient Boosting": GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    results.append({
        "Model": name,
        "MAE": mean_absolute_error(y_test, pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, pred)),
        "R2": r2_score(y_test, pred)
    })

results_df = pd.DataFrame(results)
print(results_df.round(3))
