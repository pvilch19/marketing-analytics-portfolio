# Graduate coursework models, prepared for standalone portfolio reproduction.
# Original formulas retained; explicit imports and factor reference replace attach().
# Usage: Rscript --vanilla regression-models.R data .
# Authorized CSV exports only; no data downloads or source-file changes.

args <- commandArgs(trailingOnly = TRUE)
input_dir <- if (length(args) >= 1) args[1] else "data"
output_dir <- if (length(args) >= 2) args[2] else "."

read_input <- function(filename, fields) {
  path <- file.path(input_dir, filename)
  if (!file.exists(path)) stop("Supply an authorized CSV: ", filename)
  x <- read.csv(path, check.names = FALSE)
  if (!all(fields %in% names(x))) stop("Missing required fields in ", filename)
  x <- x[, fields, drop = FALSE]
  if (anyNA(x)) stop("Missing values require review in ", filename)
  x
}
linear <- read_input("linear.csv", c("Experience", "Salary"))
ads <- read_input("poly.csv", c("online", "purchases"))
awards <- read_input("poisson.csv", c("awards", "program", "score"))
for (x in list(linear, ads, awards[, c("awards", "score")])) {
  if (!all(vapply(x, is.numeric, logical(1))) || any(!is.finite(as.matrix(x)))) {
    stop("Model variables must be finite numeric values.")
  }
}
if (any(awards$awards < 0 | awards$awards != floor(awards$awards))) {
  stop("Poisson outcomes must be nonnegative integer counts.")
}
if (!setequal(unique(awards$program), c("Academic", "General", "Vocational"))) {
  stop("Review program categories before changing the reference group.")
}
awards$program <- factor(awards$program, levels = c("Academic", "General", "Vocational"))
ads$online_2 <- ads$online^2
models <- list(
  salary_linear = lm(Salary ~ Experience, data = linear),
  advertising_linear = lm(purchases ~ online, data = ads),
  advertising_quadratic = lm(purchases ~ online + online_2, data = ads),
  awards_poisson = glm(awards ~ program + score, data = awards, family = poisson(link = "log"))
)

metrics <- do.call(rbind, lapply(names(models), function(name) {
  m <- models[[name]]
  s <- summary(m)
  is_count <- inherits(m, "glm")
  data.frame(model = name, n = nobs(m),
    r_squared = if (is_count) NA_real_ else s$r.squared,
    adjusted_r_squared = if (is_count) NA_real_ else s$adj.r.squared,
    aic = AIC(m), residual_df = df.residual(m))
}))
coefficients <- do.call(rbind, lapply(names(models), function(name) {
  m <- models[[name]]
  c <- coef(summary(m))
  data.frame(model = name, term = rownames(c), estimate = c[, 1],
    std_error = c[, 2], statistic = c[, 3], p_value = c[, 4],
    test = if (inherits(m, "glm")) "z" else "t",
    exp_coefficient = if (inherits(m, "glm")) exp(c[, 1]) else NA_real_,
    row.names = NULL)
}))
b <- coef(models$advertising_quadratic)
turning_point <- -b["online"] / (2 * b["online_2"])
maximum_supported <- b["online_2"] < 0 && turning_point >= min(ads$online) && turning_point <= max(ads$online)
notes <- data.frame(
  measure = c("advertising_turning_point", "advertising_min", "advertising_max",
    "quadratic_maximum_within_observed_range", "poisson_pearson_dispersion"),
  value = c(turning_point, min(ads$online), max(ads$online), as.numeric(maximum_supported),
    sum(residuals(models$awards_poisson, type = "pearson")^2) / df.residual(models$awards_poisson))
)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(metrics, file.path(output_dir, "model-comparison.csv"), row.names = FALSE, na = "")
write.csv(coefficients, file.path(output_dir, "coefficients.csv"), row.names = FALSE, na = "")
write.csv(notes, file.path(output_dir, "model-checks.csv"), row.names = FALSE)
cat("Completed four fits across three model types; aggregate outputs written.\n")
cat("No held-out evaluation or causal inference is performed.\n")
