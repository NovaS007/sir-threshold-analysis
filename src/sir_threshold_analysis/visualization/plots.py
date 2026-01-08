import sir_threshold_analysis.models.sir as sir_model
import matplotlib.pyplot as plt

def plot_sir_simulation(disease, y0, t_end, dt):
    """
    Plot the SIR model simulation over time.
    """
    results = disease.simulate(y0, t_end, dt)

    times = [t for t, _, _, _ in results]
    S_values = [S for _, S, _, _ in results]
    I_values = [I for _, _, I, _ in results]
    R_values = [R for _, _, _, R in results]

    plt.figure(figsize=(10, 6))
    plt.plot(times, S_values, label="Susceptible")
    plt.plot(times, I_values, label="Infected")
    plt.plot(times, R_values, label="Recovered")

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("SIR Model Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

disease1 = sir_model.SIRModel(beta=0.3, gamma=0.01, population_size=1000)
plot_sir_simulation(disease1, (999, 1, 0), 100, 0.1)
