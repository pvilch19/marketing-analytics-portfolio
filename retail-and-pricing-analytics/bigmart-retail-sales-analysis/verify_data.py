"""Recheck the supplied BigMart workbooks without changing either source file.

Run: python verify_data.py ORIGINAL.xlsx CLEANED.xlsx
Dependencies: pandas, openpyxl. Outputs aggregate checks to standard output.
This validation utility was added during portfolio preparation.
"""
import json
import sys
import pandas as pd


def verify(original_path, cleaned_path):
    original = pd.read_excel(original_path, sheet_name="Data")
    cleaned = pd.read_excel(cleaned_path, sheet_name="Data")
    expected = original["Item_Fat_Content"].replace(
        {"LF": "Low Fat", "low fat": "Low Fat", "reg": "Regular"}
    )
    return {
        "original_rows": len(original),
        "original_columns": len(original.columns),
        "cleaned_rows": len(cleaned),
        "cleaned_columns": len(cleaned.columns),
        "original_columns_preserved": original.equals(cleaned[original.columns]),
        "cleaned_missing_cells": int(cleaned.isna().sum().sum()),
        "fat_labels_match_expected": expected.equals(cleaned["Item_Fat_Content_Clean"]),
        "outlet_age_matches_2026_reference": bool(
            (cleaned["Outlet_Age"] == 2026 - cleaned["Outlet_Establishment_Year"]).all()
        ),
        "zero_visibility_rows": int((cleaned["Item_Visibility"] == 0).sum()),
        "sales_mean": float(cleaned["Item_Outlet_Sales"].mean()),
        "sales_median": float(cleaned["Item_Outlet_Sales"].median()),
        "sales_min": float(cleaned["Item_Outlet_Sales"].min()),
        "sales_max": float(cleaned["Item_Outlet_Sales"].max()),
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Provide original and cleaned workbook paths.")
    print(json.dumps(verify(sys.argv[1], sys.argv[2]), indent=2))
