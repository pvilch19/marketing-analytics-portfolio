"""Reproduce aggregate BigMart comparisons from an authorized clean workbook.

Usage: python analyze_sales.py CLEANED.xlsx --output-dir .
Reads saved Data-sheet values; never modifies the input workbook.
"""
import argparse
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'


def analyze(source, destination):
    data = pd.read_excel(source, sheet_name='Data')
    required = ['Item_Visibility', 'Item_Outlet_Sales', 'Item_Type',
                'Outlet_Type', 'Outlet_Location_Type', 'Outlet_Identifier']
    if not set(required).issubset(data.columns):
        raise ValueError('Workbook is missing required fields')
    if data[required].isna().any().any():
        raise ValueError('Missing analysis fields require review')
    groups = data.groupby(['Outlet_Type', 'Outlet_Location_Type']).agg(
        observations=('Item_Outlet_Sales', 'size'),
        outlets=('Outlet_Identifier', 'nunique'),
        mean_sales=('Item_Outlet_Sales', 'mean')).reset_index()
    categories = data.groupby('Item_Type').agg(
        observations=('Item_Outlet_Sales', 'size'),
        mean_visibility=('Item_Visibility', 'mean'),
        mean_sales=('Item_Outlet_Sales', 'mean')).reset_index()
    row_corr = data['Item_Visibility'].corr(data['Item_Outlet_Sales'])
    category_corr = categories['mean_visibility'].corr(categories['mean_sales'])
    results = {
        'rows': len(data), 'unique_outlets': int(data['Outlet_Identifier'].nunique()),
        'zero_visibility_rows': int(data['Item_Visibility'].eq(0).sum()),
        'row_level_visibility_sales_correlation': row_corr,
        'category_mean_visibility_sales_correlation': category_corr,
        'outlet_groups': groups.to_dict(orient='records'),
        'category_means': categories.to_dict(orient='records')}
    destination = Path(destination)
    figures = destination/'figures'
    figures.mkdir(parents=True, exist_ok=True)
    (destination/'sales-findings.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
    fig, ax = plt.subplots(figsize=(9, 4.8))
    labels = [f"{r.Outlet_Type} / {r.Outlet_Location_Type}\n{r.outlets} outlet(s), {r.observations:,} observations"
              for r in groups.itertuples()]
    bars = ax.barh(labels, groups['mean_sales'], color='#276e90')
    ax.bar_label(bars, fmt='%.2f', padding=4)
    ax.set(xlabel='Mean item-outlet sales (source units)',
           title='Observed outlet/location groups')
    ax.set_xlim(0, groups['mean_sales'].max()*1.16)
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(figures/'sales-by-outlet-group.svg')
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.scatter(categories['mean_visibility'], categories['mean_sales'], color='#276e90')
    for name in ['Seafood', 'Breakfast', 'Health and Hygiene']:
        r = categories.loc[categories['Item_Type'].eq(name)].iloc[0]
        ax.annotate(name,(r['mean_visibility'],r['mean_sales']),xytext=(4,5),textcoords='offset points',fontsize=8)
    ax.set(xlabel='Category mean visibility (source units)',
           ylabel='Category mean sales (source units)',
           title=f'16 category averages: r = {category_corr:.3f}')
    ax.text(0.02,0.02,f'Individual observations: r = {row_corr:.3f}\nAggregation changes the apparent relationship.',
            transform=ax.transAxes, fontsize=9)
    ax.margins(x=0.18,y=0.18)
    fig.tight_layout()
    fig.savefig(figures/'visibility-category-comparison.svg')
    plt.close(fig)
    print(json.dumps({k:v for k,v in results.items() if k not in ['outlet_groups','category_means']},indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook')
    parser.add_argument('--output-dir', default='.')
    args = parser.parse_args()
    analyze(args.workbook, args.output_dir)
