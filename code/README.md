# Active entry points

- `revision_numerics.py`: baseline finite-reservoir spectral calculation, threshold search, continuous reference and cutoff-residual diagnostics; supports `--compute-only`, `--plot-only` and `--figure1-only`.
- `polish_analysis.py`: reference-defect bound, continuum transient ceilings, refined tolerance scan and small-tolerance comparison; supports `--compute-only` and `--plot-only`.
- `generate_figures.py`: runs both stages, forwarding the shared `--compute-only` or `--plot-only` option.
- `generate_approximation_map.py`: draws the supporting approximation map.

Run commands from the repository root. Numerical algorithms use relative repository paths; no private workspace or external review directory is required. See the root README for the model, numerical interpretation and reproduction commands.
