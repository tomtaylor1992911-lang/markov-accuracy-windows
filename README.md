# Markov accuracy windows in finite quantum reservoirs

Public repository: https://github.com/tomtaylor1992911-lang/markov-accuracy-windows  
Reproducible snapshot: `v1.0.1` (30 October 2026).

Reproducible Python code and source data for **Tolerance-dependent Markov accuracy windows in finite quantum reservoirs** by Xiaxia Cui, Renxin Yu, Qiang Tang, and Jau Tang.

This repository accompanies the revised research manuscript. No publication DOI is assigned here. It contains the numerical implementation, stored numerical data, and exported figures; the manuscript and peer-review correspondence are not included.

## Research question

For a specified initial state, error tolerance and Markov reference, which mechanism first ends the accuracy window, and can a sufficient window be evaluated from the known memory kernel and reference trajectory?

The calculation combines tolerance-resolved first crossings, a continuous reference with the same finite bandwidth, and a reference-defect bound. The finite Lorentzian reservoir is a quantitative benchmark. The analytical scalar construction applies to a convolution Volterra equation with a locally integrable kernel, a unique absolutely continuous solution normalized by `c(0)=1`, and the independently supplied survival-amplitude bound `|c(t)| <= 1`. The population comparison uses `P=|c|^2` and the specified exponential reference; it is not a general density-matrix or channel-error theorem.

## Install

Python 3.10 or newer is recommended. Only NumPy and Matplotlib are required.

```bash
python -m venv .venv
# Activate the environment using the command for your operating system.
python -m pip install -r requirements.txt
```

The package requirements are `numpy>=2.0` and `matplotlib>=3.9`. The stored results were generated with deterministic NumPy algorithms. There are no fitting procedures, random seeds, or stochastic training stages.

## Reproduce figures from the included data

Run from the repository root:

```bash
python code/generate_figures.py --plot-only
```

This reads the included CSV/JSON files and regenerates the PDF, SVG and PNG exports in `figures/`. It does not recompute the numerical trajectories or parameter scans. To redraw only Figure 1:

```bash
python code/revision_numerics.py --figure1-only
```

The overlap-corrected Figure 3, Figure 4 and Figure S1 can be redrawn without recomputation:

```bash
python code/polish_analysis.py --certificate-figure-only
python code/revision_numerics.py --residual-figures-only
```

All eight manuscript and supplementary figures were checked for legend, annotation and axis-label overlap on 30 October 2026. Layout corrections preserve the plotted arrays, line styles, axis limits and ticks.

Individual plotting stages can also be run separately:

```bash
python code/revision_numerics.py --plot-only
python code/polish_analysis.py --plot-only
```

## Recompute the numerical analysis

```bash
python code/generate_figures.py
```

This runs the baseline finite-reservoir calculations, convergence comparisons and cutoff-residual analysis, then the reference-defect and refined tolerance analyses, and finally redraws the figures. It overwrites generated files in `data/` and `figures/`. To keep computation and rendering separate:

```bash
python code/revision_numerics.py --compute-only
python code/polish_analysis.py --compute-only
python code/generate_figures.py --plot-only
```

Full recomputation is more expensive than plot-only reproduction. The large cutoff-sensitivity CSV contains the resolved curves for several cutoffs. Runtime summaries written during recomputation go to the repository-local `validation/` directory, which is ignored by Git; the numerical summaries required for plot-only use are also stored in `data/`.

## Parameters and key values

The baseline numerical parameters are `hbar=1`, `Lambda=2`, `W=16`, `omega0=10`, `gamma=0.08`, and `N_B=256`. Frequencies use the unit `Lambda/2` and times use `2/Lambda`. The exact trajectory begins with an excited subsystem and vacuum reservoir.

| Quantity | Baseline value |
| --- | ---: |
| First 1% population-error crossing | 0.1427799476 |
| First 2% population-error crossing | 0.3508040008 |
| First 5% population-error crossing | 103.3874897 |
| Reference-defect sufficient 5% endpoint | 102.7756444 |
| Finite-grid rephasing scale | 100.5309649 |

The stored scans use coupling ratios `gamma/Lambda = 0.01, 0.04, 0.10, 0.20` and tolerances `0.01, 0.02, 0.05, 0.10`. The initial scan uses 32, 64, 128 and 256 bath modes. The finite bandwidth is retained in the continuous reference.

## Numerical interpretation

The finite-mode Hamiltonian is solved through the spectral representation of the invariant single-excitation sector. The first sampled error-crossing bracket is refined using the analytic amplitude and bisection, with checks under time-grid halving. A continuous finite-band reference is approximated with Gauss-Legendre quadrature and compared against refined quadrature orders and uniform midpoint grids.

`reference_only_bound()` in `polish_analysis.py` uses bare detunings, coupling squares and the prescribed exponential reference. It does not diagonalize the Hamiltonian or evaluate the exact target amplitude. Exact trajectories are evaluated separately for validation and observed-crossing comparisons. The trajectory-dependent cutoff residual is a separate diagnostic and retains exact-trajectory inputs.

The analytical inequalities give sufficient error bounds. Their reported numerical endpoints use converged numerical quadrature, not interval-arithmetic enclosures. Sampled maxima and locally refined peak estimates do not provide strict error envelopes between sampling times. A bound exceeding a tolerance ends sufficient certification; it does not prove that the actual error has crossed the tolerance. These distinctions also apply when comparing the numerical endpoint with the observed first crossing.

## Figure map

| Manuscript figure | Output stem |
| --- | --- |
| Figure 1 | `finite_bath_markov_benchmark` |
| Figure 2 | `tolerance_transition` |
| Figure 3 | `prospective_certificate` |
| Figure 4 | `continuum_residual_benchmark` |
| Supplementary Figure S1 | `finite_bath_residual_diagnostic` |
| Supplementary Figure S2 | `cutoff_sensitivity` |
| Supplementary Figure S3 | `convergence_checks` |
| Supplementary Figure S4 | `short_time_scaling` |

`validity_window_scan` and `approximation_map` are additional generated diagnostic outputs. Source tables and column definitions are indexed in [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

## Repository layout

- `code/`: active numerical and plotting entry points.
- `data/`: numerical source curves, parameter scans and JSON summaries.
- `figures/`: PDF/SVG vector exports and high-resolution PNG previews.
- `validation/`: local runtime output created during recomputation; not versioned.

## License and citation

The Python code is released under the [MIT License](LICENSE). The numerical data and figure files are released under [Creative Commons Attribution 4.0 International](LICENSE-DATA.md). These licenses cover the material in this repository; they do not include third-party software, the unpublished manuscript or review correspondence.

Please cite the authors and manuscript title when using this code or its data. Machine-readable citation metadata are in [CITATION.cff](CITATION.cff). A publication DOI should be added there when one becomes available.
