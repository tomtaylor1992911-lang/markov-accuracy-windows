"""Run both numerical stages and regenerate all published figure outputs.

Use --plot-only to redraw the included data without recomputing dynamics.
Use --compute-only to recompute data without rendering plots.
"""
from revision_numerics import main as base_main
from polish_analysis import main as polish_main

if __name__ == "__main__":
    base_main()
    polish_main()
