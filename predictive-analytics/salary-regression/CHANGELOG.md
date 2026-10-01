# Analysis changes

- Replaced Colab-mounted input with the relative path `data/Salary_Data.csv`.
- Added `random_state=42` to the ML split. The original split was unseeded, so its stored results differ from this reproducible version.
- Retained OLS on all 30 observations and a separate 70/30 ML evaluation.
- Added held-out MAE and RMSE alongside R².
- Removed individual source rows from displayed output; actual/predicted comparisons remain available in memory.
- Clarified association, sample-size limitations and the distinction between training fit and test evaluation.
- Executed both revised notebooks successfully on September 30, 2026. Exact tested package versions are recorded in requirements.txt.
