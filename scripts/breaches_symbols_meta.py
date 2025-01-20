import itertools
import pandas as pd
import numpy as np

dataset_path = "data/transformed/breaches_symbols.json"
df = pd.DataFrame(pd.read_json(dataset_path))

c_company = df["Company"].nunique()
c_industry = df["Industry"].nunique()

types = list(itertools.chain(*df["Type"]))
c_types = len(set(types))

r_affected = np.ptp(df.loc[df["Affected"] != "Unknown", ["Affected"]])
r_pre = np.ptp(df.loc[~(df["Pre"].isnull()), ["Pre"]])
r_during = np.ptp(df.loc[~(df["During"].isnull()), ["During"]])
r_post = np.ptp(df.loc[~(df["Post"].isnull()), ["Post"]])
r_stock_change = np.ptp(df.loc[~(df["Stock Change"].isnull()), ["Stock Change"]])

print(f"{c_company=} {c_industry=} {c_types=}")
print(f"{r_affected=}")
print(f"{r_pre=} {r_during=} {r_post=}")
print(f"{r_stock_change=}")
