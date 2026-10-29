import pandas as pd
import numpy as np
from collections import defaultdict
import sys

importance_sum = defaultdict(float)
appearances = defaultdict(int)
top5_count = defaultdict(int)

name=str(sys.argv[1])
for seed in range(1, 4001):

    filename = f"rsf_model_{name}_{seed}.txt"

    try:
        df = pd.read_csv(filename,sep=r"\s{2,}",engine="python")
        rows = []

        with open(filename) as f:
            lines = f.readlines()

            for line in lines:

                line = line.strip()

                if (not line
                    or line.startswith("Seed:")
                    or line.startswith("Number of variables:")
                    or "Variable" in line):
                    continue

                try:
                    var, imp = line.rsplit(maxsplit=1)
                    rows.append([var, float(imp)])
                except:
                    print("Could not parse:", repr(line))

            df = pd.DataFrame(rows, columns=["Variable", "Importance"])
    except Exception as e:
        print(f"Skipping {filename}: {e}")
        continue

    # Sort just in case
    df = df.sort_values("Importance", ascending=False)

    # Top 5 variables in this model
    top5_vars = set(df.head(5)["Variable"])

    for _, row in df.iterrows():
        var = row["Variable"]
        imp = float(row["Importance"])

        importance_sum[var] += imp
        appearances[var] += 1

        if var in top5_vars:
            top5_count[var] += 1

# Build summary table
summary = []

for var in appearances:

    n = appearances[var]

    summary.append({
        "Variable": var,
        "MeanImportance": importance_sum[var] / n,
        "Appearances": n,
        "Top5Freq": top5_count[var] / n
    })

summary_df = pd.DataFrame(summary)

summary_df = summary_df.sort_values(
    ["Top5Freq", "MeanImportance"],
    ascending=False
)

summary_df.to_csv(
    "variable_selection_summary_"+name+".csv",
    index=False
)

print(summary_df.head(20))
