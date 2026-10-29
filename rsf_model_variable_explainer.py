import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sksurv.ensemble import RandomSurvivalForest
from sksurv.metrics import concordance_index_censored
from sksurv.util import Surv
import json
import sys
from sklearn.inspection import permutation_importance

filename=str(sys.argv[1])
status=str(sys.argv[2])
time_variable=str(sys.argv[3])
name=str(sys.argv[4])
seed = int(sys.argv[5]) # Seed provided as argument

# ------------------ Load and Prepare Data ------------------ #
data = pd.read_csv(filename)
X = data.drop(columns=[time_variable, status])
y = Surv.from_dataframe(status, time_variable, data)

rng = np.random.default_rng(seed)

# Randomly select 40 columns without replacement
selected_cols = rng.choice(X.columns, size=40, replace=False)

X = X[selected_cols]

print("Selected variables:")
print(list(selected_cols))

best_model = RandomSurvivalForest(
    n_estimators=500,
    max_depth=None,
    min_samples_split=5,
    min_samples_leaf=5,
    max_features="sqrt",
    bootstrap=True,
    random_state=seed,   # use the model seed
    n_jobs=1
)

best_model.fit(X, y)

def cindex_scorer(estimator, X, y):
    pred = estimator.predict(X)
    return concordance_index_censored(
        y[status],
        y[time_variable],
        pred
    )[0]

# Permutation importance
perm = permutation_importance(
    best_model,
    X,
    y,
    scoring=cindex_scorer,
    n_repeats=5,
    random_state=seed,
    n_jobs=1
)

importance_df = pd.DataFrame({
    "Variable": X.columns,
    "Importance": perm.importances_mean
}).sort_values("Importance", ascending=False)

# Save
outfile = f"rsf_model_{name}_{seed}.txt"

with open(outfile, "w") as f:
    f.write(importance_df.to_string(index=False))

print(f"Saved feature importances to {outfile}")

