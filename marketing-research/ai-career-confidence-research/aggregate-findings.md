# Aggregate Research Findings

Selected values transcribed from the SPSS output images embedded in the MKT 5322 team report, *AI Perceptions and Career Confidence Among College Students*. The source report's Figures 1–6 are the evidence for the tables below. They were visually inspected; the models were not rerun. No respondent records, individual responses or original screenshots are included.

## Sample and model scope

Frequency output shows 138 valid observations for the displayed demographic and behavioral variables. The linear model shows total df = 137, residual df = 135 and two predictors, consistent with 138 analyzed cases. This supports the analysis sample size, but does not independently establish how the original submissions were screened.

The binary classification table also totals 138 cases: 65 in category 0 and 73 in category 1. The report interprets these as No and Yes after recoding. The inspected source export labels the unrevised outcome 1 = Yes and 2 = No; final recoding syntax was not available.

## Multiple linear regression

Outcome: response to feeling confident about securing a job after graduation. Predictors: job-replacement anxiety and belief that AI skills improve employability. Source: Figure 4.

| Predictor | B | Standard error | Standardized beta | t | p |
|---|---:|---:|---:|---:|---:|
| Intercept | 2.645 | 0.390 | — | 6.774 | < .001 |
| Job-replacement anxiety | -0.145 | 0.062 | -0.172 | -2.337 | .021 |
| AI employability belief | 0.486 | 0.075 | 0.477 | 6.478 | < .001 |

R-squared = .278; adjusted R-squared = .267; F(2, 135) = 25.982, p < .001; residual standard error = .921. Values are rounded as displayed in the original output. This is model fit on the analyzed sample, not held-out prediction accuracy. The regression ANOVA tests the joint null for the slopes; it is not evidence of a separate group ANOVA.

## Binary logistic regression

Outcome: belief that using AI improves hiring chances, under the report's stated recoding. This is not observed employment. Sources: Figures 5–6.

| Predictor | B | Standard error | Wald statistic | p | Odds ratio |
|---|---:|---:|---:|---:|---:|
| Career confidence | -0.543 | 0.242 | 5.020 | .025 | 0.581 |
| Job-replacement anxiety | -0.371 | 0.173 | 4.586 | .032 | 0.690 |
| AI employability belief | 1.641 | 0.309 | 28.162 | < .001 | 5.161 |
| Intercept | -2.485 | 1.182 | 4.418 | .036 | 0.083 |

Each slope has one degree of freedom. Odds ratios refer to a one-unit increase in a predictor, holding the other predictors constant. For example, 0.690 represents approximately 31% lower modeled odds, not a 31% reduction in probability. The 5.161 odds ratio is not an effect on actual job offers and does not compare an experimentally treated group with a control group.

| Reported model summary | Value | Reading the result |
|---|---:|---|
| Omnibus model chi-square | 49.485, df = 3, p < .001 | Comparison with the intercept-only model on these data |
| -2 log likelihood | 141.359 | A model fit quantity, not an accuracy percentage |
| Cox & Snell pseudo-R-squared | .301 | A likelihood-based summary |
| Nagelkerke pseudo-R-squared | .402 | Not directly equivalent to 40.2% of outcome variance explained in OLS |
| Hosmer–Lemeshow test | 6.042, df = 8, p = .643 | No detected lack of fit by this test; not proof of correct specification or external calibration |

At the displayed .500 classification threshold, the table contains 45 correct category-0 predictions and 58 correct category-1 predictions, with 20 and 15 errors respectively. Thus 103/138 = 74.6% classified correctly after rounding. Always predicting category 1 would give 73/138 = 52.9%. Both are sample-based summaries; no held-out assessment is documented.

## Interpretation boundaries

The portfolio corrects several overstatements in the source narrative: odds are not probabilities, pseudo-R-squared is not OLS variance explained, and a nonsignificant goodness-of-fit test does not establish model validity. The poster labels the logistic dependent variable inconsistently; the report and output variable identify hiring belief, while employability belief is a predictor.

No t-test results, completed k-means solution, demographic group significance findings or causal marketing effects are claimed. Sharing the original respondent data or original team artifacts would require separate privacy and attribution review.
