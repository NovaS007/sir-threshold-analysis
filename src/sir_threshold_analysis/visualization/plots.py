import matplotlib.pyplot as plt

from sir_threshold_analysis.simulation.solver import simulate

def plot_simulation(disease,
                    y0,
                    t_end,
                    dt,
                    labels,
                    title=None):
    """
    Generic plotter for any compartment model that returns:
      [(t, y1, y2, ...), ...]
    where y1... are compartments in the same order as `labels`.
    """
    results = simulate(disease,
                       y0,
                       t_end,
                       dt)

    # times = first column
    times = [row[0] for row in results]

    plt.figure(figsize=(10, 6))

    # each compartment is column i+1
    for i, label in enumerate(labels):
        values = [row[i + 1] for row in results]
        plt.plot(times, values, label=label)

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(title or f"{disease.__class__.__name__} Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()