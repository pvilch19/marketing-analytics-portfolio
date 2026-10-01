# Model Calculations

Based on the named Assignment 3 submission, worksheet **Raw data**. The source workbook is excluded; the cell references below identify the calculations reviewed, not downloadable files. Model assumptions are supplied coursework inputs.

## Source calculation guide

| Model component | Source cell(s) | Formula or value |
|---|---|---|
| Demand table | E2:F41 | Every demand cell uses `15000 − 200 × price` |
| Printer cost | I3 | 10 |
| Cartridge price, annual quantity and cost | I7:I9 | 10; 4; 5 |
| Printer-only price and cost | I15:I16 | 42.5; 10 |
| Printer-only demand | I17 | `=15000-(200*(I15))` |
| Printer-only contribution | I18 | `=I17*(I15-I16)` |
| Printer-only total | I20 | `=I18` |
| Combined-case printer price | I24 | Saved as 32.499999765625034, rounded to 32.50 |
| Combined-case cartridge price | J24 | 10 |
| Combined-case unit costs | I25:J25 | 10; 5 |
| Combined-case printer demand | I26 | `=15000-(200*(I24))` |
| Cartridge volume | J26 | `=4*I26` |
| Printer contribution | I27 | `=I26*(I24-I25)` |
| Cartridge contribution | J27 | `=J26*(J24-J25)` |
| Combined contribution | I29 | `=I27+J27` |

The demand chart references E2:E41 and F2:F41 and contains linear trend lines. Since the demand cells already follow an exact supplied equation, the chart does not demonstrate empirical estimation of price sensitivity.

## Analytical verification added for the portfolio

For printer-only contribution:

`C_printer(p) = (p − 10)(15,000 − 200p)`

`dC_printer/dp = 17,000 − 400p`

Setting the derivative to zero gives **p = 42.50**, demand **6,500**, and contribution **211,250**.

Each printer generates assumed cartridge contribution of `4 × (10 − 5) = 20`. Therefore:

`C_combined(p) = (p − 10 + 20)(15,000 − 200p)`

`dC_combined/dp = 13,000 − 400p`

Setting the derivative to zero gives **p = 32.50**, demand **8,500**, printer contribution **191,250**, cartridge contribution **170,000**, and total **361,250**.

Both second derivatives equal **−400**, so these stationary points are maxima for their respective quadratic objectives. Both lie in the economically meaningful range `0 ≤ p ≤ 75`, where price and modeled demand are nonnegative. That range is used for the portfolio's mathematical check, not asserted as a saved Solver constraint.

## Comparable contribution at both prices

| Calculation | At $42.50 | At $32.50 |
|---|---:|---:|
| Printer revenue: pQ | $276,250 | $276,250 |
| Printer variable cost: 10Q | $65,000 | $85,000 |
| Printer contribution | $211,250 | $191,250 |
| Cartridge revenue: 10 × 4Q | $260,000 | $340,000 |
| Cartridge variable cost: 5 × 4Q | $130,000 | $170,000 |
| Cartridge contribution | $130,000 | $170,000 |
| Combined contribution | $341,250 | $361,250 |

The revenue breakdown and combined outcome at $42.50 are portfolio calculations derived from the original formulas. They distinguish the **$20,000 modeled benefit of changing price under the combined objective** from the unrelated comparison of objectives that include different products. No figures represent observed business gains.

## Verification scope

All 84 formula cells in the named workbook were independently evaluated and matched their stored numerical values within floating-point tolerance. The analytical optima were also checked against a one-cent price grid from 0 through 75. This verifies arithmetic and these mathematical objectives; it does not validate demand assumptions or rerun Excel Solver.

Saved Solver names point to I24 as the changing cell and I29 as the objective. The submission's text refers to clicking Solver and discusses both optimized prices. No Answer Report, Sensitivity Report or convergence log was found. Some residual constraint-name entries are also present in the uncompleted template; they are not treated as proof of active constraints. A separate saved printer-only Solver setup is not available.

The source comparison text repeats the question number for the second scenario. This summary identifies that scenario as printer-plus-cartridge pricing and retains the supported prices and arithmetic.
