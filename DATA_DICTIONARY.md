# Numerical source-data dictionary

Times use `2/Lambda` and frequencies use `Lambda/2`, with baseline numerical `Lambda=2`. Populations, trace distances and tolerances are dimensionless. Where a column denotes a maximum from a sampled grid, its interpretation is numerical rather than a certified continuous-interval supremum. The CSV header is the canonical column name; no columns are renamed for release.

## `continuum_reference.csv`

Baseline same-bandwidth continuous-reference population and finite-mode comparisons.

Columns: `time`, `P_gauss1024`, `P_gauss768`, `P_gauss512`, `P_N32`, `P_N256`, `P_Markov`, `finite_grid_error_N32`, `finite_grid_error_N256`, `finite_memory_markov_error`.

## `continuum_transient_ceiling.csv`

Numerically estimated transient peak times/heights and comparison-grid checks for four couplings.

Columns: `gamma_over_Lambda`, `gamma`, `horizon`, `peak_time`, `delta_star`, `finite_N256_peak_time`, `finite_N256_delta_star`, `gauss768_to1024_max_population_difference`, `finite_N256_to_continuum_max_population_difference`.

## `continuum_transient_curves.csv`

Continuous-reference/Markov transient error curves for four couplings.

Columns: `gamma_over_Lambda`, `time`, `continuum_markov_error`.

## `cutoff_sensitivity.csv`

Resolved population and error/bound traces for the stated memory cutoffs.

Columns: `tau_c`, `time`, `actual_residual`, `residual_bound`, `amplitude_error_to_cutoff`, `weighted_amplitude_bound`, `population_error_to_cutoff`, `population_cutoff_bound`, `rate_mismatch`, `population_markov_bound`.

## `dense_tolerance_transition.csv`

Refined tolerance scan around the initial-error ceiling, with early and late branch identifiers.

Columns: `N_B`, `gamma_over_Lambda`, `gamma`, `tolerance`, `tolerance_over_continuum_ceiling`, `t_first_exit`, `branch_0_early_1_late`, `continuum_delta_star`, `finite_N256_delta_star`.

## `finite_bath_benchmark.csv`

Mode-count scan, spacing, rephasing scale, first 5% crossing and pre-rephasing sampled error.

Columns: `N_B`, `delta_omega`, `t_recurrence`, `t_first_D_gt_0.05`, `max_error_before_recurrence`.

## `finite_bath_curves.csv`

Baseline time traces of normalized correlations, exact and Markov populations, and population errors for 32 and 256 modes.

Columns: `time`, `correlation_abs_N32`, `correlation_abs_N256`, `P_N32`, `P_N256`, `P_Markov`, `D_N32`, `D_N256`.

## `finite_bath_residual.csv`

Resolved actual cutoff residual, its components, propagated bounds, rate mismatch and population comparisons.

Columns: `time`, `actual_residual`, `state_variation_bound`, `initial_slip_bound`, `correlation_tail`, `total_bound`, `weighted_actual_residual`, `weighted_total_bound`, `actual_amplitude_error_to_cutoff`, `actual_population_error_to_cutoff`, `population_cutoff_bound`, `rate_mismatch`, `population_markov_bound`, `P_exact`, `P_cutoff`, `P_Markov`.

## `numeric_results_polish.json`

Structured reference-only endpoints, quadrature refinements, transient ceilings and small-tolerance summaries.

Top-level keys: `parameters`, `scope`, `prospective_inputs`, `numerical_status`, `reference_only_compute_seconds`, `reference_only_convergence`, `exact_validation_compute_seconds`, `reference_only_windows`, `baseline_prefactor_comparison`, `continuum_transient_ceiling`, `short_time_scaling`, `time_seconds`.

## `numerical_results.json`

Structured baseline parameters, mode scans, threshold/convergence checks, cutoff summaries and runtime notes.

Top-level keys: `model`, `definitions`, `threshold_scan`, `threshold_grid_max_difference`, `benchmark`, `dense_eigh_checks`, `quadrature_convergence`, `continuum_reference_max_time`, `continuum_markov_max_error_0_to_10`, `continuum_markov_max_error_0_to_125`, `finite_grid_max_error_0_to_80`, `residuals`, `residual_grid_convergence`, `walltime_seconds`, `numerical_notes`, `verification_checks`.

## `quadrature_convergence.csv`

Population/amplitude differences for quadrature orders and uniform midpoint references.

Columns: `scheme`, `order`, `max_amplitude_difference_to_gauss1024`, `max_population_difference_to_gauss1024`.

## `reference_only_certificate.csv`

Baseline reference-defect amplitude/population bound and validation/error traces.

Columns: `time`, `reference_residual_abs`, `reference_amplitude_bound`, `reference_population_bound`, `reference_population_bound_coarse`, `actual_population_error`, `aposteriori_population_bound`, `aposteriori_bound_one_plus_cc`, `aposteriori_bound_two`.

## `reference_only_window_scan.csv`

Reference-only sufficient endpoints and observed first exits for four couplings and four tolerances.

Columns: `N_B`, `gamma_over_Lambda`, `gamma`, `tolerance`, `horizon`, `reference_only_bound_end`, `observed_first_exit`, `bound_end_over_observed`.

## `short_time_scaling.csv`

Small-tolerance first exits and normalized ratios used to check the leading short-time scaling.

Columns: `gamma_over_Lambda`, `gamma`, `tolerance`, `tolerance_over_delta_star`, `t_first_exit`, `gamma_t_exit_over_delta`, `first_order_ratio`.

## `threshold_convergence.csv`

First-crossing agreement under halved threshold sampling grids.

Columns: `N_B`, `gamma_over_Lambda`, `tolerance`, `coarse_dt`, `fine_dt`, `coarse_crossing`, `fine_crossing`, `absolute_difference`.

## `validity_window_scan.csv`

Initial 64-case mode-count/coupling/tolerance first-crossing scan.

Columns: `N_B`, `gamma_over_Lambda`, `gamma`, `tolerance`, `delta_omega`, `t_recurrence`, `horizon`, `t_first_exit`, `t_first_exit_over_recurrence`.
