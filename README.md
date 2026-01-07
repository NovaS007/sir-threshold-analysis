# SIR Threshold Analysis

An interactive Python framework for simulating and analyzing compartmental epidemic models, with a focus on infection thresholds, parameter sensitivity, and disease dynamics.

## Overview

This project implements classic compartmental epidemiological models—including **SIR** and **SEIR**—to explore how disease spread depends on key parameters such as transmission rate (β) and recovery rate (γ). The primary goal is to study **threshold behavior** (e.g., conditions under which outbreaks grow or die out) through simulation, analysis, and visualization.

The codebase is designed to be modular, extensible, and research-oriented, separating mathematical models, numerical solvers, analysis tools, and visualization logic.

## Features (Current)

- Deterministic SIR and SEIR compartmental models  
- Numerical simulation of disease dynamics  
- Basic CLI interface for running simulations  
- Metrics and sensitivity analysis scaffolding  
- Visualization utilities for time-series plots  
- Unit tests for core model behavior  
- Jupyter notebook for exploratory analysis  

## Project Structure

```text
src/sir_threshold_analysis/
├── analysis/        # Metrics, threshold logic, sensitivity analysis
├── models/          # SIR, SEIR model definitions
├── simulation/      # Solvers and experiment runners
├── visualization/   # Plotting and visualization utilities
├── cli.py           # Command-line interface
```

Additional directories:
- `notebooks/` — exploratory and experimental notebooks  
- `tests/` — unit tests for model correctness  

## Usage

At this stage, the project is primarily intended for development and experimentation.

Example (CLI):

```bash
python -m sir_threshold_analysis.cli
```

Further usage instructions and examples will be added as the project matures.

## Roadmap

Planned improvements include:
- Additional compartmental models (SIRD, SEIRD)
- Interactive visualizations with real-time parameter controls
- More robust threshold and sensitivity analyses
- Improved CLI and/or GUI interfaces
- Documentation of mathematical assumptions and derivations

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
